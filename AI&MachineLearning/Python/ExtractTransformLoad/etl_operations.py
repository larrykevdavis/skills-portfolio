from pony.orm import *
import json
import csv
import xml.etree.ElementTree as ET

# a dictionary variable to store the attributes and their occurence number for each of the files
initialattributes={}
# a list to store all the unique attributes, unique to each file
uniqueattributes=[]

def update_attribute_occurence(addedkey,listofdataobjects,initialattributesdictionary):
	found=0
	for keyvalue in addedkey.split(' '):
		for key in listofdataobjects[0].keys():
			if keyvalue.lower() in key.lower():
				found=1
				break

	if found==1:
		initialattributesdictionary[addedkey]=initialattributesdictionary[addedkey]+1

def fetch_unique_attributes(listofdataobjects,uniqueattributeslist):
	for record in listofdataobjects:
		keylist=record.keys()
		for key in keylist:
			#make lowercase
			key=key.lower()
		
			found=0
			for addedkey in uniqueattributeslist:
				for keyvalue in addedkey.split(' '):
					if keyvalue in key:
						found=1
						break

				if found==1:
					break

			if found==0:
				uniqueattributeslist.append(key)

def unify_common_attribute_names(commonattributeslist,dataobject):
	updateddataobject=[]

	for record in dataobject:
		newrecord={}

		foundattribute=[]
		foundattr=[]

		for key in record.keys():
			found=""
			attr=""
				
			if key in foundattribute:
				pass
			else:
				for attribute in commonattributeslist:
					if attribute in foundattr:
						pass
					else:
						for keyvalue in attribute.split(' '):
							if keyvalue.lower() in key.lower():
								foundattribute.append(key)
								foundattr.append(attribute)
								found=key
								attr=attribute
								attr=attr.title()
								break

					if found!="":
						break

			if found!="":
				newrecord[attr]=str(record.get(key))
			else:
				newkey=key.title()
				newrecord[newkey]=str(record.get(key))

		updateddataobject.append(newrecord)

	return updateddataobject	

def fetch_unified_record(unifiedcommonattributes_jsondata,unifiedcommonattributes_xmldata,commonattributes):
	unified_records=[]
	#using the csv file as the starting point
	file=open('user_data_23_4.csv')
	csvdata = csv.DictReader(file)
	for csvrecord in csvdata:
		commonattribute_one=commonattributes[0].title()
		commonattribute_two=commonattributes[1].title()
		commonattribute_three=commonattributes[2].title()

		for jsonrecord in unifiedcommonattributes_jsondata:
			if csvrecord[commonattribute_one].lower()==jsonrecord[commonattribute_one].lower() and csvrecord[commonattribute_two].lower()==jsonrecord[commonattribute_two].lower() and int(csvrecord[commonattribute_three])==int(jsonrecord[commonattribute_three]):
				csvrecord.update(jsonrecord)

		for xmlrecord in unifiedcommonattributes_xmldata:
			if csvrecord[commonattribute_one].lower()==xmlrecord[commonattribute_one].lower() and csvrecord[commonattribute_two].lower()==xmlrecord[commonattribute_two].lower() and int(csvrecord[commonattribute_three])==int(xmlrecord[commonattribute_three]):
				csvrecord.update(xmlrecord)

		# processing of the text file records
		if csvrecord["First Name"].lower()=="valerie" and csvrecord["Second Name"].lower()=="ellis":
			csvrecord["Credit_Card_Security_Code"]=str(762)

		if csvrecord["First Name"].lower()=="charlie" and csvrecord["Second Name"].lower()=="west" and csvrecord["Company"].lower()=="williams-wheeler":
			newsalary=int(csvrecord["Salary"])+2100
			csvrecord["Salary"]=str(newsalary)

		if csvrecord["First Name"].lower()=="charlie" and csvrecord["Second Name"].lower()=="short":
			csvrecord["Age (Years)"]=str(52)

		if csvrecord["Second Name"].lower()=="martin" and int(csvrecord["Pension"])==22896:
			newpension=((22896*0.15)/100)+22896
			csvrecord["Pension"]=str(newpension)


		unified_records.append(csvrecord)
		
	file.close()
	return unified_records


def push_unified_record_to_db(uniqueattributes,unified_records):
	#fix the commonattributes in uniqueattributes
	for attribute in uniqueattributes:
		index=uniqueattributes.index(attribute)
		uniqueattributes.remove(attribute)
		uniqueattributes.insert(index,attribute.title())

	#generate an attribute dictionary
	attributedict={}
	for attribute in uniqueattributes:
		attributedict[attribute]=Optional(str)


	db = Database()

	Orchid_customers=type('Orchid_customers', (db.Entity,),attributedict)
	db.bind(provider='mysql', host='127.0.0.1', user='testuser', passwd='testuser', db='testuser')
	db.generate_mapping(create_tables=True)

	with db_session:
		for record in unified_records:
			Orchid_customers(**record)
			

#1. read the data files and store them in a variable
# 1.1 - Read the CSV file as the starting point
file=open('user_data_23_4.csv')
csvdata = csv.DictReader(file)

# for each of the record in the csv file
for csvrecord in csvdata:
	# get the list of attributes
	keylist=csvrecord.keys()
	# iterate the list of attributes 
	for key in keylist:
		#make lowercase
		key=key.lower()
		# assign each attribute a number 0 and store it in the dictionary
		initialattributes[key]=0
		# update the unique attributes with any of the attribute which does not currently exist in it
		if key not in uniqueattributes:
			uniqueattributes.append(key)
# close the csv file
file.close()



#1.2  Read the JSON file
file= open('user_data_23_4.json')
jsondata=json.load(file)
file.close()

xmldatatree=ET.parse('user_data_23_4.xml')
xmldataroot = xmldatatree.getroot()


for addedkey in initialattributes.keys():
	#update attribute occurence from json file
	update_attribute_occurence(addedkey,jsondata,initialattributes)
	#update attribute occurence from xml file
	update_attribute_occurence(addedkey,xmldataroot,initialattributes)

#update the unique records from json file
fetch_unique_attributes(jsondata,uniqueattributes)
#update the unique records from xml file
fetch_unique_attributes(xmldataroot,uniqueattributes)
# isolate all the common attributes repeated in all the files
commonattributes=[]

for attribute in initialattributes.keys():
	if initialattributes[attribute]==2:
		commonattributes.append(attribute)

# fetch_unified_record(commonattributes,uniqueattributes)
#unify json data common attributes
unifiedcommonattributes_jsondata=unify_common_attribute_names(commonattributes,jsondata)
#unify xml data common attributes
unifiedcommonattributes_xmldata=unify_common_attribute_names(commonattributes,xmldataroot)
# print(unifiedcommonattributes_xmldata)
unified_records=fetch_unified_record(unifiedcommonattributes_jsondata,unifiedcommonattributes_xmldata,commonattributes)
#push to the database
push_unified_record_to_db(uniqueattributes,unified_records)
