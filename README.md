# Banking Transactions ETL Testing & Python Automation

This project demonstrates end-to-end ETL testing for banking transaction data using SQL, Python, pytest, Azure SQL, and Azure Data Factory concepts.

## Project Objective

The goal is to validate banking transaction data from staging to target and reject tables using manual SQL validation and automated Python tests.

## Technologies

- Python
- pytest
- SQL
- Azure SQL Database
- Azure Data Factory
- pyodbc
- Git / GitHub
- VS Code

## ETL Flow

```text
Source CSV
   ↓
BANK_STG.Transactions
   ↓
Business Rule Validation
   ↓
Valid Records → BANK_TGT.Transactions
Invalid Records → BANK_ERR.RejectedTransactions
   ↓
BANK_CTL.BatchControl
