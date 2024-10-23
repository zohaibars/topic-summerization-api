import logging
import re
import time
from app.utils.connections import  openai_client
from app.core.agents.spell_check_agent.spell_check_util import SpellingsOutputParser
from app.core.agents.spell_check_agent.chains import get_spell_check_chain

logging.basicConfig(level="INFO")
logger = logging.getLogger(__name__)

def check_spellings(text: str):
    llm = openai_client()
    spell_check_chain = get_spell_check_chain(llm)
    parser = SpellingsOutputParser(original=text)
    err_correction_str = spell_check_chain.invoke(
        {
            "urdu": text
        }
    )
    final_spell_check = parser.parse(process_str=err_correction_str)
    logger.info(final_spell_check)
    return final_spell_check
