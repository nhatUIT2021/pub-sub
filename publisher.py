
from google.cloud import pubsub_v1

# TODO(developer)
project_id = "pub-sub-672022"
topic_id = "pubsub"

publisher = pubsub_v1.PublisherClient()
# The `topic_path` method creates a fully qualified identifier
# in the form `projects/{project_id}/topics/{topic_id}`
topic_path = publisher.topic_path(project_id, topic_id)
rows_to_insert = [
    {"Name": "Phred Phlyntstone", "DOB": "1/1/1992", "Sex":"Male"}
    
]

for n in range(1, 2):
    data_str = f"Message number {n}"
    # Data must be a bytestringde
    data = rows_to_insert.encode("utf-8")
    # When you publish a message, the client returns a future.
    future = publisher.publish(topic_path, data)
    print(future.result())

print(f"Published messages to {topic_path}.")

