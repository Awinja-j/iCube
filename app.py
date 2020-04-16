from flask import Flask
from src.question1 import darts
from src.question2 import loot_bank
# from src.question3 import ice_fire
# from src.question4 import jo_owes


app = Flask(__name__)
app.register_blueprint(darts)
app.register_blueprint(loot_bank)
# app.register_blueprint(ice_fire, url_prefix='/ice_fire')
# app.register_blueprint(jo_owes, url_prefix='/jo_owes')


@app.route('/')
def hello():
    return "Hello World!"

if __name__ == '__main__':
    app.run()