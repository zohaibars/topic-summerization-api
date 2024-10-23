import logging
import re
import time
from app.utils.connections import  llms_clients_lang
from app.core.agents.urdu_nouns_agent.nouns_util import Urdu_stop_words, NounsOutputParser
from app.core.agents.urdu_nouns_agent.chain import get_nouns_chain

logging.basicConfig(level="INFO")
logger = logging.getLogger(__name__)

llm = llms_clients_lang(model="llama-3.1-70b-versatile")

def get_nouns(model: str = "", text: str = ""):
    logger.info("Extracting Nouns")
    start = time.time()
    if model:
        llm = llms_clients_lang(model=model)
    nouns_chain = get_nouns_chain(llm)
    parser = NounsOutputParser(original_text=text)
    extractions = nouns_chain.invoke(
        {
            "text": parser.processed_text
        }
    )
    final_nouns = parser.parse(text=extractions)
    end = time.time()
    logger.info(final_nouns)
    time_taken = end - start
    logger.info(f"Extraction took {time_taken}s")
    return final_nouns
