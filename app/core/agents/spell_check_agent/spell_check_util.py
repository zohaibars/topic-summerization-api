import re
import logging
from app.utils.models import UrduSpellCheck

logging.basicConfig(level="INFO")
logger = logging.getLogger(__name__)


class SpellingsOutputParser():
    def __init__(self, original: str):
        self.original = original

    def parse(self, process_str: str,) -> str:
        possible_matches = [
            r'\[Response Format START\](.*)\[Response Format END\]',
            r'Spell Check:(.*)\[Response Format END\]',
            r'Spell Check:(.*)'
        ]
        match = None
        for pattern in possible_matches:
            match = re.search(pattern, process_str, re.DOTALL)
            if match:
                break
        
        if not match:
            raise ValueError("Failed to find the response format delimiters in the text")
        content = match.group(1).strip()

        error_corrections = []
        lines = content.split('\n')
        for line in lines:
            if 'none' in line.lower():
                break
            if ',' in line:
                error, correction = map(str.strip, line.split(','))
                error_corrections.append({"error": error, "correction": correction})

        return UrduSpellCheck(
            urdu_text=self.original,
            error_corrections=error_corrections
        )