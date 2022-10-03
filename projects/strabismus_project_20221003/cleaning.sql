BULK INSERT strabismus_data
FROM "C:\Users\chloe\chloelinli.github.io\projects\strabismus_project_20221003\strabismus_data.csv"
WITH
    (FIRST ROW = 2
    FIELDTERMINATOR = ","
    ROWTERMINATOR = "\n"
    TABLOCK);