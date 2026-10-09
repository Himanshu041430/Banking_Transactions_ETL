from src.db_connection import get_connection


def test_reject_leakage():

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT COUNT(*)
        FROM BANK_ERR.RejectedTransactions R
        JOIN BANK_TGT.Transactions T
            ON R.TransactionID = T.TransactionID
    """)

    leakage_count = cursor.fetchone()[0]

    cursor.close()
    connection.close()

    print("Rejected Rows Found In Target:", leakage_count)

    assert leakage_count == 0

    

    