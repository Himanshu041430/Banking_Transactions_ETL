def test_reject_reasons(db_connection):

    expected = {
        905001: "INVALID_ACCOUNT",
        905002: "INACTIVE_ACCOUNT",
        905003: "INVALID_AMOUNT",
        905004: "FUTURE_TRANSACTION_DATE",
        905005: "INVALID_TRANSACTION_TYPE",
        905006: "INVALID_TRANSACTION_STATUS",
        905007: "INVALID_CURRENCY",
        905008: "INVALID_CHANNEL"
    }

    cursor = db_connection.cursor()

    cursor.execute("""
        SELECT TransactionID, RejectReason
        FROM BANK_ERR.RejectedTransactions
        WHERE TransactionID BETWEEN 905001 AND 905008
        ORDER BY TransactionID
    """)

    rows = cursor.fetchall()

    cursor.close()

    actual = {
        row.TransactionID: row.RejectReason
        for row in rows
    }

    print("Expected:", expected)
    print("Actual:", actual)

    assert actual == expected
    
    