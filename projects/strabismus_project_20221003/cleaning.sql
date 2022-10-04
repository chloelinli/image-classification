-- database
USE strabismus

-- create table
CREATE TABLE cleaned_strabismus_data
    (Subject_ID VARCHA PRIMARY KEY,
    GROUP VARCHAR,
    AGE INT,
    Fuse_status BOOLEAN,
    NDE VARCHAR,
    VA_OD FLOAT,
    VA_OS FLOAT,
    Aulcsf_OD FLOAT,
    AULCSF_OS FLOAT,
    Aulcsf_OU FLOAT,
    Csf_acuity_OD FLOAT,
    Csv_acuity_OS FLOAT,
    Csf_acuity_OU FLOAT,
    Beta_OD FLOAT,
    BETA_OS FLOAT,
    BETA_OU FLOAT,
    DELTA_OD FLOAT,
    DELTA_OS FLOAT,
    DELTA_OU FLOAT,
    Fmax_OD FLOAT,
    Fmax_OS FLOAT,
    Fmax_OU FLOAT,
    Gamma_OD FLOAT,
    Gamma_OS FLOAT,
    Gamma_OU FLOAT,
    'Ref_OD (Sphere CyL Axis)' VARCHAR,
    Ref_OS VARCHAR,
    Type VARCHAR)
GO
BULK INSERT cleaned_strabismus_data
    FROM 'C:\Users\chloe\chloelinli.github.io\projects\strabismus_project_20221003\strabismus_data.csv'
    WITH
        (FIRSTROW = 2,
        FIELDTERMINATOR = ',',
        ROWTERMINATOR = '\n')
GO