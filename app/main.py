from fastapi import FastAPI
from app.api.endpoints import spell_check, summary, urdu_nouns
app = FastAPI(
    title="llm-api"
)

@app.get("/")
async def root():
    return {"Status": "Healthy"}

app.include_router(summary.router, prefix="/summarize", tags=["summary"])
app.include_router(urdu_nouns.router, prefix="/word-cloud", tags=["word_cloud"])
app.include_router(spell_check.router, prefix="/spell-check", tags=["spell_check"])
