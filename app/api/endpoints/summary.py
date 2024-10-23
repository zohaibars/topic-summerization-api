import logging
from fastapi import APIRouter, HTTPException
from app.core.agents.summary_agent.summarization_core import get_summary
from app.utils.models import Docs, summaryResponse

router = APIRouter()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@router.post("/extract-8b/")
async def summarize(docs: Docs):
    try:
        logger.info("Summazrizing using 8b")
        summary = get_summary(model="llama3-8b-8192", docs=docs.input, running_summary=[""])
        return summary
    except Exception as ex:
        logger.error(f"Failed to generate summary report: {ex}")
        if ex.status_code == 429:
            raise HTTPException(status_code=429, detail=f"{ex}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

@router.post(
    "/extract-70b/",
    response_model=summaryResponse
)
async def summarize(docs: Docs):
    try:
        logger.info("Summazrizing using 70b")
        summary = get_summary(model="llama3-70b-8192", docs=docs.input, running_summary=docs.running_summaries)
        response = summaryResponse(response=summary)
        return response
    except Exception as ex:
        logger.error(f"Failed to generate summary report: {ex}")
        if ex.status_code == 429:
            raise HTTPException(status_code=429, detail=f"{ex}")
        raise HTTPException(status_code=500, detail="Internal Server Error")
