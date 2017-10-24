from exchanges import Kraken,Bitstamp,Bitfinex,Poloniex,Bittrex
import requests as req
import json as json

kraken = Kraken()
bitstamp = Bitstamp()
bitfinex = Bitfinex()
poloniex = Poloniex()
bittrex = Bittrex()
#print(kraken.availableTickers)
#print(kraken.pairsByTicker)
#print(bitstamp.availableTickers)
#print(bitfinex.availableTickers)
#print(poloniex.availableTickers)
#print(bittrex.availableTickers)
print (kraken.getCurrentPrice("BTC","ETH"))
print(bitstamp.getCurrentPrice("BTC","ETH"))
print(bitfinex.getCurrentPrice("BTC","ETH"))
print(poloniex.getCurrentPrice("BTC","ETH"))
print(bittrex.getCurrentPrice("BTC","ETH"))

