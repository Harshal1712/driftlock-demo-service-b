from pydantic import BaseModel, ConfigDict, field_validator


class Invoice(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: str
    amount_cents: int
    currency: str

    @field_validator("currency")
    @classmethod
    def upper_currency(cls, value: str) -> str:
        return value.upper()
