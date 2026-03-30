from langchain_core.documents import Document
import requests
import os
from dotenv import load_dotenv

load_dotenv()

DATA_API = os.getenv("DINESPHERE_DATA_API")

data = requests.get(DATA_API).json()

docs = []

orders = data.get("data", {}).get("orders", [])

for order in orders:
    customer = order.get("customer_name", "Unknown")
    total = order.get("total_amount", 0)

    order_items = order.get("order", [])  # list

    items_list = []

    for entry in order_items:
        quantity = entry.get("quantity", 1)

        for item in entry.get("items", []):
            title = item.get("title", "Unknown")
            items_list.append(f"{title} x{quantity}")

    items_str = ", ".join(items_list)

    content = (
        f"Customer: {customer}\n"
        f"Items: {items_str}\n"
        f"Total Amount: ₹{total}"
    )

    docs.append(
        Document(
            page_content=content,
            metadata={
                "customer": customer,
                "total": total,
                "source": "api"
            }
        )
    )

print(docs[:2])