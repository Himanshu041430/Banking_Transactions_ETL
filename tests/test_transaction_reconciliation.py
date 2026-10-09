def test_transaction_reconciliation(db_connection):

    cursor = db_connection.cursor()

    cursor.execute("""
        SELECT COUNT(*)
        FROM BANK_STG.Transactions
    """)
    stg_count = cursor.fetchone()[0]

    cursor.execute("""
        SELECT COUNT(*)
        FROM BANK_TGT.Transactions
    """)
    tgt_count = cursor.fetchone()[0]

    cursor.execute("""
        SELECT COUNT(*)
        FROM BANK_ERR.RejectedTransactions
    """)
    reject_count = cursor.fetchone()[0]

    cursor.close()

    print("STG Count:", stg_count)
    print("TGT Count:", tgt_count)
    print("Reject Count:", reject_count)

    assert stg_count == tgt_count + reject_count

    
    
