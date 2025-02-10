from typing import List, Dict, Any

from langchain.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field


class Summary(BaseModel):
    summary: str = Field(description="summary")
    facts: List[str] = Field(description="interesting facts about them")
    ice_breaker: str = Field(
        description="anIcebreaker that can be used to start a conversation with the person."
    )

    def to_dict(self) -> Dict[str, Any]:
        return {
            "summary": self.summary,
            "facts": self.facts,
            "ice_breaker": self.ice_breaker,
        }


summary_parser = PydanticOutputParser(pydantic_object=Summary)
