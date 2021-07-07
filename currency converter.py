# pip install forex-python
from forex_python.converter import CurrencyRates
c = CurrencyRates()
r = c.convert("USD", "INR", 1)
print(r)

# output: 73.4139296914



