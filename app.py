import os
from manage import app, db
from src.question4 import User, IOU

from src.question1 import darts
from src.question2 import loot_bank
from src.question3 import ice_fire
from src.question4 import jo_owes

app.register_blueprint(darts)
app.register_blueprint(loot_bank)
app.register_blueprint(ice_fire)
app.register_blueprint(jo_owes)

with app.app_context():
    from src.question4 import User, IOU
    db.init_app(app)
    db.create_all()


@app.route('/')
def hello():
    return "Hello World!"

if __name__ == '__main__':
    app.run(debug=True)