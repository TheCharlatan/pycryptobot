from kraken import Kraken
import requests as req
import json as json

kraken = Kraken()
print(kraken.pairsByAssets)
print (kraken.getCurrentPrice("XXBTZUSD"))

