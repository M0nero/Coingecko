
import sys
sys.path.insert(0, '/Users/gorda/Desktop/PyProjects/ass1/src')

import coingecko

N = int(input("Enter the number of displayed cryptocurrencies (1...250) : "))
result = coingecko.collector(N)
for count, row in enumerate(result, start=1):
    print(count, row)
