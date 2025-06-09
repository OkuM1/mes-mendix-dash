from pydantic import BaseModel


class Order(BaseModel):
    """Pydantic model representing a work order."""

    order_id: str
    line_id: str
    item_name: str
    quantity: int
    status: str

