from manage import db
from flask import Blueprint, request

jo_owes = Blueprint('jo_owes', __name__, url_prefix='/jo_owes')

class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(), nullable=False)

    def __init__(self, full_name):
        self.full_name = full_name

    def __repr__(self):
        return '<"User: {},{}>'.format(self.id)
    
    def serialize(self):
        return {
            'id': self.id, 
            'full_name': self.full_name,
        }

class IOU(db.Model):
    __tablename__ = 'iou'

    id = db.Column(db.Integer, primary_key=True)
    lender_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    borrower_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    amount = db.Column(db.Integer, nullable=False)

    # lender = db.relationship("User", back_populates='User', foreign_keys=[id])
    # borrower = db.relationship("User", back_populates='User', foreign_keys=[id])

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

#-------------------------------------------------------------------------------------------------------

@jo_owes.route('/users', methods=['GET'])
def list_user_information():
    try:
        users = User.query.all()
        return users
    except Exception as e:
	    return(str(e))

@jo_owes.route('/add', methods=['POST'])
def create_user():
    try:
        req = request.get_json()
        user_name = req['user_name']
        user = User(full_name = user_name)
        db.session.add(user)
        db.session.commit()
        return ('user created succesfully')
    except Exception as e:
	    return(str(e))


@jo_owes.route('/iou', methods=['POST'])
def create_iou():
    try:
        req = request.get_json()
        lender = req['lender']
        borrower = req['borrower']
        amount = req['amount']

        check_lender = User.query.filter_by(id=lender).first()
        check_borrower = User.query.filter_by(id=borrower).first()
        
        if not check_lender:
            return 'This lender does not exist'
        if not check_borrower:
            return 'This borrower does not exist'

        iou = IOU(
            lender_id = lender,
            borrower_id = borrower,
            amount = amount
        )
        db.session.add(iou)
        db.session.commit()
        return('Record saved succesfully')
    except Exception as e:
	    return(str(e))

@jo_owes.route('/delete', methods=['DELETE'])
def delete():
    try:
        req = request.get_json()
        user_id = req['user_id']
        deleted = User.query.filter_by(id=user_id).first()
        if not deleted:
            return 'This user was not found'
        else:
            db.session.delete(User.query.get(user_id))
            db.session.commit()
            return 'delete succesfull'
    except Exception as e:
	    return(str(e))
