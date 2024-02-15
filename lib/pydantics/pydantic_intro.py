from typing import List
# Base model is the key ingredient in pydantic
# validator is something that 
from pydantic import BaseModel


class Variant(BaseModel):
    label: str
    key: str

class Product(BaseModel):
    id: int
    title: str
    description: str
    sold: bool
    variants: List[Variant]


item = Product(
    id=123,
    title="hello",
    description="Yo this is descripton",
    variants=[Variant(label="Label", key="keyadj;alkdl;fka;dkfja;ldkajf;kd;a")],
    sold=True,
)

print(item)
