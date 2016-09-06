from ebaysdk.finding import Connection as Finding
import json

#"REDACTED" AppID

try:
    api = Finding(config_file = 'ebay.yaml')
    response = api.execute('findItemsAdvanced', {'keywords': 'Doom'}) #works. But needed the YAML file in my Home directory. Don't know why
    
    """
        with open("ebayResults", "w") as f:   
        json.dump(response.dict(), f)
    """
    #makes a HUGE EFFING dicitonary with nested dictionaries and list. Need to be a better way 
    print (response.dict()["searchResult"]["item"]) 
  
    lowest_price = 100
    
    #print(response.dict()) #yields a CRAP ton of results
except ConnectionError as e:
    print(e)
    print(e.response.dict())
