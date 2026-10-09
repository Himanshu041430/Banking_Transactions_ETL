def test_latest_batch_control(db_connection):

    cursor = db_connection.cursor()

    cursor.execute("""
        SELECT TOP 1
            BatchID,
            PipelineName,
            LoadType,
            SourceCount,
            ValidCount,
            RejectCount,
            Status
        FROM BANK_CTL.BatchControl
        ORDER BY BatchID DESC
    """)

    row = cursor.fetchone()

    cursor.close()

    batch_id = row.BatchID
    pipeline_name = row.PipelineName
    load_type = row.LoadType
    source_count = row.SourceCount
    valid_count = row.ValidCount
    reject_count = row.RejectCount
    status = row.Status

    print("BatchID:", batch_id)
    print("PipelineName:", pipeline_name)
    print("LoadType:", load_type)
    print("SourceCount:", source_count)
    print("ValidCount:", valid_count)
    print("RejectCount:", reject_count)
    print("Status:", status)

    assert status == "SUCCESS"
    assert source_count == valid_count + reject_count
    
    


