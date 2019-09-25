*** Settings ***
Documentation   SQL Proc Level Tests
Resource  DatabaseConnections.robot
Suite Setup  DatabaseConnections.Connect
Suite Teardown  DatabaseConnections.Disconnect


*** Variables ***



*** Test Cases ***
Insert a Record
    DatabaseConnections.Get Input Data
    DatabaseConnections.Insert Record


Verify the Table
    DatabaseConnections.Verify Table


Verify the Table Records
    DatabaseConnections.Verify Records


