# Coingecko
## Requirements

Requires `python3` and `requests` library.

```sh
pip install requests
```
## Installation

### install script

Clone the repository. You need to provide proper path in your test script

### edit path in the script

Provide proper path to the file where data will be saved. You need to edit `test.py` file. In my case it is:

```python
sys.path.insert(0, '/Users/gorda/Desktop/PyProjects/ass1/src')
```


## Usage


## Examples

You need just input a number of **_top_** N cryptocurrencies which are sorted by market capitalization.

Usage examples:

```python

Enter the number of displayed cryptocurrencies (1...250) : 7

1 Bitcoin     
2 Ethereum    
3 Cardano     
4 Tether      
5 Binance Coin
6 XRP
7 Solana

```

## Test

Run unit tests with:

```
# after installing the project
run test.py
```

## License
[MIT](https://choosealicense.com/licenses/mit/)
