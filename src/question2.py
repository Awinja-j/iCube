from flask import Blueprint, request, jsonify

loot_bank = Blueprint('loot_bank', __name__, url_prefix='/loot_bank')

@loot_bank.route('/', methods=['GET'])
def loot():
    limit = 0
    loot = request.get_json()
    knapsack = loot['knapsack']
    for x in loot['items']:
        weight = x['weight']
        value = x['value']
    return(weight, value)