
/****** Executing the Stored Procedures for the Business Requirement 1 ******/
EXEC getPetAndOwners
/****** Executing the Stored Procedures for the Business Requirement 2 ******/
EXEC getPetWithinAndAboveAgeRange @Age=5
/****** Executing the Stored Procedures for the Business Requirement 3 ******/
EXEC runBillingFunction @PetID=1
/****** Executing the Stored Procedures for the Business Requirement 4 ******/
EXEC getSampleXML
/****** Executing the Stored Procedures for the Business Requirement 5 ******/
EXEC getPharmacyXMLandNonXML
/****** Executing the Stored Procedures for the Business Requirement 6 ******/
updateMedicationCost @Cost='20.5', @MedicationNumber=1
/****** Executing the Stored Procedures for the Business Requirement 7 ******/
EXEC searchPetMedication @Pet='Dog'