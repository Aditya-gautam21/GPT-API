from langchain_core.documents import Document
import requests
import os
from dotenv import load_dotenv

load_dotenv()

DATA_API = os.getenv("DINESPHERE_DATA_API")

def load_data():
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

        with open('orders.txt', 'a', encoding='utf-8') as f:
            content = (
                f"Customer: {customer}\n"
                f"Items: {items_str}\n"
                f"Total Amount: ₹{total}\n"
            )

            f.write(content + '\n\n')

if __name__ == '__main__':
    load_data()
    