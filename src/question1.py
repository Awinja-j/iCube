"""
A circle can be defined as the locus of all points that satisfy the equation
x2 + y2 = r2
where x,y are the coordinates of each point and r is the radius of the circle.

Solving the equation for the radius r


The equation has three variables (x, y and r). 
If we know any two, then we can find the third. 
So if we are given a point with known x and y coordinates we can rearrange the equation to solve for r:
r	=	 √	  x	2 	+	 y	2    
The negative root here has no meaning. 
Note the this only works where the circle center is at the origin (0,0), 
because then there is only one circle that will pass through the given point P. 
This finds the radius r of that circle.
"""
from math import pow, sqrt
from flask import Blueprint, request, jsonify

darts = Blueprint('darts', __name__,url_prefix='/darts')

@darts.route('/', methods=['GET'])
def darts_game():
    score = 0
    if not request:
        abort(400)
    x=request.args.get('x')
    y=request.args.get('y')
    radius = sqrt(pow(int(x),2) + pow(int(y),2))
    if radius >5 <=10:
        score = 1
    elif radius >1 <=5:
        score = 5
    elif radius >0 <= 1:
        score = 10
    else:
        score

    return jsonify({"score": score})