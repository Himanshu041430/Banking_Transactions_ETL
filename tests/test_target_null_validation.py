import pytest

@pytest.mark.db
@pytest.mark.data_quality
def test_target_required_columns_not_null(db_connection):

    query = """
    SELECT COUNT(*)
    FROM BANK_TGT.Transactions
    WHERE TransactionID IS NULL
       OR AccountID IS NULL
       OR Amount IS NULL
       OR TransactionDate IS NULL
       OR TransactionType IS NULL
       OR TransactionStatus IS NULL
       OR Currency IS NULL
       OR Channel IS NULL
    """

    cursor = db_connection.cursor()
    cursor.execute(query)

    null_count = cursor.fetchone()[0]

    print("Target NULL Count:", null_count)

    assert null_count == 0, \
        f"NULL values found in required target columns: {null_count}"

    