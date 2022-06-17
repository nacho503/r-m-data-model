from flask import Flask,jsonify,request,
from modelsFlaskSQLAlchemy import db,User,Favorite,Episode,Character
from flask_sqlalchey import SQLAlchemy

app=Flask(__name__)
db.init_app(app)

@app.route('/',methods=['GET'])
def home():
    return 'Home page'

@app.route('/characters',methods=['GET']) #recibe todos los personajes
def get_character():
    return jsonify(characters) 


@app.route('/set_favorite_char',methods=['PUT']) #PENDIENTE ingresa character a favoritos
def set_favorite_char():
    #todo = request.json.get("todo")
    #todos.append(todo)
    return jsonify(characters) 


@app.route('/delete_favorite_char/<int:id>',methods=['DELETE']) #PENDIENTE ingresa character a favoritos
def delete_favorite_char():
    #len(todos)
    #todos.pop(0)
    return jsonify(characters) 


if __name__ == "__main__":
    app.run(host="localhost",port="5000")
