import csv
import random
from datetime import date, timedelta

# Read valid AccountIDs from accounts.csv
account_ids = []

with open("data/accounts.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        account_ids.append(row["AccountID"])

transaction_types = ["DEBIT", "CREDIT"]
channels = ["ATM", "ONLINE", "POS", "BRANCH"]

with open("data/transactions.csv", "w", newline="") as file:
    writer = csv.writer(file)

    writer.writerow([
        "TransactionID",
        "AccountID",
        "TransactionType",
        "Amount",
        "TransactionDate",
        "Channel",
        "Currency",
        "TransactionStatus"
    ])

    for i in range(1, 5001):
        transaction_id = 900000 + i
        account_id = random.choice(account_ids)
        transaction_type = random.choice(transaction_types)
        amount = round(random.uniform(5.00, 5000.00), 2)

        days_back = random.randint(0, 90)
        transaction_date = date.today() - timedelta(days=days_back)

        channel = random.choice(channels)

        writer.writerow([
            transaction_id,
            account_id,
            transaction_type,
            amount,
            transaction_date,
            channel,
            "CAD",
            "SUCCESS"
        ])

print("transactions.csv created successfully")
