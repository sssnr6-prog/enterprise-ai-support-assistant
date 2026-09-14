from fastapi import FastAPI
import json

app = FastAPI()

def load_data():
    with open("invoice_data.json", "r") as f:
        return json.load(f)
    
def save_data(data):
    with open("invoice_data.json", "w") as f:
        json.dump(data, f, indent=4)


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
    
@app.post("/invoices")
def create_invoice(invoice: dict):
    data = load_data()
    data.append(invoice)
    save_data(data)  # ← Saves updated data to file
    return {"status": "Invoice created", "invoice": invoice}


