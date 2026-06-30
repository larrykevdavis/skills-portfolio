
/****** 1. Inserting 5 Records to the PetOwner Table ******/
INSERT INTO dbo.PetOwner (
       [Name]
      ,[Gender]
      ,[Age]
      ,[TelNumber]
      ,[Address])
VALUES 
	('John Milei','M',45,20458536,'2 Old Shore Drive'),
	('Nance Robardey','F',30,93260323,'0626 Knutson Point'),
	('Nonie Jorden','F',20,94793614,'6531 Garrison Alley'),
	('Fredric Mead','M',56,36047938,'1662 Carey Parkwaym'),
	('Shauna Oakenfield','F',55,48285915,'594 Hooker Street')


/****** 2. Inserting 5 Records to the Pet Table ******/
INSERT INTO dbo.Pet (
       [OwnerID]
	  ,[Name]
      ,[Age]
      ,[Type]
      ,[Breed]
      ,[Weight]
	  ,[Color]
	  ,[Gender])
VALUES 
	(1,'Milano',5,'Dog','German Shepherd',9,'Brown','F'),
	(2,'Buma',15,'Dog','Bulldog',10,'Grey','F'),
	(3,'Kanalo',8,'Hamster','Syrian Hamster',15,'White','F'),
	(4,'Kormen',2,'Cat','Birman',3,'Black','M'),
	(5,'Kimora',1,'Hamster','Campbell Dwarf Hamster',12,'Black','M')


/****** 3. Inserting 5 Records to the Employee Table ******/
INSERT INTO dbo.Employee (
       [Name]
      ,[Category]
      ,[OfficeNumber]
      ,[TelNumber]
      ,[Email]
      ,[Gender])
VALUES 
	('Meryl Nyssen','Doctor',201,86118428,'mnyssen0@noaa.gov','F'),
	('Jay Oehme','Doctor',202,37352617,'joehme1@soundcloud.com','F'),
	('Germana OLeary','Nurse',203,69728389,'goleary2@discovery.com','F'),
	('Marcia Cowles','Nurse',204,19299054,'mcowles3@huffingtonpost.com','M'),
	('Cherilynn Pidwell','Receptionist',204,51841166,'cpidwell5@paypal.com','M')


/****** 4. Inserting 5 Records to the Pharmacy Table ******/
INSERT INTO dbo.Pharmacy(PharmacyData)
VALUES
(
'
<pharmacy>
	<name>Klein-Hamill</name>
	<location>Aylesbury</location>
	<physicaladdress>2624 Main Place</physicaladdress>
	<telnumber>2836078</telnumber>
	<email>khamill0@cnet.com</email>
</pharmacy>'
),
(
'
<pharmacy>
	<name>Johnston and Sons</name>
	<location>Amersham </location>
	<physicaladdress>9343 Commercial Drive</physicaladdress>
	<telnumber>50465931</telnumber>
	<email>johnst@so.uk</email>
</pharmacy>'
),
(
'
<pharmacy>
	<name>Swift-Romaguera</name>
	<location>Chalfont St. Giles </location>
	<physicaladdress>25369 Pennsylvania Drive</physicaladdress>
	<telnumber>73346968</telnumber>
	<email>swi@roma.com</email>
</pharmacy>'
),
(
'
<pharmacy>
	<name>Marks and Sons</name>
	<location>Beaconsfield </location>
	<physicaladdress>67 Shelley Circle</physicaladdress>
	<telnumber>70714092</telnumber>
	<email>mk@sons.com</email>
</pharmacy>'
),
(
'
<pharmacy>
	<name>Barrows LLC</name>
	<location>Stoke Poges</location>
	<physicaladdress>010 Fordem Point</physicaladdress>
	<telnumber>3154075</telnumber>
	<email>barrows@l.uk</email>
</pharmacy>'
)

