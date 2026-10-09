import csv
from datetime import date, timedelta

future_date = date.today() + timedelta(days=10)

bad_records = [
    {
        "TransactionID": "999001",
        "AccountID": "999999",
        "TransactionType": "DEBIT",
        "Amount": "100.00",
        "TransactionDate": str(date.today()),
        "Channel": "ATM",
        "Currency": "CAD",
        "TransactionStatus": "SUCCESS"
    },
    {
        "TransactionID": "999002",
        "AccountID": "50001",
        "TransactionType": "DEBIT",
        "Amount": "-50.00",
        "TransactionDate": str(date.today()),
        "Channel": "POS",
        "Currency": "CAD",
        "TransactionStatus": "SUCCESS"
    },
    {
        "TransactionID": "999003",
        "AccountID": "50001",
        "TransactionType": "CREDIT",
        "Amount": "0.00",
        "TransactionDate": str(date.today()),
        "Channel": "ONLINE",
        "Currency": "CAD",
        "TransactionStatus": "SUCCESS"
    },
    {
        "TransactionID": "999004",
        "AccountID": "50001",
        "TransactionType": "TRANSFER",
        "Amount": "250.00",
        "TransactionDate": str(date.today()),
        "Channel": "BRANCH",
        "Currency": "CAD",
        "TransactionStatus": "SUCCESS"
    },
    {
        "TransactionID": "999005",
        "AccountID": "50001",
        "TransactionType": "DEBIT",
        "Amount": "75.00",
        "TransactionDate": str(future_date),
        "Channel": "ATM",
        "Currency": "CAD",
        "TransactionStatus": "SUCCESS"
    }
]

with open("data/bad_transactions.csv", "w", newline="") as file:
    fieldnames = [
        "TransactionID",
        "AccountID",
        "TransactionType",
        "Amount",
        "TransactionDate",
        "Channel",
        "Currency",
        "TransactionStatus"
    ]

    writer = csv.DictWriter(file, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerows(bad_records)

print("bad_transactions.csv created successfully")



