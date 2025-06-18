from pydantic import BaseModel

class Products(BaseModel):
    id: int
    name: str
    quantity: int

    model_config = {
        'from_attributes': True
    }