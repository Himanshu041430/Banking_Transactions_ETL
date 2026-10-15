import pytest

@pytest.mark.db
@pytest.mark.data_quality
def test_target_domain_values(db_connection):

    query = """
    SELECT COUNT(*)
    FROM BANK_TGT.Transactions
    WHERE TransactionType NOT IN ('DEBIT', 'CREDIT')
       OR TransactionStatus <> 'SUCCESS'
       OR Currency <> 'CAD'
       OR Channel NOT IN ('BRANCH', 'ONLINE', 'ATM', 'POS')
    """

    cursor = db_connection.cursor()
    cursor.execute(query)

    invalid_count = cursor.fetchone()[0]

    print("Invalid Domain Value Count:", invalid_count)

    assert invalid_count == 0, \
        f"Invalid domain values found in target: {invalid_count}"
    