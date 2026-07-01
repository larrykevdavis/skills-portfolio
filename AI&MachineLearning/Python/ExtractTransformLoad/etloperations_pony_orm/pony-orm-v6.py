from pony.orm import *
import xml.etree.cElementTree as ET
import csv,json

def wrangler(field):
	wrangled=""
	if field=="First Name":
		wrangled="firstName"

	elif field=="Second Name":
		wrangled="lastName"

	elif field=="Age (Years)":
		wrangled="age"

	elif field=="Sex":
		wrangled="sex"
	else:
		wrangled=field
	return wrangled

def fields_as_list():
	fields=[]

	tree = ET.ElementTree(file="user_data.xml")
	root = tree.getroot()
	xmliterator=iter(root)
	print("Iterating XML file to extract fields")
	while True:
		try:
			data = next(xmliterator) 
			for field in data.keys():
				field=wrangler(field)
				if field not in fields:
					fields.append(field)		
		except StopIteration:
			print("End of XML data iteration reached")
			print(" ")
			break

	with open("user_data.csv", mode ='r')as csver:
		reader = csv.DictReader(csver)
		csviterator=iter(reader)
		print("Iterating CSV file to extract fields")
		while True:
			try:
				data = next(csviterator) 
				for field in data.keys():
					field=wrangler(field)
					if field not in fields:
						fields.append(field)		
			except StopIteration:
				print("End of CSV data iteration reached")
				print(" ")
				break

	with open("user_data.json", mode ='r')as jsoner:
		reader = json.load(jsoner)
		jsoniterator=iter(reader)
		print("Iterating Json file to extract fields")
		while True:
			try:
				data = next(jsoniterator) 
				for field in data.keys():
					field=wrangler(field)
					if field not in fields:
						fields.append(field)		
			except StopIteration:
				print("End of Json data iteration reached")
				print(" ")
				break


	fields.append("no_category")
	return fields



def values_as_list():
	record=[]

	tree = ET.ElementTree(file="user_data.xml")
	root = tree.getroot()
	xmliterator=iter(root)
	print("Iterating XML file to extract the values")
	print(" ")
	count=1

	while True:
		try:
			print("Iterating through record:%s"%str(count))
			values=[]
			data = next(xmliterator) 
			criteria=""

			for field in data.keys():
				values.append(data.get(field).upper())

			with open("user_data.csv", mode ='r')as csver:
				reader = csv.DictReader(csver)
				csviterator=iter(reader)
				print("|>>Iterating CSV file to extract values")
				
				while True:
					try:
						check=0
						got=0
						data = next(csviterator) 

						contains=[]
						for field in data.keys():
							value=data.get(field).upper()
							if check<3:
								contains.append(value)
							else:
								break
							check+=1

						check=0
						if contains[0] in values and contains[1] in values and contains[2] in values:
							for field in data.keys():
								value=data.get(field).upper()
								if check<4:
									pass
								else:
									values.append(value)
								check+=1

					except StopIteration:
						print("|....Finished extracting values from csv file")
						break

			with open("user_data.json", mode ='r')as jsoner:
				reader = json.load(jsoner)
				jsoniterator=iter(reader)
				print("|>>Iterating JSON file to extract values")
				
				while True:
					try:
						check=0
						got=0
						data = next(jsoniterator) 

						contains=[]
						for field in data.keys():
							value=str(data.get(field)).upper()
							if check<3:
								contains.append(value)
							else:
								break
							check+=1

						check=0
						if contains[0] in values and contains[1] in values and contains[2] in values:
							for field in data.keys():
								value=str(data.get(field)).upper()
								if check<3 or check==10:
									pass
								else:
									values.append(value)
								check+=1



					except StopIteration:
						print("|....Finished extracting values from JSON file")
						print(" ")
						break
			#solve inconsistency
			debt="0"

			if len(values)==23:
				values.append(debt)
				print("..(Solving a data inconsistency)..")

			with open("user_data.txt", mode ='r')as txter:
				reader = txter.readlines()
				print("|>>Iterating txtfile to extract values")
				for line in reader:
					if values[0] in line.upper() and values[1] in line.upper():
						values.append(line)
						break
				
			if len(values)==24:
				values.append(" ")
				print("..(Solving a data inconsistency)..")

			record.append(values)
			count+=1

		except StopIteration:
			print(" ")
			print("End of XML data iteration reached")
			
			break

	return record

	
def map_to_db(fieldlist,valueslist):
	
	# print("| Mapping the data to the database using ponyORM")
	db = Database()
	att_datatype={}
	
	datalist=[]

	print("|>>Initializing the data fields with their respective datatypes")
	for field in fieldlist:
		att_datatype[field]=Optional(str,610)
	print("|....Done")
	print(" ")

	print("|>>Initializing the data mappings")
	for valuelist in valueslist:
		att_value={}
		for i in range(len(fieldlist)):
			att_value[fieldlist[i]]=valuelist[i]
		datalist.append(att_value)

	print("|....Done")
	print(" ")

	print("|>>Creating the database tables with the inialized data fields")
	detailsmapping=type('Detailsmapping', (db.Entity, ),att_datatype)
	print("|....Done")
	print(" ")

	db.bind(provider='mysql', host='', user='', passwd='', db='')
	db.generate_mapping(create_tables=True)
	
	print("|>>Inserting Data records")
	i=1
	with db_session:
		for data in datalist:
			print("|>>>Inserting record: %s"%str(i))
			detailsmapping(**data)
			i+=1
	print("|....Done")

	

map_to_db(fields_as_list(),values_as_list())