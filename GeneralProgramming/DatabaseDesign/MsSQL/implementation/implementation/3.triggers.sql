
USE [HermitPetClinic]
GO

SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
-- =============================================
-- Description: A trigger to Update the consultation fee based on the age of the pet
-- =============================================
CREATE TRIGGER ConsultationFeeTrigger
   ON [dbo].[Consultation]
   AFTER INSERT
AS 

BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

	DECLARE @age INT;
	DECLARE @fee INT;
	DECLARE @petid INT;
	DECLARE @consultationNumber INT;

    -- Insert statements for trigger here
    SET @petid= (SELECT PetID from inserted)
	SET @age=(SELECT age from Pet WHERE PetID=@petid)
	SET @consultationNumber=(SELECT ConsultationNumber from inserted )

	IF @age>=0 AND @age<=10
		SET @fee=10;
	ELSE IF @age>=10 AND @age<=15
	    SET @fee=15
	ELSE IF @age>=15 AND @age<=20
		SET @fee=20

	UPDATE dbo.Consultation SET Fee=@fee WHERE ConsultationNumber=@consultationNumber		
END
GO

-- =============================================
-- Description: A trigger to Update Appointments
-- =============================================
CREATE TRIGGER AppointmentTrigger
   ON [dbo].[Consultation]
   AFTER UPDATE
AS 
IF ( UPDATE (AppointmentRequired))  
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;
	DECLARE @appoint INT;
	DECLARE @petid INT;

    -- Insert statements for trigger here
	SET @appoint=(SELECT AppointmentRequired from inserted)
	SET @petid=(SELECT PetID from inserted)

	IF @appoint=1
		INSERT INTO [dbo].Appointment(petID,AppointmentFee) VALUES(@petid,5);
	ELSE
	    DELETE FROM [dbo].Appointment WHERE petID=@petid
		
END