import csv
from datetime import date

VALID_TRANSACTION_TYPES = {"DEBIT", "CREDIT"}


def load_accounts():
    valid_accounts = set()

    with open("data/accounts.csv", "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            valid_accounts.add(row["AccountID"])

    return valid_accounts


def load_bad_transactions():
    records = []

    with open("data/bad_transactions.csv", "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            records.append(row)

    return records


def test_invalid_account_detected():
    valid_accounts = load_accounts()
    records = load_bad_transactions()

    invalid_accounts = [
        row for row in records
        if row["AccountID"] not in valid_accounts
    ]

    assert len(invalid_accounts) > 0


def test_negative_or_zero_amount_detected():
    records = load_bad_transactions()

    invalid_amounts = [
        row for row in records
        if float(row["Amount"]) <= 0
    ]

    assert len(invalid_amounts) > 0


def test_invalid_transaction_type_detected():
    records = load_bad_transactions()

    invalid_types = [
        row for row in records
        if row["TransactionType"] not in VALID_TRANSACTION_TYPES
    ]

    assert len(invalid_types) > 0


def test_future_transaction_date_detected():
    records = load_bad_transactions()

    future_dates = [
        row for row in records
        if date.fromisoformat(row["TransactionDate"]) > date.today()
    ]

    assert len(future_dates) > 0
    

 
    