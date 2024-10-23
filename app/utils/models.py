import re
import logging
from pydantic import BaseModel, Field, model_validator
from typing import List, Optional, Dict, Any

logging.basicConfig(level="INFO")
logger = logging.getLogger(__name__)

class Docs(BaseModel):
    input: List[str]
    running_summaries: List[str]


class userInput(BaseModel):
    question: str
    chat_history: Optional[list]


class summaryResponse(BaseModel):
    response: Dict[str, Any]


class Text(BaseModel):
    text: str = Field(description="Input text for which requests are made for processing")


class Nouns(BaseModel):
    text: str = Field(description="Text excluding stop words.")
    nouns: List[str] = Field(description="List of Proper Nouns.")
    frequencies: Dict[str, int] = Field(description="Frequency of each unique proper noun in words list.")
    
    @model_validator(mode="before")
    @classmethod
    def fill_count(cls, values):
        text = values.get("text", "")
        nouns = values.get("nouns", [])
        unique_nouns = list(set(nouns))
        values["nouns"] = unique_nouns
        freq = values.get("frequencies", {})
        if not freq:
            for noun in unique_nouns:
                count = len(re.findall(r'\b' + re.escape(noun) + r'\b', text))
                if count:
                    freq[noun] = freq.get(noun, 0) + count
                else:
                    freq[noun] = freq.get(noun, 0) + 1
        values["frequencies"] = freq
        return values

# spell check model
class UrduSpellCheck(BaseModel):
    urdu_text: str = Field(..., description="The Urdu text to be checked.")
    error_corrections: List[Dict[str, str]] = Field(..., description="List of dictionaries containing detected errors and their suggested corrections.")
    mistakes_count: int = Field(default_factory=int, description="Estimated count of mistakes in the text.")
    error_rate: float = Field(default_factory=float, description="Error rate in the original Urdu text.")

    @model_validator(mode="before")
    @classmethod
    def analysis(cls, values):
        text = values.get("urdu_text", "")
        errors = values.get("error_corrections", [])
        mistakes_count = 0
        for err in errors:
            word = err["error"]
            mistakes = len(re.findall(r"\b" + re.escape(word) + r"\b", text))
            if mistakes:
                mistakes_count += mistakes
            else:
                mistakes_count += 1
        word_count = len(text.split())
        values["mistakes_count"] = mistakes_count
        values["error_rate"] = (mistakes_count / word_count)* 100
        return values

# Topic summary models
class Topics(BaseModel):
    topic_summaries: List[Dict[str, str]] = Field(description="List of dictionaries with two fields topics and their summaries")
    

class TopicSummariesState(BaseModel):
    trancripts: List[str] = Field(description="Transcripts to be processed")
    extractions: List[str] = Field(description="Extractions of key elements from news channel transcripts.")
    topic_summary: Dict[str, str] = Field(description="Created topic summaries based on extractions")
    verification: Dict[str, str] = Field(description="Check for missing topics and other detail. ")
    translation: Dict[str, str]  = Field(description="Transaltion of verified summaries")
    step: str = Field(description="Steps taken when summerizing.")

