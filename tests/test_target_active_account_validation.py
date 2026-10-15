import pytest

@pytest.mark.db
@pytest.mark.data_quality
def test_target_contains_only_active_accounts(db_connection):

    query = """
    SELECT COUNT(*)
    FROM BANK_TGT.Transactions t
    JOIN BANK_STG.Accounts a
        ON t.AccountID = a.AccountID
    WHERE a.AccountStatus <> 'ACTIVE'
    """

    cursor = db_connection.cursor()
    cursor.execute(query)

    inactive_count = cursor.fetchone()[0]

    print("Inactive Account Transactions In Target:", inactive_count)

    assert inactive_count == 0, \
        f"Transactions from inactive accounts found in target: {inactive_count}"
    