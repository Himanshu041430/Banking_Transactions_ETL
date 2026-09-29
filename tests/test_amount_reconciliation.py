def test_transaction_amount_reconciliation():
    source_amounts = [100, 250, 50]
    target_amounts = [100, 250, 50]
    assert sum(source_amounts) == sum(target_amounts)

def test_amount_by_transaction_id():
    source = {"TXN001": 100, "TXN002": 250}
    target = {"TXN001": 100, "TXN002": 250}

    assert sum(source.values()) == sum(target.values())
    assert source == target