import json

with open("invoice_data.json", "r") as file:
    invoices = json.load(file)

for invoice in invoices:
    print(invoice)