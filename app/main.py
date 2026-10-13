from fastapi import FastAPI

from app.schemas import Invoice

app = FastAPI(title="service-b")


@app.post("/invoices")
def create_invoice(invoice: Invoice) -> dict:
    return invoice.model_dump()
