-- database
USE strabismus

-- create table
CREATE TABLE cleaned_strabismus_data (
    "Subject_ID" VARCHAR,
    "Group" VARCHAR,
    "Age" INT,
    "Fuse_status" BOOLEAN,
    "NDE" VARCHAR,
    "VA_OD" FLOAT,
    "VA_OS" FLOAT,
    "Aulcsf_OD" FLOAT,
    "Aulcsf_OS" FLOAT,
    "Aulcsf_OU" FLOAT,
    "Csf_acuity_OD" FLOAT,
    "Csv_acuity_OS" FLOAT,
    "Csf_acuity_OU" FLOAT,
    "Beta_OD" FLOAT,
    "Beta_OS" FLOAT,
    "Beta_OU" FLOAT,
    "Delta_OD" FLOAT,
    "Delta_OS" FLOAT,
    "Delta_OU" FLOAT,
    "Fmax_OD" FLOAT,
    "Fmax_OS" FLOAT,
    "Fmax_OU" FLOAT,
    "Gamma_OD" FLOAT,
    "Gamme_OS" FLOAT,
    "Gamma_OU" FLOAT,
    "Ref_OD (Sphere CyL Axis)" VARCHAR,
    "Ref_OS" VARCHAR,
    "Type" VARCHAR
)
GO
BULK INSERT cleaned_strabismus_data
    FROM 'projects\strabismus_project_20221003\strabismus_data.csv'
    WITH
        (FIRSTROW = 2,
        FIELDTERMINATOR = ',',
        ROWTERMINATOR = '\n')
GO

SELECT * FROM cleaned_strabismus_data;