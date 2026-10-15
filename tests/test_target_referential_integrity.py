import pytest

@pytest.mark.db
@pytest.mark.data_quality
def test_target_account_referential_integrity(db_connection):

    query = """
    SELECT COUNT(*)
    FROM BANK_TGT.Transactions t
    LEFT JOIN BANK_STG.Accounts a
        ON t.AccountID = a.AccountID
    WHERE a.AccountID IS NULL
    """

    cursor = db_connection.cursor()
    cursor.execute(query)

    orphan_count = cursor.fetchone()[0]

    print("Orphan AccountID Count:", orphan_count)

    assert orphan_count == 0, \
        f"Orphan AccountIDs found in target: {orphan_count}"
    