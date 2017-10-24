import json as json
import requests as req

class Kraken:
  def __init__(self):
    self.allPairs = self.getPairs()
    self.allAssets = self.getTradedAssets()
    self.pairsByAssets = self.orderPairs()
    self.translateList = self.mapTicker()

  def getJson(self,url):
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
    jsonResponse = self.getJson("https://api.kraken.com/0/public/AssetPairs")
    allPairs = []
    for i in jsonResponse["result"]:
      allPairs.append(i.split(".d",1)[0])
    return allPairs

  def getTradedAssets(self):
    """
    Returns traded Assets on Kraken
    """
    jsonResponse = self.getJson("https://api.kraken.com/0/public/Assets")
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

  def mapTicker(self):
    """
    Map general ticker names to Kraken generic names
    """
    translatedTicker={}
    for name in self.allAssets:
      print(name, name[1:])
      if name[0]=="X" or name[0]=="Z":
         translatedTicker[name] = name[1:]
      else:
        translatedTicker[name] = name
    print(translatedTicker)      

  def getCurrentPrice(self,ticker):
    """
    Gets the current price of a traded currency pair on Kraken
    """
    uri = "https://api.kraken.com/0/public/Ticker"
    requestUrl = uri + "?pair=" + ticker
    jsonResponse = self.getJson(requestUrl)
    currentPrice = jsonResponse["result"][ticker]["c"]
    return currentPrice


class Bitstamp:
  currencyPairs = ["btcusd", "btceur", "eurusd", "xrpusd", "xrpeur", "xrpbtc", "ltcusd", "ltceur", "ltcbtc", "ethusd", "etheur", "ethbtc"]

  def getJson(self,url):
    """
    Gets the json at the url location and returns a json object
    """
    r = req.get(str(url),"GET")
    jsonResponse = json.loads(r.text)
    return jsonResponse

  def getCurrentPrice(self,ticker):
    """
    Gets the current price of a traded currency pair on Kraken
    """
    uri = "https://www.bitstamp.net/api/v2/ticker/"
    requestUrl = uri + ticker
    jsonResponse = self.getJson(requestUrl)
    currentPrice = jsonResponse["last"]
    return currentPrice



