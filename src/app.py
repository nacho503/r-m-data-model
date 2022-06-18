import os
from flask import Flask,jsonify,request
from modelsFlaskSQLAl import db,User,Favorite,Episode,Character
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS

BASEDIR=os.path.abspath(os.path.dirname(__file__))
app=Flask(__name__)

#Configs
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///' + os.path.join(BASEDIR,"rickAndMorty.db") #Direccion de base de datos, test es el nombre de l abase de datos
app.config['DEBUG']=True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db.init_app(app) #conexion con base de datos
CORS(app) # no tengamos errores de cors
Migrate(app,db) #migra y crea base de datos


@app.route('/post_user',methods=['POST'])
def post_user():
    user = User()
    user.name = request.json.get("name")
    user.password = request.json.get("password")

    db.session.add(user)
    db.session.commit()

    return jsonify(user.serialize()),200

@app.route('/users',methods=['GET'])
def all_users():
    users=User.query.all()
    users=list(map(lambda user: user.serialize(),users))
    return jsonify(users.serialize()),200 

# @app.route('/characters',methods=['GET']) #recibe todos los personajes
# def get_character():
#     return jsonify(user.serialize()),200 


# @app.route('/set_favorite_char',methods=['PUT']) #PENDIENTE ingresa character a favoritos
# def set_favorite_char():
#     #todo = request.json.get("todo")
#     #todos.append(todo)
#     return jsonify(characters) 


# @app.route('/delete_favorite_char/<int:id>',methods=['DELETE']) #PENDIENTE ingresa character a favoritos
# def delete_favorite_char():
#     #len(todos)
#     #todos.pop(0)
#     return jsonify(characters) 


if __name__ == "__main__":
    app.run(host="localhost",port="5000")
