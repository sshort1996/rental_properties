import re
price = '$1,050'
prices = re.findall(r'\d+(?:,\d+)*(?:\.\d+)?|\d+(?:\.\d+)?', price)
prices = [re.sub(r'[^\d\.]+', '', x) for x in prices]

print(prices)
# Convert prices to floats
prices = [float(price) for price in prices]

print(prices)
print( sum(prices) / len(prices))

