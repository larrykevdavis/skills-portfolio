
"""
importing the required packages
- pony - the object relation mapper to be used to transfer the records
to the database
- csv - an inbuilt python library for working with csv files
- xml - an inbuilt python library for working with xml files
- json - an inbuilt python library for working with json files
"""
from pony.orm import *
import csv,xml,json

"""
Initializing the pony Database object for creating the database mappings
"""
mapping=Database()
print("Preparing database objects")
"""
Initializing a list object named com to store all the data attributes representing
the homogenous record
"""
com=[]

"""
Initializing the file reader objects using the following procedure
- the user_data.csv file is opened in read mode
- the user_data.json file is opened in read mode
After being opened in read mode, the data is read using the following objects:
- a DictReader object reads the data from the csv file in the form of a dictionary
data structure which represents object as key value pairs
- a json.load object which reads the data from the json file as a dictionary 
- an xml parser reads the user_data.xml to extract the root of the xml tree 
of the file user_data.xml
"""
opencsv=open('user_data.csv', mode ='r')
openjson=open('user_data.json', mode ='r')
vh=csv.DictReader(opencsv)
ch=json.load(openjson)

"""
- A for loop iterates through  user_data.xml file to extract all the 
dictionary keys. These keys represent the attributes that will be used 
as the attributes when creating the database table
- Each of these attributes is added to the already initialized com list object
"""
for obj in xml.etree.ElementTree.parse('user_data.xml').getroot():
	for keys in obj.attrib.keys():
		com.append(keys)

"""
- A for loop iterates through DictReader object of the csv file to extract all the 
dictionary keys. These keys represent the attributes that will be used 
as the attributes when creating the database table
- Each of these attributes is added to the already initialized com list object
"""

for obj in vh:
	for keys in obj.keys():
		com.append(keys)

"""
- A for loop iterates through the json.load object of the json file to extract all the 
dictionary keys. These keys represent the attributes that will be used 
as the attributes when creating the database table
- Each of these attributes is added to the already initialized com list object
"""
for obj in ch:
	for keys in obj.keys():
		com.append(keys)

"""
- After the reading process of the file, the file is closed to avoid release the
memory used to store the data items during the reading process
"""
openjson.close()
opencsv.close()
print("Finished")

"""
-After all iterations and storage of the data attributes is done, the com list object contains
multiple data attributes. Among these attributes there exist attributes which are duplicated
- To eliminate these duplicates a set data structure is used by applying the set() function. 
A set data structure does not allow any duplicates to be contained in the data therefore it
eliminates any object that is repeated more that once.
- The result is then converted back to a list using the list() function
"""
allowed=list(set(com))

"""
After the removal of duplicates the sex attribute still remains in the coms list object with a similar 
name. This similar attribute was capitalized therefore it was not detected by the set() function
it is removed manually from the list using the pop() function
"""
allowed.pop(allowed.index("Sex"))
print("Creating database objects")	


"""
To generate database mappings, pony ORM works by checking for a class definition which 
inherits from the Entity class defined within pony. Once this class is found,all the attributes
defined within it alongside the data types assigned to the attributes are then automatically 
transfered into a database system as attributes to a table named using the class name
- Here a class named RELATIONAL is defined inheriting from the entity object
- When creating this class, the assumption is made that all the attributes to be mapped
to the database are known ahead of time
- In python when a class is created, it maintains a namespace dictionary known as locals. The 
definition of the RELATIONAL class takes advanteg of this and adds the attributes within the 
com list object directly to the locals dictionary with the attributes as keys and their datatypes
being the values
- Several data types are supported by pony which include string(str), integer(int),float and Json.Inorder
for these data types to be mapped in a pony object they need an identifier which is either Optional or Required
the Optional identifier means that that attribute can be null or not containing any data when mapped to the 
database, the Required identifier means that this attribute cannot be empty when mapped to the database
- Using a for loop, all the attributes are added to the locals dictionary using the attribute name as the key
and the value is assigned using the Optional keyword and the Json data type.
- When mapped to a json data type, all data regardless of whether it is of the string,integer or float data type,
is converted to a string this makes it easy for mapping data which contains a mix of multiple data types as is the
case of this homogenous record.
"""

