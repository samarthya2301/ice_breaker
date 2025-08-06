from typing import List
from langchain_core.output_parsers import PydanticOutputParser
from langchain_core.output_parsers import XMLOutputParser
from langchain_core.output_parsers import CommaSeparatedListOutputParser
from pydantic import BaseModel, Field

class Summary(BaseModel):
	summary: str = Field(description="summary")
	facts: List[str] = Field(description="interesting facts about them")

summary_parser_json = PydanticOutputParser(pydantic_object=Summary)
summary_parser_xml = XMLOutputParser(pydantic_object=Summary)
summary_parser_csv = CommaSeparatedListOutputParser(pydantic_object=Summary)