/****** 5. Inserting 5 Records to the Medication Table ******/
INSERT INTO dbo.Medication(MedicationData)
VALUES
(
'
<medication>
<name>Amiodarone</name>
<pet>Dog</pet>
<cost>30.4</cost>
<currency>Euro</currency>
<dosage>8–10 mg/kg, PO, every 12–24 hr for 7–10 days, then reduce to 4–6 mg/kg/day for longterm treatment</dosage>
</medication>'
),
(
'
<medication>
<name>Amlodipine</name>
<pet>Dog</pet>
<cost>18.4</cost>
<currency>Euro</currency>
<dosage>0.1–0.2 mg/kg, PO, bid; or 0.2–0.4 mg/kg/day, PO</dosage>
</medication>'
),
(
'
<medication>
<name>Amlodipine</name>
<pet>Cat</pet>
<cost>120.4</cost>
<currency>Euro</currency>
<dosage>0.625–1.25 mg/cat, PO, once to twice daily</dosage>
</medication>'
),
(
'
<medication>
<name>Procainamide</name>
<pet>Hamster</pet>
<cost>50</cost>
<currency>Euro</currency>
<dosage>4–6 mg/kg, PO, every 2–4 hr (regular formulation); 10–20 mg/kg, PO, tid (sustained release); 2–25 mg/kg, slow IV bolus to effect</dosage>
</medication>'
),
(
'
<medication>
<name>Quinidine sulfate</name>
<pet>Hamster</pet>
<cost>190</cost>
<currency>Euro</currency>
<dosage> 6–20 mg/kg, IM, qid; or 6–20 mg/kg, PO, tid-qid</dosage>
</medication>'
)

/****** 6. Inserting 5 Records to the Stock Table ******/
INSERT INTO dbo.Stock (
       [PharmacyID]
      ,[MedicationNumber]
      ,[Quantity]
       )
VALUES 
	(1,1,200),
	(1,2,10),
	(2,3,150),
	(2,4,10),
	(3,5,300)


/****** 7. Inserting 5 Records to the Consultation Table - Each Insertion Fires the Consultation Fee Trigger******/
INSERT INTO dbo.Consultation (
       [PetID]
      ,[EmpNumber]
       )
VALUES (1,2)
GO

INSERT INTO dbo.Consultation (
       [PetID]
      ,[EmpNumber]
       )
VALUES (2,1)
GO

INSERT INTO dbo.Consultation (
       [PetID]
      ,[EmpNumber]
       )
VALUES (3,2)
GO

INSERT INTO dbo.Consultation (
       [PetID]
      ,[EmpNumber]
       )
VALUES (4,4)
GO

INSERT INTO dbo.Consultation (
       [PetID]
      ,[EmpNumber]
       )
VALUES (5,4)
GO

/****** 8. Inserting 5 Records to the Appointment Table
These are inserted through an AFTER UPDATE Trigger by updating the consultation table Which fires the Appointment Trigger******/
UPDATE dbo.Consultation SET Diagnosis='External Parasites', AppointmentRequired=1 WHERE ConsultationNumber=1

UPDATE dbo.Consultation SET Diagnosis='Heartworms',AppointmentRequired=1 WHERE ConsultationNumber=2

UPDATE dbo.Consultation SET Diagnosis='Pinworm Infection',AppointmentRequired=1 WHERE ConsultationNumber=3

UPDATE dbo.Consultation SET Diagnosis='Cat scratch disease',AppointmentRequired=1 WHERE ConsultationNumber=4

UPDATE dbo.Consultation SET Diagnosis='Skin abscese',AppointmentRequired=1 WHERE ConsultationNumber=5


/****** 9. Inserting 5 Records to the Prescription Table ******/
INSERT INTO dbo.Prescription (
       [ConsultationNumber]
      ,[MedicationNumber]
       )
VALUES 
	(1,1),
	(1,2),
	(2,2),
	(3,3),
	(3,4),
	(4,4),
	(5,5)
/****** 10. Inserting 5 Records to the Personnel Table ******/
INSERT INTO dbo.Personnel (
       [EmpNumber]
      ,[AppointmentID]
       )
VALUES 
	(1,1),
	(3,1),
	(4,1),
	(2,2),
	(3,2),
	(4,3),
	(1,3),
	(3,3),
	(1,4),
	(4,4),
	(3,4),
	(2,5),
	(4,5),
	(3,5)