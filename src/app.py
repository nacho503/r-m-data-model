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
    return jsonify(users),200 

@app.route('/put_user',methods=['PUT']) #PENDIENTE ingresa character a favoritos
def put_user(id):
    user=User.query.get(id)
    user.password = request.json.get("password")
    user.password = request.json.get("name")
    db.session.add(user)
    db.session.commit()
    return jsonify(user.serialize()),200 


@app.route('/delete_user/<int:id>', methods=['DELETE'])
def delete_user(id):
    user=User.query.get(id)
    db.session.delete(user)
    db.session.commit()
    return jsonify('Borrado'),200


if __name__ == "__main__":
    app.run(host="localhost",port="5000")
