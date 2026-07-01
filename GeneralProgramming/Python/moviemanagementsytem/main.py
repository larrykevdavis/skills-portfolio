#import all the class definitions from the movies module
from movies import *
""""
This section provides the testing functionality for the defined classes
"""

#movie object named 007 with all the details required for a movie
OO7=Movie('OO7',2023,'Action','01-4-2023')	
#movie list object named actions that contains 007 object in the objects collection
actions=MovieList()
actions.store(OO7)
#An actor object named JamesBond with all the details required for an actor in the class
JamesBond=Actor('James','Bond','Male','11-02-1988')
#An actor list object named all_actors that contains JamesBond object in the objects collection
all_actors=ActorList()
all_actors.store(JamesBond)
#A statement to call the movie object method to get all the detail of the movie object 007
actions.search('OO7')
#A statement to call the actor list object method to get the number of objects in its collection.
print("The actor list object has %s actor objects"%all_actors.total())
#A statement to call the actor list object method to get the details of the actor James Bond
all_actors.search('James')
#A statement to call the actor list object method to remove the details of the actor James Bond from the collection
all_actors.remove('James')
#A statement to call the actor list object method to get the number of objects in its collection.
print("The actor list object has %s actor objects"%all_actors.total())


"""
This line allows this script to be used as a module or run as an executable script
"""
