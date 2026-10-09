import csv
import random
from datetime import date

account_types = ["CHECKING", "SAVINGS"]
account_statuses = ["ACTIVE", "INACTIVE"]

with open("data/accounts.csv", "w", newline="") as file:
    writer = csv.writer(file)

    writer.writerow([
        "AccountID",
        "CustomerID",
        "AccountType",
        "Balance",
        "Currency",
        "AccountStatus",
        "OpenDate"
    ])

    account_id = 50001

    for customer_id in range(1001, 2001):
        number_of_accounts = random.choice([1, 1, 1, 2])

        for _ in range(number_of_accounts):
            account_type = random.choice(account_types)
            balance = round(random.uniform(100.00, 25000.00), 2)
            status = random.choice(account_statuses)

            writer.writerow([
                account_id,
                customer_id,
                account_type,
                balance,
                "CAD",
                status,
                date.today()
            ])

            account_id += 1

print("accounts.csv created successfully")