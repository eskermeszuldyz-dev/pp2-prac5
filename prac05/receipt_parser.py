import re
import json

def clean_price(price_str):
    return float(price_str.replace(" ", "").replace(",", "."))

with open("raw.txt", "r", encoding="utf-8") as file:
    data = file.read()

# Извлечение товаров и цен
pattern = r"""
\d+\.\s*\n
(.+?)\n
[\d, ]+\s+x\s+[\d ]+,\d{2}\n
([\d ]+,\d{2})
"""
items = re.findall(pattern, data, re.VERBOSE)

products, prices = [], []
for name, total_price in items:
    products.append(name.strip())
    prices.append(clean_price(total_price))

# Итоговая сумма
total_match = re.search(r"ИТОГО:\s*\n([\d ]+,\d{2})", data)
total_from_receipt = clean_price(total_match.group(1)) if total_match else None
calculated_total = round(sum(prices), 2)

# Дата и время
datetime_match = re.search(r"Время:\s*(\d{2}\.\d{2}\.\d{4})\s*(\d{2}:\d{2}:\d{2})", data)
date = datetime_match.group(1) if datetime_match else None
time = datetime_match.group(2) if datetime_match else None

# Способ оплаты
payment_match = re.search(r"(Банковская карта|Наличные|Cash|Card)", data, re.IGNORECASE)
payment_method = payment_match.group(1) if payment_match else None

# JSON вывод
receipt_data = {
    "products": products,
    "item_count": len(products),
    "item_prices": prices,
    "calculated_total": calculated_total,
    "total_from_receipt": total_from_receipt,
    "date": date,
    "time": time,
    "payment_method": payment_method
}

print(json.dumps(receipt_data, indent=4, ensure_ascii=False))