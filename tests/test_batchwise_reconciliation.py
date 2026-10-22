
import pytest

@pytest.mark.db
@pytest.mark.reconciliation
def test_batchwise_reconciliation(db_connection):

    cursor = db_connection.cursor()

    query = """
    SELECT
        BatchID,
        SourceCount,
        ValidCount,
        RejectCount
    FROM BANK_CTL.BatchControl
    """

    cursor.execute(query)
    rows = cursor.fetchall()

    assert len(rows) > 0, "No batch records found"

    for row in rows:
        batch_id = row.BatchID
        source_count = row.SourceCount
        valid_count = row.ValidCount
        reject_count = row.RejectCount

        assert source_count is not None
        assert valid_count is not None
        assert reject_count is not None

        total_processed = valid_count + reject_count

        print(
            f"Batch {batch_id}: Source={source_count}, "
            f"Valid={valid_count}, Reject={reject_count}"
        )

        assert source_count == total_processed, (
            f"Batch {batch_id} reconciliation failed: "
            f"Source={source_count}, Processed={total_processed}"
        )
