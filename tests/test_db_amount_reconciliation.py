import pytest

@pytest.mark.db
@pytest.mark.reconciliation
def test_db_amount_reconciliation(db_connection):

    cursor = db_connection.cursor()

    stg_query = """
    SELECT COALESCE(SUM(t.Amount), 0)
    FROM BANK_STG.Transactions t
    JOIN BANK_STG.Accounts a
        ON t.AccountID = a.AccountID
    WHERE a.AccountStatus = 'ACTIVE'
      AND t.Amount > 0
      AND t.TransactionDate <= GETDATE()
      AND t.TransactionType IN ('DEBIT', 'CREDIT')
      AND t.TransactionStatus = 'SUCCESS'
      AND t.Currency = 'CAD'
      AND t.Channel IN ('BRANCH', 'ONLINE', 'ATM', 'POS')
    """

    tgt_query = """
    SELECT COALESCE(SUM(Amount), 0)
    FROM BANK_TGT.Transactions
    """

    cursor.execute(stg_query)
    stg_amount = cursor.fetchone()[0]

    cursor.execute(tgt_query)
    tgt_amount = cursor.fetchone()[0]

    print("Valid STG Amount:", stg_amount)
    print("TGT Amount:", tgt_amount)

    assert stg_amount == tgt_amount, \
        f"Amount reconciliation failed: STG={stg_amount}, TGT={tgt_amount}"

    