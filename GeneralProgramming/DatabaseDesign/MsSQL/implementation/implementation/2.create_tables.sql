USE [HermitPetClinic]
GO


SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

/****** 1. Object:  Table [dbo].[PetOwner]  ******/
CREATE TABLE [dbo].[PetOwner](
	[OwnerID] [int] IDENTITY(1,1) NOT NULL,
	[Name] [varchar](50) NULL,
	[Gender] [char](10) NULL,
	[Age] [int] NULL,
	[TelNumber] [int] NULL,
	[Address] [varchar](50) NULL,
 CONSTRAINT [PK_PetOwner] PRIMARY KEY CLUSTERED 
(
	[OwnerID] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO

/****** 2. Object:  Table [dbo].[Pet]  ******/
CREATE TABLE [dbo].[Pet](
	[PetID] [int] IDENTITY(1,1) NOT NULL,
	[OwnerID] [int] NULL,
	[Name] [varchar](50) NULL,
	[Age] [numeric](18, 0) NULL,
	[Type] [varchar](50) NULL,
	[Breed] [varchar](50) NULL,
	[Weight] [numeric](18, 0) NULL,
	[Color] [varchar](50) NULL,
	[Gender] [char](10) NULL,
 CONSTRAINT [PK_Pet] PRIMARY KEY CLUSTERED 
(
	[PetID] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO

ALTER TABLE [dbo].[Pet]  WITH CHECK ADD  CONSTRAINT [FK_Pet_PetOwner] FOREIGN KEY([OwnerID])
REFERENCES [dbo].[PetOwner] ([OwnerID])
ON UPDATE CASCADE
ON DELETE CASCADE
GO

ALTER TABLE [dbo].[Pet] CHECK CONSTRAINT [FK_Pet_PetOwner]
GO


/****** 3. Object:  Table [dbo].[Employee]  ******/
CREATE TABLE [dbo].[Employee](
	[EmpNumber] [int] IDENTITY(1,1) NOT NULL,
	[Name] [varchar](50) NULL,
	[Category] [varchar](50) NULL,
	[OfficeNumber] [numeric](18, 0) NULL,
	[TelNumber] [numeric](18, 0) NULL,
	[Email] [varchar](50) NULL,
	[Gender] [char](10) NULL,
 CONSTRAINT [PK_Employee] PRIMARY KEY CLUSTERED 
(
	[EmpNumber] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO

/****** 4. Object:  Table [dbo].[Pharmacy]  ******/
CREATE TABLE [dbo].[Pharmacy](
	[PharmacyID] [int] IDENTITY(1,1) NOT NULL,
	[PharmacyData] [xml] NULL,
 CONSTRAINT [PK_Pharmacy] PRIMARY KEY CLUSTERED 
(
	[PharmacyID] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO

/****** 5. Object:  Table [dbo].[Medication]  ******/
CREATE TABLE [dbo].[Medication](
	[MedicationNumber] [int] IDENTITY(1,1) NOT NULL,
	[MedicationData] [xml] NULL,
 CONSTRAINT [PK_Medication] PRIMARY KEY CLUSTERED 
(
	[MedicationNumber] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO


/****** 6. Object:  Table [dbo].[Stock]  ******/
CREATE TABLE [dbo].[Stock](
	[PharmacyID] [int] NULL,
	[MedicationNumber] [int] NULL,
	[Quantity] [numeric](18, 0) NULL
) ON [PRIMARY]
GO

ALTER TABLE [dbo].[Stock]  WITH CHECK ADD  CONSTRAINT [FK_Stock_Medication] FOREIGN KEY([MedicationNumber])
REFERENCES [dbo].[Medication] ([MedicationNumber])
ON UPDATE CASCADE
ON DELETE CASCADE
GO

ALTER TABLE [dbo].[Stock] CHECK CONSTRAINT [FK_Stock_Medication]
GO

ALTER TABLE [dbo].[Stock]  WITH CHECK ADD  CONSTRAINT [FK_Stock_Pharmacy] FOREIGN KEY([PharmacyID])
REFERENCES [dbo].[Pharmacy] ([PharmacyID])
ON UPDATE CASCADE
ON DELETE CASCADE
GO

ALTER TABLE [dbo].[Stock] CHECK CONSTRAINT [FK_Stock_Pharmacy]
GO


/****** 7. Object:  Table [dbo].[Consultation]  ******/
CREATE TABLE [dbo].[Consultation](
	[ConsultationNumber] [int] IDENTITY(1,1) NOT NULL,
	[PetID] [int] NULL,
	[EmpNumber] [int] NULL,
	[Diagnosis] [varchar](50) NULL,
	[AppointmentRequired] [bit] NULL,
	[Fee] [money] NULL,
 CONSTRAINT [PK_Consultation] PRIMARY KEY CLUSTERED 
(
	[ConsultationNumber] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO

ALTER TABLE [dbo].[Consultation] ADD  CONSTRAINT [DF_Consultation_AppointmentRequired]  DEFAULT ((0)) FOR [AppointmentRequired]
GO

ALTER TABLE [dbo].[Consultation]  WITH CHECK ADD  CONSTRAINT [FK_Consultation_Employee] FOREIGN KEY([EmpNumber])
REFERENCES [dbo].[Employee] ([EmpNumber])
ON UPDATE CASCADE
ON DELETE CASCADE
GO

ALTER TABLE [dbo].[Consultation] CHECK CONSTRAINT [FK_Consultation_Employee]
GO

ALTER TABLE [dbo].[Consultation]  WITH CHECK ADD  CONSTRAINT [FK_Consultation_Pet] FOREIGN KEY([PetID])
REFERENCES [dbo].[Pet] ([PetID])
ON UPDATE CASCADE
ON DELETE CASCADE
GO

ALTER TABLE [dbo].[Consultation] CHECK CONSTRAINT [FK_Consultation_Pet]
GO


/****** 8. Object:  Table [dbo].[Prescription]  ******/
CREATE TABLE [dbo].[Prescription](
	[MedicationNumber] [int] NULL,
	[ConsultationNumber] [int] NULL
) ON [PRIMARY]
GO

ALTER TABLE [dbo].[Prescription]  WITH CHECK ADD  CONSTRAINT [FK_Prescription_Consultation] FOREIGN KEY([ConsultationNumber])
REFERENCES [dbo].[Consultation] ([ConsultationNumber])
GO

ALTER TABLE [dbo].[Prescription] CHECK CONSTRAINT [FK_Prescription_Consultation]
GO

ALTER TABLE [dbo].[Prescription]  WITH CHECK ADD  CONSTRAINT [FK_Prescription_Medication1] FOREIGN KEY([MedicationNumber])
REFERENCES [dbo].[Medication] ([MedicationNumber])
GO

ALTER TABLE [dbo].[Prescription] CHECK CONSTRAINT [FK_Prescription_Medication1]
GO

/****** 9. Object:  Table [dbo].[Appointment]  ******/
CREATE TABLE [dbo].[Appointment](
	[AppointmentID] [int] IDENTITY(1,1) NOT NULL,
	[PetID] [int] NULL,
	[Date] [date] NULL,
	[Time] [time](7) NULL,
	[Status] [varchar](50) NULL,
	[AppointmentFee] [money] NULL,
	[CancellationFee] [money] NULL,
 CONSTRAINT [PK_Appointment] PRIMARY KEY CLUSTERED 
(
	[AppointmentID] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO

ALTER TABLE [dbo].[Appointment] ADD  CONSTRAINT [DF_Appointment_CancellationFee]  DEFAULT ((0.0)) FOR [CancellationFee]
GO

ALTER TABLE [dbo].[Appointment]  WITH CHECK ADD  CONSTRAINT [FK_Appointment_Pet] FOREIGN KEY([PetID])
REFERENCES [dbo].[Pet] ([PetID])
ON UPDATE CASCADE
ON DELETE CASCADE
GO

ALTER TABLE [dbo].[Appointment] CHECK CONSTRAINT [FK_Appointment_Pet]
GO



/****** 10. Object:  Table [dbo].[Personnel]  ******/
CREATE TABLE [dbo].[Personnel](
	[EmpNumber] [int] NULL,
	[AppointmentID] [int] NULL
) ON [PRIMARY]
GO

ALTER TABLE [dbo].[Personnel]  WITH CHECK ADD  CONSTRAINT [FK_Personnel_Appointment] FOREIGN KEY([AppointmentID])
REFERENCES [dbo].[Appointment] ([AppointmentID])
GO

ALTER TABLE [dbo].[Personnel] CHECK CONSTRAINT [FK_Personnel_Appointment]
GO

ALTER TABLE [dbo].[Personnel]  WITH CHECK ADD  CONSTRAINT [FK_Personnel_Employee] FOREIGN KEY([EmpNumber])
REFERENCES [dbo].[Employee] ([EmpNumber])
GO

ALTER TABLE [dbo].[Personnel] CHECK CONSTRAINT [FK_Personnel_Employee]
GO