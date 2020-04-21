from flask import Blueprint, request, jsonify

loot_bank = Blueprint('loot_bank', __name__, url_prefix='/loot_bank')

@loot_bank.route('/', methods=['GET'])
def loot_():
    loot = {}
    _loot = request.get_json()
    knapsack = _loot['knapsack']
    items = _loot['items'][0:]

    for item in _loot['items']:
      if len(loot) == 0:
        value =[element['value'] for element in items]
        highest_value = max(value)
        for x in _loot['items']:
          if x['value'] == highest_value:
              _loot['items'].remove(x)
              loot['items']= x
              loot['knapsack']= x['weight']
              items = l['items'][0:]
      else:
        weight = [element['weight'] for element in items]
        for i in weight:
          checker = i + loot['knapsack']
          if checker > knapsack:
            for x in _loot['items']:
              if x['weight'] == i:
                _loot['items'].remove(x)
                items = _loot['items'][0:]
                return loot
          else:
            value =[element['value'] for element in items]
            highest_value = max(value)
            for x in l['items']:
              if x['value'] == highest_value:
                  _loot['items'].remove(x)
                  loot['items']=x
                  loot['knapsack'] += x['weight']
                  return loot