from flask_sqlalchemy import SQLAlchemy

db=SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250))
    password = db.Column(db.String(250))
    # favorites=db.relationship('Favorite')

    def __repr__(self):
        return "<User %>" % self.name

    def serialize(self):
        return {
            "id":self.id,
            "name": self.name,
            "password": self.password
        }

class Favorite(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id')) 
    # episode = db.Column(db.String(250), db.ForeignKey('episode.name'))
    # character = db.Column(db.String(250), db.ForeignKey('character.name'))

    def __repr__(self):
        return "<Favorite %>" % self.name #no se cual va aqui

    def serialize(self):
        return {
            "id":self.id,
            "user_id": self.user_id,
            "episode": self.episode,
            "character": self.character
        }

class Episode(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    episode = db.Column(db.String(250))
    name = db.Column(db.String(250))
    character = db.Column(db.String(250))
    air_date=db.Column(db.String(250)) 
    # favorite = db.relationship('Favorite', backref='episode') 

    def __repr__(self):
        return "<Episode %>" % self.name #no se cual va aqui

    def serialize(self):
        return {
            "id":self.id,
            "user_id": self.user_id,
            "episode": self.episode,
            "character": self.character,
            "air_date": self.air_date
        }

class Character(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250))
    status = db.Column(db.String(250))
    episode = db.Column(db.String(250))
    gender=db.Column(db.String(250))  
    species=db.Column(db.String(250))  
    location=db.Column(db.String(250))
    # favorite = db.relationship('Favorite', backref='character')   

    def __repr__(self):
        return "<Character %>" % self.name 

    def serialize(self):
        return {
            "id":self.id,
            "name": self.name,
            "status": self.status,
            "episode": self.episode,
            "gender": self.gender,
            "species": self.species,
            "location": self.location,
        }
