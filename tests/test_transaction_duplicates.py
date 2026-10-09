
def test_duplicate_transaction_id(db_connection):

    cursor = db_connection.cursor()

    cursor.execute("""
        SELECT COUNT(*)
        FROM
        (
            SELECT TransactionID
            FROM BANK_STG.Transactions
            GROUP BY TransactionID
            HAVING COUNT(*) > 1
        ) AS DuplicateTransactions
    """)

    duplicate_count = cursor.fetchone()[0]

    cursor.close()

    print("Duplicate TransactionID Count:", duplicate_count)

    assert duplicate_count == 0
    
