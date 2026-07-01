"""
Import the random module to generate a random ID for the Movie class
"""
import random
"""
Definition of the movie class
"""

class Movie:
	"""
	The movie class has a constructor which receives the title, year,genre and releasedate attributes as parameters
	- The constructor initializes and stores the parameters in the class instance
	- It has getter methods for getting the attributes respectively named
		-getId
		-getGenre
		-getYear
		-getReleasedate

	- It has setter methods for setting the attributes
		-setId
		-setGenre
		-setYear
		-setReleasedate


	"""

	def __init__(self,title,year,genre,releasedate):
		self.id=random.randint(0,1000)
		self.title=title
		self.year=year
		self.genre=genre
		self.releasedate=releasedate

	def setTitle(self,genre):
		self.genre=genre

	def setGenre(self,genre):
		self.genre=genre

	def setYear(self,year):
		self.year=year

	def setReleaseDate(self,releasedate):
		self.releasedate=releasedate

	def getId(self):
		return self.id

	def getTitle(self):
		return self.title

	def getGenre(self):
		return self.genre

	def getYear(self):
		return self.year

	def getReleaseDate(self):
		return self.releasedate


"""
Definition of the MovieList class
"""
class MovieList:
	"""
	The MovieList class has a an empty constructor with no attrbiutes
	- It has a list to store movie objects
	- It has the store method which receives an object of the Movies
		- This method then creates a dictionary with attributes derived
		using the getter methods of the Movie object
		- The dictionary is then attached to the list store

	- It has the search method which receives as a parameter the title of the movie
		- It then iterates through the list object check if the dictionary has the title
		in its title key
		- If the movie is found, its details are printed to the user. If not a message
		is printed to the user


	- It has the remove method which receives as a parameter the title of the movie
		- it iterates through the list store and checks if the title is present as a dictionary key
		- If the movie is present, it is removed from the list if it is not, a  message is 
		returned to the user

	- It has a total method which returns the total number of items in the list storing the movie
	objects


	"""
	
	def __init__(self):
		self.moviestore=[]

	def store(self,movieobj):
		dictionary={}
		dictionary["id"]=movieobj.getId()
		dictionary["title"]=movieobj.getTitle()
		dictionary["genre"]=movieobj.getGenre()
		dictionary["year"]=movieobj.getYear()
		dictionary["releasedate"]=movieobj.getReleaseDate()
		self.moviestore.append(dictionary)

	def search(self,title):
		movie={}
		found=0
		for moviedict in self.moviestore:
			if moviedict["title"]==title:
				found=1
				movie=moviedict
				break

		if found==1:
			print("Found the following movie")
			print("Title:%s"%movie["title"])
			print("Genre:%s"%movie["genre"])
			print("Year:%s"%movie["year"])
			print("Release Date:%s"%movie["releasedate"])
		else:
			print("Movie with the title:%s not found"%title)
	
		return movie

	def remove(self,title):
		found=0
		for moviedict in self.moviestore:
			if moviedict["title"]==title:
				found=1
				index=self.moviestore.index(moviedict)
				self.moviestore.pop(index)
				break


	def total(self):
		return len(self.moviestore)


"""
Definition of the Actor Class
"""
class Actor:
	"""
	The Actor has a constructor that takes in as parameters the firstname,surname,gender and 
	date of birth
	- The constructor initializes and stores the parameters in the class instance
	- It has getter methods for getting the parameters respectively named
		-getFirstName
		-getSurname
		-getGender
		-getDob

	- It has setter methods for setting the parameters named
		-setFirstName
		-setSurname
		-setGender
		-setDob
	"""
	def __init__(self,firstname,surname,gender,dob):
		self.firstname=firstname
		self.surname=surname
		self.gender=gender
		self.dob=dob

	def setFirstName(self,firstname):
		self.firstname=firstname

	def setSurname(self,surname):
		self.surname=surname

	def setGender(self,gender):
		self.gender=gender

	def setDob(self,dob):
		self.dob=dob

	def getFirstName(self):
		return self.firstname

	def getSurname(self):
		return self.surname

	def getGender(self):
		return self.gender

	def getDob(self):
		return self.dob



"""
Definition of the ActorList class
"""
class ActorList:
	"""
	The ActorList class has a an empty constructor with no attrbiutes
	- It has a list to store Actor objects
	- It has the store method which receives an object of the Actor class
		- This method then creates a dictionary with attributes derived
		using the getter methods of the Actor object
		- The dictionary is then attached to the list store

	- It has the search method which receives as a parameter the firstname of the actor
		- It then iterates through the list object check if the dictionary has the firstname
		in its firstname key
		- If the actor is found, their details are printed to the user. If not a message
		is printed to the user

	- It has the remove method which receives as a parameter the firstname of the actor
		- it iterates through the list store and checks if the title is present as a dictionary key
		- If an actor is found,the method checks if there is any other actor with the same firstname
		- If only one actor is found, they are removed from the list
		- If more than one actor is found, a list of options with the firstname and lastname is shown
		to the user
		- The user is then prompted to select an actor to remove
		- Once the user is selected, they are removed from the list

	- It has a total method which returns the total number of items in the list storing the movie
	objects


	"""
	def __init__(self):
		self.actorstore=[]

	def store(self,actorobj):
		dictionary={}
		dictionary["firstname"]=actorobj.getFirstName()
		dictionary["surname"]=actorobj.getSurname()
		dictionary["gender"]=actorobj.getGender()
		dictionary["dob"]=actorobj.getDob()
		self.actorstore.append(dictionary)


	def remove(self,firstname):
		found=[]
		for actordict in self.actorstore:
			if actordict["firstname"]==firstname:
				found.append(actordict)
		if len(found)==1:
			print("Actor with the firstname:%s has been deleted"%firstname)
			index=self.actorstore.index(found[0])
			self.actorstore.pop(index)
		elif len(found)==0:
			print("No actor with that firsname has been found")
		elif len(found)>1:
			for i in range(len(found)):
				print("Found the following actors:")
				print("%s.FirstName:%s Surname:%s"%(i+1,actordict["firstname"],actordict["surname"]))

			sel=input("Enter the option number of the actor to delete")
			for i in range(len(found)):
				if i+1==sel:
					print("Actor with the firstname:%s and surname:%shas been deleted"%(actordict["firstname"],actordict["surname"]))
					index=self.actorstore.index(found[i])
					self.actorstore.pop(index)


	def total(self):
		return len(self.actorstore)

	def search(self,firstname):
		for actordict in self.actorstore:
			if actordict["firstname"]==firstname:
				print("Found the following actor:")
				print("############################")
				print("First Name:%s"%actordict["firstname"])
				print("SurName:%s"%actordict["surname"])
				print("Gender:%s"%actordict["gender"])
				print("Date of Birth:%s"%actordict["dob"])
				print("############################")



"""
This line allows this script to be used as a module or run as an executable
"""
if __name__ == '__main__':
	main()


