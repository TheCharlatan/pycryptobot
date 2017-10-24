from exchanges import Kraken,Bitstamp
import requests as req
import json as json

availableTickers = []


kraken = Kraken()
bitstamp = Bitstamp()
#print(kraken.pairsByTicker)
#print(bitstamp.pairsByTicker)
print (kraken.getCurrentPrice("BTC","USD"))
print(kraken.getCurrentPrice("USD","LTC"))
print(bitstamp.getCurrentPrice("BTC","USD"))
print(bitstamp.getCurrentPrice("USD","LTC"))

