
from pydantic import BaseModel, Field


class StudentSchema(BaseModel):
    id: int = Field(gt=0)
    name: str = Field(min_length=1)
    age: int = Field(gt=0)
    department: str = Field(min_length=1)
    year: int = Field(gt=0)
    cgpa: float = Field(ge=0, le=10)
