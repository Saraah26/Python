import re
text = "Item code: Bx_123, AB_345 (price:$50)"

print("Digits:",re.findall(r"\d+",text))

print("Word character:",re.findall(r"\w+",text))

print("Uppercase:",re.findall(r"[A-Z]+",text))

print("Lowercase:",re.findall(r"[a-z]+",text))

print("Symbols:",re.findall(r"[^\w\s]+",text))

