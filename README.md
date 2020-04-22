# iCube

### Requirements

- python 3.5/python 3.6. 
- sqlite3 database

### Installation

Clone this repo using htts or ssh, depending on your preference.

ssh:

```$ git clone git@github.com:Awinja-j/iCube.git```

http:

```$ git clone https://github.com/Awinja-j/iCube.git```

cd into the created folder and install a [virtual environment](https://virtualenv.pypa.io/en/stable/)

`$ virtualenv venv`

Activate the virtual environment

`$ source venv/bin/activate`

Install all app requirements

`$ pip install -r requirements.txt`

Create the database and run migrations

`$ python manage.py db init`

`$ python manage.py db migrate`

`$ python manage.py db upgrade`

All done! Now, start your server by running python manage.py runserver. For best experience, use a GUI platform like postman to make requests to the api.

# Endpoint

Live Endpoint: https://fierce-dusk-18712.herokuapp.com

### Question 1
Endpoint: /darts/

| Description | HTTP Method | URL   | Params | Response w/o Payload | Response w/ Payload |
|-------------|-------------|-------|----------------|----------------------|---------------------|
| Play darts  | GET         | / | ?x=0&y=10       | {"score": 0}       | {"score":1}          |

![Image description](https://github.com/Awinja-j/iCube/blob/master/images/Screenshot%202020-04-17%20at%2002.10.56.png)

### Question 2 
Endpoint: /loot_bank/

| Description | HTTP Method | URL   | Payload Format                                                                                                                                         | Response w/o Payload | Response w/ Payload                                                                         |
|-------------|-------------|-------|--------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------|---------------------------------------------------------------------------------------------|
| Loot Bank   | GET         | /| { "Knapsack:100, "items":[{ "weight": 5, "value": 10 },  { "weight": 4, "value": 40 },  { "weight": 6, "value": 30 },  { "weight": 4, "value": 50 }] } | {"knapsack":}        | {"Knapsack:100, "items":[{   { "weight": 4, "value": 40 },   { "weight": 4, "value": 50 }]} |

![Image description](https://github.com/Awinja-j/iCube/blob/master/images/Screenshot%202020-04-22%20at%2007.00.55.png)
### Question 3
Endpoint: /ice_fire/

| Description                      | HTTP Method | URL             | Payload Format | Response w/o Payload | Response w/ Payload |
|----------------------------------|-------------|-----------------|----------------|----------------------|---------------------|
| display character/books/house    | GET         | /characters     |                |                      |                     |
| view details of selected element | GET         | /character/<id> |                |                      |                     |



![Image description](https://github.com/Awinja-j/iCube/blob/master/images/Screenshot%202020-04-22%20at%2006.57.43.png)
### Question 4
Endpoint: /jo_owes/

| Description              | HTTP Method | URL    | Payload Format                        | Response w/o Payload | Response w/ Payload             |
|--------------------------|-------------|--------|---------------------------------------|----------------------|---------------------------------|
| List of User Information | GET         | /users | {"users":["Adam","Bob"]}              | {"users":}           | {"users":(sorted by name)}      |
| Create User              | POST        | /add   | {"user":}                             | N/A                  | {User object for new user}      |
| Create IOU               | POST        | /iou   | {"lender":,"borrower":,"amount":5.25} | N/A                  | {"users": and(sorted by name)>} |
| Delete User              | DELETE      | /users | {"user":{"id":3}}                     | N/A                  | {"user deleted succesfully"     |

![Image description](https://github.com/Awinja-j/iCube/blob/master/images/Screenshot%202020-04-17%20at%2002.10.56.png)

