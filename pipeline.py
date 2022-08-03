#import argparse
import apache_beam as beam
from apache_beam import window
from apache_beam.options.pipeline_options import PipelineOptions, StandardOptions


# project-id:dataset_id.table_id
table_spec = 'pub-sub-672022:tutorial_dataset.user_original'
table_spec1 = 'pub-sub-672022:tutorial_dataset.user_backup'

pipeline_options = PipelineOptions()
pipeline_options.view_as(StandardOptions).streaming = True

options = PipelineOptions([
    "--runner=FlinkRunner",
    "--flink_master=localhost:8081",
    "--environment_type=LOOPBACK"
])
# Create a pipeline object using a local runner for execution.
with beam.Pipeline( options=options) as pipeline:
    result = (
        pipeline
        | 'ReadTable' >> beam.io.ReadFromBigQuery(table=table_spec,gcs_location='gs://nhat441992')
        | 'windows' >> beam.WindowInto(window.FixedWindows(10))

        |'WritetoPubsub' >> beam.io.WriteToPubSub(topic="projects/pub-sub-672022/topics/writetobigquery" , ) 
        #| 'windows2' >>beam.WindowInto(window.FixedWindows(60))
        #| 'group' >> beam.GroupBy(lambda s: s[2])



        |'ReadfromPubsub' >> beam.io.ReadFromPubSub(topic="projects/pub-sub-672022/topics/writetobigquery" , )
        #| 'windows3' >>beam.WindowInto(window.FixedWindows(60))
        #| 'group3' >> beam.GroupByKey()
        |'WritetoBigquery' >> beam.io.WriteToBigQuery(table=table_spec1,)
        #| 'windows4' >>beam.WindowInto(window.FixedWindows(15, 0))
        #| 'group3' >> beam.GroupByKey()
    )
    
#pipeline.run()
#|'WritetoPubsub' >> beam.io.WriteToPubSub(topic='projects/pub-sub-672022/topics/my-topic')

