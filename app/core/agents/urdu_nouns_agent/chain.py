from app.core.prompts.nouns_prompt import (
    NOUNS_SYSTEM_PROMPT,
    NOUNS_PROMPT
)
from langchain_core.output_parsers.string import StrOutputParser

from langchain_core.prompts import PromptTemplate

def get_nouns_chain(llm):
    nouns_prompt = PromptTemplate.from_template(NOUNS_PROMPT)
    nouns_chain = nouns_prompt | llm | StrOutputParser()
    return nouns_chain