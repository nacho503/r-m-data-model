from flask import Flask,jsonify,request

app=Flask(__name__)

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


if __name__ == "__main__":
    app.run(host="localhost",port="5000")
