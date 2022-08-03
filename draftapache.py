import apache_beam as beam
options = {'project': "pub-sub-672022",
           'runner': 'DataflowRunner',
           'region': "asia-east1",
           }
pipeline_options = beam.pipeline.PipelineOptions(flags=[], **options)
pipeline = beam.Pipeline(options = pipeline_options)
BQ_source = beam.io.BigQuerySource(query = "select * from tutorial_datast.user_original")
BQ_data = pipeline | beam.io.Read(BQ_source)

"""
# Create a pipeline object using a local runner for execution.
with beam.Pipeline('DirectRunner') as pipeline:
  read_requests = pipeline | beam.Create([
    ReadFromBigQueryRequest(query='SELECT * FROM tutorial_dataset.user_original'),
    ReadFromBigQueryRequest(table='pub-sub-672022.tutorial_dataset.user_original')])
  results = read_requests | ReadAllFromBigQuery()
"""

"""
    main_table = pipeline | 'VeryBig' >> beam.io.ReadFromBigQuery(table='pub-sub-672022:tutorial_dataset.user_original',gcs_location='gs://nhat441992')
    side_table = pipeline | 'NotBig' >> beam.io.ReadFromBigQuery(table='pub-sub-672022:tutorial_dataset.user_original',gcs_location='gs://nhat441992')
    results = (
        main_table
        | 'ProcessData' >> beam.Map(
            lambda element, side_input: ..., AsList(side_table)))
"""