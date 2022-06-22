from pydantic import BaseModel
class Order(BaseModel):
    order_id: int
    email: str
    owner: str
    phone_number: str
    created_on: str