from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem

engine = create_engine('sqlite:///restaurantmenu.db')

Base.metadata.bind = engine
DBSession =  sessionmaker(bind = engine)

session = DBSession()

myFirstRestaurant = Restaurant(name = "Pizza Palace")

session.add(myFirstRestaurant)
session.commit()

session.query(Restaurant).all()
cheesePizza = MenuItem(name = "Cheese Pizza", description = "all natural", course = "Entree",
 price = "$9.99", restaurant = myFirstRestaurant)
session.add(cheesePizza)
session.commit()
session.query(MenuItem).all()

firstResult = session.query(Restaurant).first()

firstResult.name
