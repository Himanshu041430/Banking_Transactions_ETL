import csv
import random
from datetime import date, timedelta

first_names = ["John", "Sarah", "David", "Michael", "Priya", "Daniel", "Emily", "Amit"]
last_names = ["Smith", "Patel", "Lee", "Brown", "Shah", "Wilson", "Taylor", "Singh"]


def random_dob():
    start_date = date(1960, 1, 1)
    end_date = date(2005, 12, 31)

    days_between = (end_date - start_date).days

    return start_date + timedelta(
        days=random.randint(0, days_between)
    )


with open("data/customers.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)

    writer.writerow([
        "CustomerID",
        "FirstName",
        "LastName",
        "Email",
        "Phone",
        "DateOfBirth",
        "Country",
        "CustomerStatus",
        "CreatedDate"
    ])

    for i in range(1, 1001):
        customer_id = 1000 + i

        first_name = random.choice(first_names)
        last_name = random.choice(last_names)

        email = (
            f"{first_name.lower()}."
            f"{last_name.lower()}"
            f"{customer_id}@email.com"
        )

        phone = random.randint(4160000000, 6479999999)

        dob = random_dob()

        status = random.choice([
            "ACTIVE",
            "INACTIVE"
        ])

        writer.writerow([
            customer_id,
            first_name,
            last_name,
            email,
            phone,
            dob.isoformat(),
            "Canada",
            status,
            date.today().isoformat()
        ])


print("customers.csv created successfully")


