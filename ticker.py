import json as json
import requests as req


class Kraken:
  def __init__(self):
    self.allPairs = self.getPairs()
    self.allAssets = self.getTradedAssets()
    self.pairsByAssets = self.orderPairs()

  def getJson(url,self):
    """
    Gets the json at the url location and returns a json object
    """
    r = req.get(str(url),"GET")
    jsonResponse = json.loads(r.text)
    return jsonResponse

  def getPairs(self):
    """
    Returns traded Currency Pairs on Kraken
    """
    requestUrl = "https://api.kraken.com/0/public/AssetPairs"
    r = req.get(requestUrl)
    jsonResponse = json.loads(r.text)
    allPairs = []
    for i in jsonResponse["result"]:
      allPairs.append(i.split(".d",1)[0])
    return allPairs

  def getTradedAssets(self):
    """
    Returns traded Assets on Kraken
    """
    requestUrl = "https://api.kraken.com/0/public/Assets"
    r = req.get(requestUrl)
    jsonResponse = json.loads(r.text)
    allAssets = []
    for i in jsonResponse["result"]:
      allAssets.append(i)
    return allAssets

  def orderPairs(self):
    """
    Order Pairs by Common Ticker into a dict
    """
    pairsByAssets = {}
    for asset in self.allAssets:
      holder = []
      for pair in self.allPairs:
        if asset in pair:
          holder.append(pair)
        pairsByAssets[asset] = holder
    return pairsByAssets

  def getCurrentPrice(ticker):
    """
    Gets the current price of a traded currency pair on Kraken
    """
    uri = "https://api.kraken.com/0/public/Ticker"
    requestUrl = uri + "?pair=" + ticker
    r = req.get(requestUrl)
    jsonResponse = json.loads(r.text)
    currentPrice = jsonResponse["result"][ticker]["c"]
    print (currentPrice)


kraken = Kraken()
print(kraken.pairsByAssets)
#print (getCurrentPrice("XXBTZUSD"))

