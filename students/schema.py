from pydantic import BaseModel

class StudentUpdateSchema(BaseModel):
    first_name: str
    last_name: str
