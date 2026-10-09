CREATE SCHEMA BANK_STG;
GO

CREATE TABLE BANK_STG.Customers (
    CustomerID INT PRIMARY KEY,
    FirstName VARCHAR(50) NOT NULL,
    LastName VARCHAR(50) NOT NULL,
    Email VARCHAR(100) NOT NULL,
    Phone VARCHAR(20),
    DateOfBirth DATE NOT NULL,
    Country VARCHAR(50) NOT NULL,
    CustomerStatus VARCHAR(20) NOT NULL,
    CreatedDate DATE NOT NULL
);

CREATE TABLE BANK_STG.Accounts (
    AccountID INT PRIMARY KEY,
    CustomerID INT NOT NULL,
    AccountType VARCHAR(20) NOT NULL,
    Balance DECIMAL(12,2) NOT NULL,
    Currency VARCHAR(10) NOT NULL,
    AccountStatus VARCHAR(20) NOT NULL,
    OpenDate DATE NOT NULL
);

CREATE TABLE BANK_STG.Transactions (
    TransactionID INT PRIMARY KEY,
    AccountID INT NOT NULL,
    TransactionType VARCHAR(20) NOT NULL,
    Amount DECIMAL(12,2) NOT NULL,
    TransactionDate DATE NOT NULL,
    Channel VARCHAR(20) NOT NULL,
    Currency VARCHAR(10) NOT NULL,
    TransactionStatus VARCHAR(20) NOT NULL
);
