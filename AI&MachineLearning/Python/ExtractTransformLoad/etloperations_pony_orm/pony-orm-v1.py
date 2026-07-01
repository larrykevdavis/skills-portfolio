from pony.orm import *
import csv,json,xml


def preprocessor(header):
	for i in range(len(header)):
		if header[i]=="Sex":
			header[i]="sex"

		if header[i]=="Age (Years)":
			header[i]="age"

		if header[i]=="First Name":
			header[i]="firstName"

		if header[i]=="Second Name":
			header[i]="lastName"

	return header

def get_xml_root(xmlfile):
	tree = xml.etree.ElementTree.parse(xmlfile)
	root = tree.getroot()
	return root


def get_json(jsonfile):
	row=[]
	with open(jsonfile, mode ='r')as jdata:
		data = json.load(jdata)
		for i in data:
			row.append(i)
	return row

def get_txt(txtfile):
	row=[]
	txt=open(txtfile, mode ='r')
	lines = txt.readlines()
	for line in lines:
		row.append(line)
	return row
		
def write_csv(header,rows,title):
	fwrite=open(title,mode='w',newline='')
	writer = csv.writer(fwrite) 
	writer.writerow(header)
	writer.writerows(rows)
	fwrite.close()

def read_csv(csvfile):
	rows=[]
	fopen=open(csvfile, mode ='r')
	fopen_read=csv.reader(fopen)
	for row in fopen_read:
		rows.append(row)
	fopen.close()
	return rows

def main():
	homogenous_rows=[]

	rows=read_csv('user_data.csv')
	rows_no_header=[]

	header=rows[0]
	header=preprocessor(header)

	for i in range(len(rows)):
		if i!=0:
			rows_no_header.append(rows[i])

	write_csv(header,rows_no_header,"preprocessed.csv")

	print("Getting Base data from CSV.")
	rows=read_csv('preprocessed.csv')
	header=rows[0]
	
	indexes=[]
	jsonindexes=[]

	root=get_xml_root("user_data.xml")
	jdata=get_json("user_data.json")
	txtdata=get_txt("user_data.txt")

	keys=[]
	for child in root:
		keys=child.keys()
		break

	for i in range(len(keys)):
		if keys[i] in header:
			indexes.append(i)
		else:
			header.append(keys[i])
	keys=[]
	for child in jdata:	
		for key in list(child.keys()):
			if key in keys:
				pass
			else:
				keys.append(key)

	for i in range(len(keys)):
		if keys[i] in header:
			jsonindexes.append(i)
		else:
			header.append(keys[i])

	for i in range(len(rows)):
		if i!=0:
			print("Creating a homogenous record with XML data")
			for child in root:
				keys=child.keys()

				if dict(child.attrib)[keys[0]].lower()==rows[i][0].lower() and dict(child.attrib)[keys[1]].lower()==rows[i][1].lower():

					for j in range(len(keys)):
						if j in indexes:
							pass
						else:
							rows[i].append(str(dict(child.attrib)[keys[j]]))
					break
			print("Homogenous record creation complete")

			print("Creating a homogenous record with JSON data")
			for child in jdata:
				keys=list(child.keys())
				if dict(child)[keys[0]].lower()==rows[i][0].lower() and dict(child)[keys[1]].lower()==rows[i][1].lower():
					for j in range(len(keys)):
						if j in jsonindexes:
							pass
						else:
							rows[i].append(str(dict(child)[keys[j]]))
					rows[i].append(" ")
					break
			print("Homogenous record creation complete")

			print("Creating a homogenous record with TXT data")
			for child in txtdata:
				if rows[i][0].lower() in child.lower() and rows[i][1].lower() in child.lower():
					rows[i].append(child)
					break
			print("Homogenous record creation complete")

			homogenous_rows.append(rows[i])
			
	header.append("departmental_messages")
	#write to csv
	print("Writing the homogenous records to a csv file")
	write_csv(header,homogenous_rows,"homogenous.csv")
	print(" ")
	print("Reading the homogenous records from csv file")
	read_csv_to_pony()


def read_csv_to_pony():
	rows=read_csv('homogenous.csv')
	header=rows[0]
	print("Creating database tables")
	db = Database()
	class Homogenous_records(db.Entity):
		for headervalue in header:
			locals()[headervalue] = Optional(str,600)
	db.bind(provider='mysql', host='', user='', passwd='', db='')
	db.generate_mapping(create_tables=True)
	print("Database table creation complete")
	print(" ")
	print("Inserting data into the database")
	print(" ")
	with db_session:
		for i in range(len(rows)):
			print("Beginning insertion of record>%s"%str(i))
			homogenous={}
			if i==0:
				pass
			else:
				for j in range(len(rows[i])):
					homogenous[header[j]]=rows[i][j]
				
				Homogenous_records(**homogenous)
			print("Finished insertion of record>")
			print(" ")

main()


