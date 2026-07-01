from pony.orm import *
import csv,json,xml

def match(dictobj1,dictobj2,key1,key2):
	matched=False

	if dictobj1[key1]==dictobj2[key1] and dictobj1[key2]==dictobj2[key2]:
		dictobj1.update(dictobj2)
		matched=True

	return [dictobj1,matched]

def fixIncosistencies(columndict):
	columns=list(columndict.keys())
	#check xml file for inconsistencies
	inconsistencies=0
	print("checking xml file for data inconsistencies")
	tree = xml.etree.ElementTree.parse("user_data.xml")
	root = tree.getroot()
	for user in root.iter("user"):
		cols=dict(user.attrib)
		collist=cols.keys()
		i=0
		while i!=len(columns):
			for col in collist:
				if columns[i] in col and columndict[columns[i]]!=col:
					inconsistencies+=1
			i+=1

	if inconsistencies>0:
		print("inconsistencies found in xml file. Fixing")
	else:
		print("No data inconsistency found in xml file")

	#check csv file for inconsistencies
	print(" ")
	inconsistencies=0
	print("checking csv file for data inconsistencies")
	file=open("user_data.csv", mode ='r')
	data = csv.DictReader(file)
	fixed=[]
	for user in data:
		cols=dict(user)
		updatedcols=dict(user)

		collist=cols.keys()
		i=0
		while i!=len(columns):
			for col in collist:
				if columns[i].lower() in col.lower() and columndict[columns[i]].lower()!=col.lower():
					print("data inconsistency found. Fixing..")
					updatedcols[columndict[columns[i]]]=updatedcols[col]
					del updatedcols[col]
					inconsistencies+=1
					print(" ")
			i+=1
		fixed.append(updatedcols)

	if inconsistencies>0:
		print("Replacing data file after fixing inconsistencies")
		header = fixed[0].keys()

		file=open("user_data.csv", "w",newline="")
		csvwriter = csv.DictWriter(file,header)
		csvwriter.writeheader()
		csvwriter.writerows(fixed)

		print("Replacement complete")
	else:
		print("No data inconsistencies found in csv file")
	file.close()

	#check json file for inconsistencies
	print(" ")
	inconsistencies=0
	print("checking json file for data inconsistencies")
	file=open("user_data.json", mode ='r')
	data = json.load(file)
	fixed=[]
	for user in data:
		cols=dict(user)
		updatedcols=dict(user)

		collist=cols.keys()
		i=0
		while i!=len(columns):
			for col in collist:
				if columns[i].lower() in col.lower() and columndict[columns[i]].lower()!=col.lower():
					print("data inconsistency found. Fixing..")
					updatedcols[columndict[columns[i]]]=updatedcols[col]
					del updatedcols[col]
					inconsistencies+=1
					print(" ")

			i+=1
		fixed.append(updatedcols)

	if inconsistencies>0:
		print("inconsistencies found in json file.")
	else:
		print("No data inconsistency found in json file")
	file.close()

	joined=join()
	ponyDB(joined)



def join():
	joined=[]

	print("Finding matching records to join from file")
	print(" ")
	print("Using XML file as the starting file ")
	tree = xml.etree.ElementTree.parse("user_data.xml")
	root = tree.getroot()
	for user in root.iter("user"):
		matched={}

		cols=dict(user.attrib)
		print("Finding match in csv file")
		file=open("user_data.csv", mode ='r')
		data = csv.DictReader(file)
		for user in data:
			cols_csv=dict(user)
			findmatch=match(cols,cols_csv,"firstName","lastName")
			if findmatch[1]==True:
				print("Match has been found and added to starting file")
				matched=findmatch[0]
				break
		file.close()
		print("Finding match in json file")
		file=open("user_data.json", mode ='r')
		data = json.load(file)
		for user in data:
			cols_json=dict(user)
			findmatch=match(matched,cols_json,"firstName","lastName")
			if findmatch[1]==True:
				print("Match has been found and added to starting file")
				matched=findmatch[0]
				break
		file.close()
		del matched['Sex']
		print(" ")
		print("Finished matching records")
		joined.append(matched)

	return joined
	

def ponyDB(joined):
	fields=[]

	db = Database()

	print("Preparing data attributes")
	for fieldnamedict in joined:
		field=list(fieldnamedict.keys())
		i=0
		while i!=len(field):
			if field[i] not in fields:
				fields.append(field[i])
			i+=1
	print(fields)

	print("Creating tables on the database")
	print("Adding method to check for duplicate records")
	class Data(db.Entity):
		firstName=Required(str)
		lastName=Required(str)
		age=Required(int)
		sex=Required(str)
		retired=Required(bool)
		dependants=Optional(str)
		marital_status=Required(str)
		salary=Required(int)
		pension=Required(int)
		company=Required(str)
		commute_distance=Required(float)
		address_postcode=Required(str)

		vehicle_Make=Required(str)
		vehicle_Model=Required(str)
		vehicle_Year=Required(int)
		vehicle_Type=Required(str)

		iban=Required(str)
		credit_card_number=Required(int,size=64)
		credit_card_security_code=Required(int)
		credit_card_start_date=Required(str)
		credit_card_end_date=Required(str)
		address_main=Required(str)
		address_city=Required(str)
		debt=Optional(Json)

	
		@property
		def get_name(self):
			return self.firstName + ' ' + self.lastName

	db.bind(provider='mysql', host='', user='', passwd='', db='')
	db.generate_mapping(create_tables=True)

	with db_session:
		print("Adding data to database")
		check=select(d.get_name for d in Data)[:]
		for fieldnamedict in joined:
			fullname=fieldnamedict["firstName"]+' '+fieldnamedict["lastName"]
			print("Checking if the record exists in the database")
			print(" ")
			if fullname in check:
				print("Record already exists.Skipping")
				print(" ")
			else:
				Data(**fieldnamedict)
				print("Record inserted into the database successfully")
			

columndict={'First':'firstName','Second':'lastName','Age':'age','Sex':'sex','make': 'vehicle_Make','model':'vehicle_Model','year':'vehicle_Year','type':'vehicle_Type'}
fixIncosistencies(columndict)

