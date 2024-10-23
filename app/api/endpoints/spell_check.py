import logging
from fastapi import APIRouter, HTTPException
from app.core.agents.spell_check_agent.spell_check_core import check_spellings
from app.utils.models import Text, UrduSpellCheck


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

router = APIRouter()

@router.post(
    "/check/",
    response_model=UrduSpellCheck
)
async def check(request: Text):
    try:
        logger.info("Making spell checks.")
        spelling_report = check_spellings(request.text)
        logger.info("Report Generated")
        return spelling_report
    except Exception as ex:
        logger.error(f"Failed to generate spelling report: {ex}")
        if ex.status_code == 429:
            raise HTTPException(status_code=429, detail=f"{ex}")
        raise HTTPException(status_code=500, detail="Internal Server Error")
