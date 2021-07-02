from flask import Flask, render_template, redirect, request
  
app = Flask(__name__)
  
people = [
        { 
                "name": "Luiz"
        }
]

@app.route("/")
@app.route('/index')
def home_view():
        return render_template('index.html')


@app.route("/<name>")
def person_detail(name):
        person = {}
        for p in people:
                if p["name"] == name:
                        person = p
                
        return render_template('index.html', person=person)


@app.route('/task', methods=['POST'])
def add_task():
        name = request.form['content']

        return redirect(f'/{name}')




