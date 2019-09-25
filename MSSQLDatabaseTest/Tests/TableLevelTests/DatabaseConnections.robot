*** Settings ***
Library     DatabaseLibrary
Library     String
Library     Dialogs

*** Variables ***
${DB_NAME} =  TestDB
${DB_USER_NAME} =  testuser
${DB_USER_PASSWORD} =  test123
${DB_HOST} =  CPX-CMSUMI7OH6Y
${DB_PORT} =  1433
${PREVIOUS_ROW_COUNT}
${DATATOLOAD}
${FIRSTNAME}
${LASTNAME}


*** Keywords ***
Connect
    [Tags]  TestDB
    Connect to Database  pymssql  ${DB_NAME}  ${DB_USER_NAME}  ${DB_USER_PASSWORD}  ${DB_HOST}  ${DB_PORT}

Disconnect
    [Tags]  TestDB
    delete all rows from table  TestTable
    delete all rows from table  Person
    Disconnect from Database


Get Input Data
    [Tags]  TestDB
    ${dataToLoad} =  get value from user  Enter Data
    ${FirstName} =  get value from user  Enter First Name
    ${LastName} =   get value from user  Enter Last Name
    set suite variable  ${DATATOLOAD}   ${dataToLoad}
    #set suite variable  ${FIRSTNAME}    ${FirstName}
    #set global variable  ${LASTNAME}    ${LastName}


Insert Record
    [Tags]  TestDB
    execute sql string  INSERT INTO TestTable (Name, TextData, Num) VALUES('${DATATOLOAD}','${DATATOLOAD}', 0);
    execute sql string  insert into Person (First_Name, Last_Name) values ('${FIRSTNAME}','${LASTNAME}');


Verify Table
    [Tags]  DBTests
    table must exist  TestTable
    table must exist  Person


Verify Records
    [Tags]  DBTests
    check if exists in database  select * from Person where First_Name = '${FIRSTNAME}' and Last_Name = '${LASTNAME}'
    row count is equal to x  select * from Person   1
    row count is 0  select * from Person where First_Name = '${DATATOLOAD}'
