import pytest

@pytest.mark.db
@pytest.mark.reconciliation
def test_db_amount_reconciliation(db_connection):

    cursor = db_connection.cursor()

    stg_query = """
    SELECT COALESCE(SUM(s.Amount), 0)
    FROM BANK_STG.Transactions s
    JOIN BANK_STG.Accounts a
        ON s.AccountID = a.AccountID
    WHERE a.AccountStatus = 'ACTIVE'
      AND s.Amount > 0
      AND s.TransactionDate <= GETDATE()
      AND s.TransactionType IN ('DEBIT', 'CREDIT')
      AND s.TransactionStatus = 'SUCCESS'
      AND s.Currency = 'CAD'
      AND s.Channel IN ('BRANCH', 'ONLINE', 'ATM', 'POS')
      AND NOT EXISTS (
          SELECT 1
          FROM BANK_ERR.RejectedTransactions e
          WHERE e.TransactionID = s.TransactionID
      )
    """

    tgt_query = """
    SELECT COALESCE(SUM(Amount), 0)
    FROM BANK_TGT.Transactions
    """

    cursor.execute(stg_query)
    stg_amount = cursor.fetchone()[0]

    cursor.execute(tgt_query)
    tgt_amount = cursor.fetchone()[0]

    print("Eligible STG Amount:", stg_amount)
    print("Target Amount:", tgt_amount)

    assert stg_amount == tgt_amount, (
        f"Amount reconciliation failed: "
        f"STG={stg_amount}, TGT={tgt_amount}"
    )

    