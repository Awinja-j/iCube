from flask import Blueprint, request, jsonify

loot_bank = Blueprint('loot_bank', __name__, url_prefix='/loot_bank')

@loot_bank.route('/', methods=['GET'])
def loot():
    limit = 0
    loot = request.get_json()
    knapsack = loot['knapsack']
    items = loot['items'][0:]
    value =[element['value'] for element in items]
    highest_value = max(value)
    
    print(highest_value)