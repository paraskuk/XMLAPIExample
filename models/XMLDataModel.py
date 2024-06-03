from pydantic import BaseModel


class XMLDataModel(BaseModel):
    data: str
