from google.cloud import bigquery
client = bigquery.Client()
    # [END bigquery_simple_app_client]
    # [START bigquery_simple_app_query]
query_job = client.query(
        """
        SELECT
          *
        FROM `tutorial_dataset.user_backup`
        LIMIT 10"""
    )
results = query_job.result()  # Waits for job to complete.
for row in results:
    print("{} : {} views".format(row.Name, row.DOB))