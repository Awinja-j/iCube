import requests   
import json
from flask import Blueprint, request, jsonify, render_template

ice_fire = Blueprint('ice_fire', __name__, url_prefix='/ice_fire')

base_url = 'https://www.anapioficeandfire.com/api'

def _characters():
    response = requests.get(base_url + '/characters')
    res = response.json()
    characters = [character for character in res]
    return characters
    
def _books():
    response = requests.get(base_url + '/books')
    res = response.json()
    books = [book for book in res]
    return books

def _houses():
    response = requests.get(base_url + '/houses')
    res = response.json()
    houses = [house for house in res]
    return houses

@ice_fire.route('/')
def icefire():
    characters = _characters()
    houses = _houses()
    books = _books()
    return render_template('table.html', characters=characters, houses=houses, books=books)