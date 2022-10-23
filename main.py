from flask import (Flask, render_template, request)
import requests
from requests.models import Response


url = "https://hp-api.herokuapp.com/api/characters"
r: Response = requests.get(url)
data = r.json()

app = Flask(__name__)

_house = []
error = "404 Not Found"
for element in data:
    _house.append(element.get("house"))
houses = set(_house)
houses.remove('')
print(houses)

@app.route('/')
def main():
    return render_template('index.html', data=data, house=houses)

@app.route('/Gryffindor')
def Gryffindor():
    students = []
    for element in data:
        if "Gryffindor" in element.get("house"):
            students.append(element.get("name"))
    return render_template('Gryffindor.html', students=students)

@app.route('/Ravenclaw')
def Ravenclaw():
    students = []
    for element in data:
        if "Ravenclaw" in element.get("house"):
            students.append(element.get("name"))
    return render_template('Ravenclaw.html', students=students)


@app.route('/Slytherin')
def Slytherin():
    students = []
    for element in data:
        if "Slytherin" in element.get("house"):
            students.append(element.get("name"))
    return render_template('Slytherin.html', students=students)

@app.route('/Hufflepuff')
def Hufflepuff():
    students = []
    for element in data:
        if "Hufflepuff" in element.get("house"):
            students.append(element.get("name"))
    return render_template('Hufflepuff.html', students=students)

@app.route('/index/search')
def search_content():
    key_word = request.args.get('name')
    print(key_word)
    return render_template('search.html', data=data, key=key_word, err=error)


if __name__ == "__main__":
    app.run(debug=True, port=2341)