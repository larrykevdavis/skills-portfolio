
USE [HermitPetClinic]
GO

SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO

/****** 1. View to Retrieve all the pets and their owners ******/
CREATE VIEW petandowners AS
SELECT Pet.Name,Pet.Age, Pet.Type,Pet.Breed,Pet.Weight,Pet.Color,Pet.Gender, PetOwner.Name as Owners_Name,PetOwner.TelNumber As Owners_TelNumber, PetOwner.Address AS Owners_Adress FROM Pet LEFT JOIN PetOwner ON Pet.OwnerID=PetOwner.OwnerID
GO
/****** 2. View to A pet in Consultation and the Consulting Doctor ******/
CREATE VIEW PetOwnerAndConsultingDoctor AS
SELECT Pet.Type AS Pet_Type,Pet.age AS Pet_Age ,PetOwner.Name Owners_Name,Employee.Name AS Consulting_Doctor FROM Consultation LEFT JOIN Pet ON Consultation.PetID=Pet.PetID LEFT JOIN PetOwner on Pet.OwnerID=Pet.OwnerID LEFT JOIN Employee on consultation.EmpNumber=Employee.EmpNumber