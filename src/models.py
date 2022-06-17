
# import os
# import sys
# from sqlalchemy import Column, ForeignKey, Integer, String
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import relationship
# from sqlalchemy import create_engine
# from eralchemy import render_er

# Base = declarative_base()


# class User(Base):
#     __tablename__='user' #Orlando no lo usa porque genera errores
#     id = Column(Integer, primary_key=True) #relacion uno a muchos con user_id
#     name = Column(String(250))
#     password = Column(String(250))
#     favorites=relationship('Favorite')
    

# class Favorite(Base):
#     __tablename__='favorite'
#     id = Column(Integer, primary_key=True)
#     user_id = Column(Integer, ForeignKey('user.id')) 
#     episode = Column(String(250), ForeignKey('episode.name'))
#     character = Column(String(250), ForeignKey('character.name'))

# class Episode(Base):
#     __tablename__='episode'
#     id = Column(Integer, primary_key=True)
#     episode = Column(String(250))
#     name = Column(String(250))
#     character = Column(String(250))
#     air_date=Column(String(250)) 
#     favorite = relationship('Favorite', back_populates='episode') 

# class Character(Base):
#     __tablename__='character'
#     id = Column(Integer, primary_key=True)
#     name = Column(String(250))
#     status = Column(String(250))
#     episode = Column(String(250))
#     gender=Column(String(250))  
#     species=Column(String(250))  
#     location=Column(String(250))
#     favorite = relationship('Favorite', back_populates='character')    

#     def to_dict(self):
#         return {}

# ## Draw from SQLAlchemy base
# try:
#     result = render_er(Base, 'diagram.png')
#     print('Success! Check the diagram.png file')
# except Exception as e:
#     print('There was a problem genering the diagram')
#     raise e