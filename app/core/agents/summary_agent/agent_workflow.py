from langgraph.graph import END
from app.utils.models import TopicSummariesState
from app.core.graph_builder.graph import GraphBuilder
from app.core.prompts.summary_prompt import (
    TOPIC_SUMMARIZATION_PROMPT,
    RUNNING_SUMMARY_PROMPT
)
from langchain_core.output_parsers.string import StrOutputParser
from langchain_core.prompts import PromptTemplate

# Topcis chain
def get_topic_chain(llm):
    topic_prompt = PromptTemplate.from_template(TOPIC_SUMMARIZATION_PROMPT)
    topic_summarization_chain = topic_prompt | llm | StrOutputParser()
    return topic_summarization_chain
# Running summary  chain
def get_summary_chain(llm):
    running_summary_prompt = PromptTemplate.from_template(RUNNING_SUMMARY_PROMPT)
    running_summary_chain = running_summary_prompt | llm | StrOutputParser()
    return running_summary_chain

# Topic summary Graph
def summarizer_node(state: TopicSummariesState):
    state["step"] = "parser_linter"
    return state


def verifier_node(state: TopicSummariesState):
    state["step"] = "unit_test_generator"
    return state

def translator_node(state: TopicSummariesState):
    state["step"] = "unit_test_generator"
    return state

def extraction_node(state: TopicSummariesState):
    state["extractions"] = "response_parsed_from_LLM"
    return state

def router(state: TopicSummariesState):
    
    return state["step"]

def get_topic_graph():
    nodes = {
        "extractor": extraction_node,
        "summarizer": summarizer_node,
        "verifier": verifier_node,
        "translator": translator_node,
    }
    edges = [
        {
            "from": "extractor",
            "condition": "",
            "to": "summarizer",
        },
        {
            "from": "summarizer",
            "condition": "",
            "to": "verifier",
        },
        {
            "from": "verifier",
            "condition": router,
            "to": {"summarizer": "summarizer", "translator": "translator"},
        },
        {
            "from": "translator",
            "condition": "",
            "to": END,
        },
    ]
    graph_builder = GraphBuilder(
        state=TopicSummariesState,
        nodes=nodes,
        edges=edges,
        entrypoint="extractor"
    )
    graph = graph_builder.build_graph()
    return graph

graph = get_topic_graph()