import logging
from fastapi import APIRouter, HTTPException
from app.core.agents.urdu_nouns_agent.word_cloud_core import get_nouns
from app.utils.models import Text, Nouns

router = APIRouter()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@router.post(
    "/nouns-70b/",
    response_model=Nouns
)
async def extract_nouns(request: Text):
    try:
        model = "llama-3.1-70b-versatile"
        nouns = get_nouns(model=model, text=request.text)
        return nouns
    except Exception as ex:
        logger.error(f"Failed to extract words: {ex}")
        if ex.status_code == 429:
            raise HTTPException(status_code=429, detail=f"{ex}")    
        raise HTTPException(status_code=500, detail="Internal Server Error")


@router.post(
    "/nouns-8b/",
    response_model=Nouns
)
async def extract_nouns(request: Text):
    try:
        nouns = get_nouns(model="llama-3.1-8b-instant", text=request.text)
        return nouns
    except Exception as ex:
        logger.error(f"Failed to extract words: {ex}")
        if ex.status_code == 429:
            raise HTTPException(status_code=429, detail=f"{ex}")
        raise HTTPException(status_code=500, detail="Internal Server Error")