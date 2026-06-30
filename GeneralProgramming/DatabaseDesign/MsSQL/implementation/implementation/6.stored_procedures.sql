/****** Stored Procedures for the Business Requirements ******/
/****** 1.The database should allow information about the pets and their owners to be retrieved. ******/
CREATE PROCEDURE getPetAndOwners
AS
SELECT Pet.Name,Pet.Age, Pet.Type,Pet.Breed,Pet.Weight,Pet.Color,Pet.Gender, PetOwner.Name as Owners_Name,PetOwner.TelNumber As Owners_TelNumber, PetOwner.Address AS Owners_Adress FROM Pet LEFT JOIN PetOwner ON Pet.OwnerID=PetOwner.OwnerID
GO

/****** 2.The database should allow information about the pets in consultation within a certain age range to be retrieved.******/
CREATE PROCEDURE getPetWithinAndAboveAgeRange @Age int
AS
SELECT Pet.PetID,Pet.Name,Pet.Age,Pet.Breed,Pet.Weight,Pet.Color,Pet.Gender
FROM Pet Left JOIN Consultation On Pet.PetID=Consultation.PetID 
GROUP BY Pet.PetID,Pet.Breed,Pet.Age,Pet.Name,Pet.Weight,Pet.Color,Pet.Gender
Having Pet.Age>=@Age
GO


/****** 3.Through a user defined function, the database should allow information about the total fees that an owner 
has been billed for their pet to be retrieved based on the ID of the pet.******/
CREATE FUNCTION getBilling(@PetID int)
RETURNS TABLE
AS
RETURN
(
SELECT Pet.PetID,Pet.Name as PetName,PetOwner.Name As OwnerName,(SUM(consultation.Fee)+SUM(Appointment.AppointmentFee)+SUM(Appointment.CancellationFee)) AS Total_Fees 
FROM Pet Left JOIN Consultation On Pet.PetID=Consultation.PetID LEFT JOIN Appointment ON Appointment.PetID=Pet.PetID LEFT JOIN PetOwner ON Pet.OwnerID=PetOwner.OwnerID 
WHERE Pet.PetID=@PetID
GROUP BY Pet.PetID,Pet.Name,PetOwner.Name
);
GO

CREATE PROCEDURE runBillingFunction @PetID int
AS
SELECT * FROM getBilling(@PetID)
GO


/****** 4.The database should allow custom XML data to be defined and stored for the pharmacy and the medication.******/
CREATE PROCEDURE getSampleXML
AS
Declare @pharmacyxml varchar(1000) 
Declare @medicationxml varchar(1000) 

SET @medicationxml ='
<medication>
<name>Amiodarone</name>
<pet>Dog</pet>
<cost>30.4</cost>
<currency>Euro</currency>
<dosage>8–10 mg/kg, PO, every 12–24 hr for 7–10 days, then reduce to 4–6 mg/kg/day for longterm treatment</dosage>
</medication>'

SET @pharmacyxml=
'
<pharmacy>
	<name>Klein-Hamill</name>
	<location>Aylesbury</location>
	<physicaladdress>2624 Main Place</physicaladdress>
	<telnumber>2836078</telnumber>
	<email>khamill0@cnet.com</email>
</pharmacy>'

PRINT N'The Medication XML format'
PRINT @medicationxml
PRINT N''

PRINT N'The Pharmacy XML format'
PRINT @pharmacyxml
GO

/****** 5.The database should allow both the XML and non-XML data about a pharmacy to be retrieved. ******/
CREATE PROCEDURE getPharmacyXMLandNonXML
AS
SELECT PharmacyID, 
ph.PharmacyData.query('/pharmacy/name[1]')AS Name,
ph.PharmacyData.query('/pharmacy/location[1]')AS Location,
ph.PharmacyData.query('/pharmacy/physicaladdress[1]')AS PhysicalAddress,
ph.PharmacyData.query('/pharmacy/telnumber[1]')AS TelephoneNumber,
ph.PharmacyData.query('/pharmacy/email[1]')AS Email
FROM dbo.Pharmacy ph
GO


/****** 6.The database should allow the XML data in the medication data to be modified.******/
CREATE PROCEDURE updateMedicationCost @Cost varchar(10), @MedicationNumber int
AS
UPDATE Medication
SET MedicationData.modify('replace value of (/medication/cost/text())[1] with sql:variable("@Cost")')
WHERE MedicationNumber=@MedicationNumber;
GO

/****** 7.The database should allow the medication data of a predefined pet, to be searched and retrieved.******/
CREATE PROCEDURE searchPetMedication @Pet varchar(10)
AS
SELECT md.MedicationData.query('/medication/name[1]')AS Name,md.MedicationData.query('/medication/dosage[1]')AS Dosage
FROM Medication md 
WHERE md.MedicationData.value('(/medication/pet)[1]', 'varchar(100)')=@Pet
GO













