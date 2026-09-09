# List of invoice records
invoices = [
    {"invoice_id": "INV001", "customer": "ABC Corp", "amount": 1500.00, "status": "Paid"},
    {"invoice_id": "INV002", "customer": "XYZ Ltd", "amount": 2500.50, "status": "Pending"},
    {"invoice_id": "INV003", "customer": "PQR Inc", "amount": 1200.75, "status": "Paid"}
]

# Print table header
print(f"{'Invoice ID':<12} {'Customer':<15} {'Amount':>10} {'Status':<10}")
print("-" * 50)

# Print each invoice record
for invoice in invoices:
    print(
        f"{invoice['invoice_id']:<12} "
        f"{invoice['customer']:<15} "
        f"${invoice['amount']:>9.2f} "
        f"{invoice['status']:<10}"
    )