from flask import Blueprint

loot_bank = Blueprint('loot_bank', __name__, url_prefix='/loot_bank')

@loot_bank.route('/')
def loot_bank():
    print('loot_bank')