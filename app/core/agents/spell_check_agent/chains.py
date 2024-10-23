from app.core.prompts.spell_check_prompt import SPELL_CHECK_PROMPT, SPELL_CHECK_SYSTEM_PROMPT
from langchain_core.output_parsers.string import StrOutputParser

from langchain_core.prompts import ChatPromptTemplate

def get_spell_check_chain(llm):
    messages = [
        (
            "system", 
            SPELL_CHECK_SYSTEM_PROMPT
        ),
        (
            "human",
            SPELL_CHECK_PROMPT
        )
    ]
    prompt = ChatPromptTemplate.from_messages(messages)
    nouns_chain = prompt | llm | StrOutputParser()
    return nouns_chain