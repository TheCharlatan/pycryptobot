from exchanges import Kraken,Bitstamp
import requests as req
import json as json

kraken = Kraken()
bitstamp = Bitstamp()
print(kraken.pairsByAssets)
print (kraken.getCurrentPrice("XXBTZUSD"))
print(bitstamp.getCurrentPrice("btcusd"))

