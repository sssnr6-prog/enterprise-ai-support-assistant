from fastapi import FastAPI
import json

app = FastAPI()

def load_data():
    with open("invoice_data.json", "r") as f:
        return json.load(f)    
@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/about")
def read_about():
    return {"description": "This is a simple FastAPI application for managing invoices."}

@app.get("/invoices")
def read_invoices():
    data = load_data()
    return data

@app.get("/invoices/{invoice_id}")
def read_invoice(invoice_id: str):
    data = load_data()
    invoice = next((item for item in data if item["invoice_id"] == invoice_id), None)
    if invoice:
        return invoice
    return {"error": "Invoice not found"}


        
    



