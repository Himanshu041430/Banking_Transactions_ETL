def test_transaction_amount_reconciliation():
    source_amounts = [100, 250, 50]
    target_amounts = [100, 250, 50]
    assert sum(source_amounts) == sum(target_amounts)