from pony.orm import *
import csv,xml,json


single=[]

def auto_orm(elements,elements_data,extension):
	extension=extension.capitalize()
	db_object=Database()
	classname=""
	classname=type(extension, (db_object.Entity, ),elements)
	db_object.bind(provider='mysql', host='localhost', user='root', passwd='', db='r')
	db_object.generate_mapping(create_tables=True)
	with db_session:
		for data in elements_data:
			classname(**data)


def auto_combine(single):
	single_orm={}
	db_object=Database()
	db_object.bind(provider='mysql', host='localhost', user='root', passwd='', db='r')
	params=""
	for i in range(len(single)):
		single_orm[single[i]]=Optional(str)
		if single[i]=='firstName':
			single[i]='xml.firstName'
		if single[i]=='lastName':
			single[i]='xml.lastName'
		if single[i]=='age':
			single[i]='xml.age'
		if single[i]=='sex':
			single[i]='xml.sex'
		if single[i]=='address_postcode':
			single[i]='xml.address_postcode'

	for i in range(len(single)):
		if i!=len(single)-1:
			params+=single[i]+","
		else:
			params+=single[i]
	
	with db_session:
		query=params+" from xml left join csv on xml.firstname=csv.firstname and xml.lastname=csv.lastname left join json on json.firstname=xml.firstname and json.lastname=xml.lastname"
		resultset=db_object.select(query)
		for i in range(len(single)):
			if single[i]=='xml.firstName':
				single[i]='firstName'
			if single[i]=='xml.lastName':
				single[i]='lastName'
			if single[i]=='xml.age':
				single[i]='age'
			if single[i]=='xml.sex':
				single[i]='sex'
			if single[i]=='xml.address_postcode':
				single[i]='address_postcode'
		records=[]
		for tupleresult in resultset:
			record={}
			for i in range(len(tupleresult)):
				record[single[i]]=tupleresult[i]
			records.append(record)

	auto_orm(single_orm,records,'single')
			
def reader(filename,extension,single):
	filename=filename+"."+extension
	if extension=='xml':
		elements={}
		elements_data=[]
		tree = xml.etree.ElementTree.parse(filename)
		for desc in tree.getroot():
			elem=dict(desc.attrib)
			elements_data.append(elem)
			for key in elem.keys():
				if key not in elements.keys():
					if key not in single:
						single.append(key)
					orm={}
					orm[key]=Optional(str,300)
					elements.update(orm)
		auto_orm(elements,elements_data,extension)

	if extension=='json':
		elements={}
		elements_data=[]
		file=open(filename, mode ='r')
		data=json.load(file)
		for desc in data:
			for i in desc:
				desc[i]=str(desc[i])
		for desc in data:
			elem=dict(desc)
			elements_data.append(elem)
			for key in elem.keys():
				if key not in elements.keys():
					if key not in single:
						single.append(key)
					orm={}
					orm[key]=Optional(str,300)
					elements.update(orm)
		file.close()
		auto_orm(elements,elements_data,extension)

	if extension=='csv':
		elements={}
		elements_data=[]
		file=open(filename, mode ='r')
		data = csv.DictReader(file)

		for desc in data:
			elem=dict(desc)
			elem['firstName']=elem['First Name']
			del elem['First Name']

			elem['lastName']=elem['Second Name']
			del elem['Second Name']

			elem['age']=elem['Age (Years)']
			del elem['Age (Years)']

			elem['sex']=elem['Sex']
			del elem['Sex']

			elem['vehiclemake']=elem['Vehicle Make']
			del elem['Vehicle Make']

			elem['vehiclemodel']=elem['Vehicle Model']
			del elem['Vehicle Model']

			elem['vehicleyear']=elem['Vehicle Year']
			del elem['Vehicle Year']

			elem['vehicletype']=elem['Vehicle Type']
			del elem['Vehicle Type']

			elements_data.append(elem)
			for key in elem.keys():
				if key not in elements.keys():
					if key not in single:
						single.append(key)
					orm={}
					orm[key]=Optional(str,300)
					elements.update(orm)
		auto_orm(elements,elements_data,extension)

	if extension=='txt':
		elements={}
		elements_data=[]
		file=open(filename, mode ='r')
		data = file.readlines()
		for desc in data:
			elem={}
			elem['info']=desc
			elements_data.append(elem)
			orm={}
			orm['info']=Optional(str,400)
			elements.update(orm)
		auto_orm(elements,elements_data,extension)

reader('user_data','xml',single)
reader('user_data','json',single)
reader('user_data','csv',single)
reader('user_data','txt',single)
auto_combine(single)
