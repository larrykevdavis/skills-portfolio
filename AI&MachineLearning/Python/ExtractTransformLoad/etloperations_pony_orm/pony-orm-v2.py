from pony.orm import *
import csv,json
from xml.dom import minidom


def unified(xmlfile,jsonfile,txtfile,csvfile):
	userattributes=['firstName','lastName','age','sex','retired',
	'dependants','marital_status','salary','pension','company'
	,'commute_distance','address_postcode']

	vehicleattributes=['First Name','Second Name','Age (Years)','Sex']

	financialattributes=['firstName','lastName','age']
	
	generalattributes=['firstName','lastName']

	unify=[]


	file = minidom.parse(xmlfile)
	users= file.getElementsByTagName('user')

	

	count=1

	for value in users:
		vehicledetails=open(csvfile, mode ='r')
		vcontents = csv.DictReader(vehicledetails)

		financialdetails=open(jsonfile, mode ='r')
		fcontents = json.load(financialdetails)

		generaldetails=open(txtfile, mode ='r')
		gcontents = generaldetails.readlines()


		firstname=""
		lastname=""

		unify_d={}
		record=[]

		finance=0
		vehicle=0
		general=0

		print("Preparing record number: %s"%str(count))
		print("..........................................")
		print("Collecting the user employment details....")
		for att in userattributes:
			unify_d[att]=value.attributes[att].value
			if att=="firstName":
				firstname=value.attributes[att].value.lower()
			if att=="lastName":
				lastname=value.attributes[att].value.lower()

		record.append(unify_d)
		print("Done.")
		print("..........................................")
		print("Collecting the vehicle details....")

		for vh in vcontents:
			vh=dict(vh)
			
			if vh["First Name"].lower()==firstname and vh["Second Name"].lower()==lastname:
				for att in vehicleattributes:
					del vh[att]
				record.append(vh)
				vehicle=1
				break
			

		if vehicle==0:
			empty={'none':'none'}
			record.append(empty)


		print("..........................................")
		print("Collecting the general details....")
		for fh in fcontents:
			fh=dict(fh)
		
			if fh["firstName"].lower()==firstname and fh["lastName"].lower()==lastname:
				for att in financialattributes:
					del fh[att]

				finance=1
				record.append(fh)
				break
					
		if finance==0:
			empty={'none':'none'}
			record.append(empty)

			
		for gh in gcontents:
			if firstname in gh.lower() and lastname in gh.lower():
				general=1
				record.append(gh)
				break

		if general==0:
			empty={'none':'none'}
			record.append(empty)
			

		unify.append(record)

		
		
		print("..........................................")
		print("Creating a Unified record....")
		print("Done")
		print("..........................................")

		count+=1

		vehicledetails.close()
		financialdetails.close()
		generaldetails.close()

		
	
	return unify


db = Database()

class Unified(db.Entity):
    id = PrimaryKey(int, auto=True)
    userdetails = Required(Json)
    vehicledetails = Required(Json)
    financedetails = Required(Json)
    generaldetails = Required(Json)


db.bind(provider='mysql', host='', user='', passwd='', db='')
db.generate_mapping(create_tables=True)

with db_session:
	unify=unified('user_data.xml','user_data.json','user_data.txt','user_data.csv')
	print("##############################")
	print("Mapping Unified records to ORM....")
	count=1
	for records in unify:
		print("Adding record:%s to database"%str(count))
		Unified(userdetails=records[0],vehicledetails=records[1],financedetails=records[2],generaldetails=records[3])
		
		print("Done.")
		print("..........................................")
		count+=1
	print("##############################")
	print("Done....")
	


