from pydantic import BaseModel, Field
from typing import Optional, List, Dict, Any, Union

"""
What Is Pydantic Used For?
Pydantic provides data validation and parsing using Python type hints. It's widely used in frameworks like FastAPI, but it works independently too.

"""

class Metadata(BaseModel):
    Summary: List[str] = Field(default_factory=list, description="Summary of the document")
    Title: str
    Author: str
    DateCreated: str   
    LastModifiedDate: str
    Publisher: str
    Language: str
    PageCount: Union[int, str]  # Can be "Not Available"
    SentimentTone: str
    