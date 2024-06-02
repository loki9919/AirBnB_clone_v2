#!/usr/bin/python3
"""New engine DBStorage"""

from models.base_model import Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session

all_classes = {'State': State, 'City': City, 'User': User,
               'Place': Place, 'Review': Review, 'Amenity': Amenity}


class DBStorage:
    """Save in the database
    """
    __engine = None
    __session = None


    def __init__(self):
        """Creates the engine to the database.
        """
        var_eng = "{0}+{1}://{2}:{3}@{4}:3306/{5}".format(
            'mysql', 'mysqldb', getenv('HBNB_MYSQL_USER'),
            getenv('HBNB_MYSQL_PWD'), getenv('HBNB_MYSQL_HOST'),
            getenv('HBNB_MYSQL_DB'))
        self.__engine = create_engine(var_eng, pool_pre_ping=True)

        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)


    def all(self, cls=None):
        """"manage dict all cls and entities"""
        new_dict = {}
        if cls is not None:
            if cls in all_classes:
                see = self.__session.query(all_classes[cls])
            else:
                see = self.__session.query(cls)
            for instance in see:
                key = instance.__class__.__name__ + "." + instance.id
                new_dict[key] = instance
        if cls is None:
            for clas in all_classes.keys():
                see = self.__session.query(all_classes[clas])
                for instance in see:
                    key = instance.__class__.__name__ + "." + instance.id
                    new_dict[key] = instance
        return (new_dict)


    def new(self, obj):
        """Add obj to the current database session."""
        self.__session.add(obj)


    def save(self):
        """Commit all changes to the current database session."""
        self.__session.commit()


    def delete(self, obj=None):
        """Delete obj from the current database session"""
        if obj is not None:
            self.__session.delete(obj)


    def reload(self):
        """Create all tables into database and initialize a new session"""
        Base.metadata.create_all(self.__engine)
        Session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(Session)


    def close(self):
        """call remove() method on the private session attribute
        """
        self.__session.remove()
        