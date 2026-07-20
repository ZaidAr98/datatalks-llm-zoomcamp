from dotenv import load_dotenv
load_dotenv()

from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import ConsoleSpanExporter, SimpleSpanProcessor

provider = TracerProvider()
provider.add_span_processor(SimpleSpanProcessor(ConsoleSpanExporter()))
trace.set_tracer_provider(provider)

tracer = trace.get_tracer("llm-zoomcamp")

from starter import index, client
from rag_helper import RAGBase


def calculate_cost(usage):
    return (usage.input_tokens * 0.15 + usage.output_tokens * 0.60) / 1_000_000


class RAGTraced(RAGBase):
    def search(self, query, num_results=5):
        with tracer.start_as_current_span("search"):
            return super().search(query, num_results=num_results)

    def llm(self, prompt):
        with tracer.start_as_current_span("llm") as span:
            response = super().llm(prompt)
            usage = response.usage
            span.set_attribute("input_tokens", usage.input_tokens)
            span.set_attribute("output_tokens", usage.output_tokens)
            span.set_attribute("cost", calculate_cost(usage))
            return response

    def rag(self, query):
        with tracer.start_as_current_span("rag"):
            return super().rag(query)


rag = RAGTraced(index=index, llm_client=client)

if __name__ == "__main__":
    query = "How does the agentic loop keep calling the model until it stops?"
    answer = rag.rag(query)
    print(answer)