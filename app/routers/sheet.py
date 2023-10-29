from fastapi_camelcase import CamelModel


class SheetItem(CamelModel):
    year: int
    month: int
    profit_or_loss: float
