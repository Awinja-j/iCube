import requests   
import json
from flask import Blueprint, request, jsonify, render_template

ice_fire = Blueprint('ice_fire', __name__, url_prefix='/ice_fire')

base_url = 'https://www.anapioficeandfire.com/api'

@ice_fire.route('/')
def icefire():
    return render_template('index.html')

@ice_fire.route('/characters')
def characters():
    response = requests.get(base_url + '/characters')
    res = response.json()
    url = [character['url'] for character in res]
    return render_template('table.html', url=url)
    

@ice_fire.route('/books')
def books():
    response = requests.get(base_url + '/books')
    res = response.json()
    url = [book['url'] for book in res]
    return render_template('table.html', url=url)


@ice_fire.route('/houses')
def houses():
    response = requests.get(base_url + '/houses')
    res = response.json()
    url = [house['url'] for house in res]
    return render_template('table.html', url=url)