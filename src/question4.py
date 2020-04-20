from manage import db
from flask import Blueprint, request

jo_owes = Blueprint('jo_owes', __name__, url_prefix='/jo_owes')

class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(), nullable=False)
    iou = db.relationship('IOU', backref='user', lazy=True)

    def __init__(self, full_name):
        self.full_name = full_name

    def __repr__(self):
        return '<"User: {},{}>'.format(self.id)
    
    def serialize(self):
        return {
            'id': self.id, 
            'full_name': self.full_name,
        }
    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_all():
        return User.query.all()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

class IOU(db.Model):
    __tablename__ = 'iou'

    id = db.Column(db.Integer, primary_key=True)
    lender_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    borrower_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    amount = db.Column(db.Integer, nullable=False)

    lender = db.relationship("User", back_populates='User', foreign_keys=[id])
    borrower = db.relationship("User", back_populates='User', foreign_keys=[id])

    def __init__(self,lender_id, borrower_id, amount):
        self.lender_id = lender_id
        self.borrower_id = borrower_id
        self.amount = amount

    def __repr__(self):
        return '<id {}>'.format(self.id)
    
    def serialize(self):
        return {
            'id': self.id, 
            'lender': self.lender_id,
            'borrower': self.borrower_id,
            'amount':self.amount
        }
    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_all():
        return IOU.query.all()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

#-------------------------------------------------------------------------------------------------------

@jo_owes.route('/users', methods=['GET'])
def list_user_information():
    try:
        users = User.get_all()
        return users
    except Exception as e:
	    return(str(e))

@jo_owes.route('/add', methods=['POST'])
def create_user():
    try:
        req = request.get_json()
        user_name = req['user_name']
        user = User(full_name = user_name)
        User.save()
        return ({},'created succesfully').format(user)
    except Exception as e:
	    return(str(e))


@jo_owes.route('/iou', methods=['POST'])
def create_iou():
    try:
        req = request.get_json()
        lender = req['lender']
        borrower = req['borrower']
        amount = req['amount']
        iou = IOU(
            lender_id = lender,
            borrower_id = borrower,
            amount = amount
        )
        IOU.save()
        return('Record saved succesfully')
    except Exception as e:
	    return(str(e))

@jo_owes.route('/delete', methods=['DELETE'])
def delete():
    try:
        req = request.get_json()
        user_id = req['user_id']
        deleted = User(id=id)
        User.delete()
        return 'delete succesfull'
    except Exception as e:
	    return(str(e))
