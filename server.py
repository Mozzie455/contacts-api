from flask import Flask, request


app = Flask(__name__)

next_id = 5

contacts =[
    {'id':'0','name': 'Shaun', 'phone':'123-234-3456'},
    {'id':'1','name': 'Bob', 'phone':'234-234-3456'},
    {'id':'2','name': 'Sue', 'phone':'345-234-3456'},
    {'id':'3','name': 'Betty', 'phone':'567-234-3456'},
]

# GET - method
@app.route('/hello')
def hello_route():
    print(f"I have received a request on the /hello endpoint")
    return f'<h1>Hello!</h1>'

@app.get('/contacts')
def list_contacts():
    return contacts

@app.get('/contacts/<id>')
def read_single_contact(id):
    for contact in contacts:
        if contact['id'] == id:
           return contact
        else:
            return f'That contact does not exist!' 

@app.post('/contacts')
def create_contacts():
    global next_id
    
    new_contact = {
        'id': f'{next_id}',
        'name': request.json['name'],
        'phone':request.json['phone'],
    }

    contacts.append(new_contact)

    next_id += 1

    return new_contact


if __name__ == '__main__':
    app.run(debug=True)    