from flask import Flask


app = Flask(__name__)

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


if __name__ == '__main__':
    app.run(debug=True)    