class RELATIONAL(mapping.Entity):
	for keys in allowed:
		locals()[keys]=Optional(Json)
print("Finished")

print("Generating pony orm database mappings")
"""
The mappings are done on a mysql database hosted on the europa.ashley host
- The connection information is defined below 
"""
mapping.bind(provider='mysql', host='localhost', user='root', passwd='', db='r')
mapping.generate_mapping(create_tables=True)

"""
By the end of this step, a database table named relational should be created
on the europa.ashley host. This can be checked by opening the phpmyadmin
on the europa.ashley site.
"""
print("Mappings generated")

print("Adding details to database")

"""
In order to interact with database after mapping it using pony, a session to the database
needs to be initiated.
- This is iniated by using the statement with db_session
"""

with db_session:
	""""
	Here a for loop is used to iterate through the xml file to extract the 
	initial data attributes. The each record from the xml file will be used as the 
	base record.
	- Each record here is represented using the dictionary data structure
	"""
	for obj in xml.etree.ElementTree.parse('user_data.xml').getroot():
		"""
		Here the data is read using the same procedures explained before.
		The end goal at the end fo the loop is to combine the data from the 
		- xml file, json file and txt file to form a homogenous record using 
		the lastname and first name as the criteria for combining the data.
		- Each record from the file is represented using a dictionary data structure
		"""
		opencsv=open('user_data.csv', mode ='r')
		openjson=open('user_data.json', mode ='r')
		opentxt=open('user_data.txt', mode ='r')

		vh=csv.DictReader(opencsv)
		ch=json.load(openjson)
		th=opentxt.readlines()

		"""
		Here a for loop is used to iterate through the csv file to find records that
		match the current record of the xml base file
		- Once a match if found, the dictinary data structure of the xml base file is updated with the details
		of the matchedd record
		"""
		for vehobj in vh:
			if dict(vehobj).get('First Name').lower()==dict(obj.attrib).get('firstName').lower() and dict(vehobj).get('Second Name').lower()==dict(obj.attrib).get('lastName').lower():
				obj.attrib.update(vehobj)
				break

		"""
		Here a for loop is used to iterate through the json file to find records that
		match the current record of the xml base file
		- Once a match if found, the dictinary data structure of the xml base file is updated with the details
		of the matchedd record
		"""
		
		for ccobj in ch:
			if dict(ccobj)['lastName'].lower()==dict(obj.attrib)['lastName'].lower() and dict(ccobj)['firstName'].lower()==dict(obj.attrib)['firstName'].lower():
				obj.attrib.update(vehobj)
				break

		""""
		Here data incosistencies are removed by dropping all columns that are not in the com list which 
		was prepared to contain distinct data attributes. 
		"""
		keys=obj.attrib.keys()
		for key in keys:
			if key not in com:
				del obj.attrib[key]

		del obj.attrib["Sex"]
		"""
		Here, if statements are used to perform data update operaions as follows
		- For the record with a firstname of shane and a last name of chambers, the credit card
		security code is updated to 935
		- For the record with a firstname of joshua an a last name of lane, the salary is incremented
		by 2100
		- For the record with a firstname of suzanne and a lastname of wright, the age is updated to
		37
		- For the record with a lastname of dunn and a pension of 22358, the pension is incremented by 15%
		"""
		if obj.attrib["firstName"].lower()=="shane" and obj.attrib["lastName"].lower()=="chambers":
			obj.attrib["credit_card_security_code"]="935"

		if obj.attrib["firstName"].lower()=="joshua" and obj.attrib["lastName"].lower()=="lane":
			obj.attrib["salary"]=str(float(obj.attrib["salary"])+2100)

		if obj.attrib["firstName"].lower()=="suzanne" and obj.attrib["lastName"].lower()=="wright":
			obj.attrib["Age (Years)"]="37"

		if obj.attrib["lastName"].lower()=="dunn" and obj.attrib["pension"].lower()=="22358":
			obj.attrib["pension"]=str(float(obj.attrib["pension"])+float(obj.attrib["pension"])*0.15)
		"""
		Once all the data attributes from the different text files are processed, the combined records are entered
		into the database
		"""
		RELATIONAL(**obj.attrib)


print("Details added succesfully")


