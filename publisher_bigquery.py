from google.cloud import pubsub_v1

# TODO(developer): Choose an existing topic.
project_id = "pub-sub-672022"
topic_id = "pubsub"

publisher_options = pubsub_v1.types.PublisherOptions(enable_message_ordering=True)
# Sending messages to the same region ensures they are received in order
# even when multiple publishers are used.
client_options = {"api_endpoint": "us-east1-pubsub.googleapis.com:443"}
publisher = pubsub_v1.PublisherClient(
    publisher_options=publisher_options, client_options=client_options
)
# The `topic_path` method creates a fully qualified identifier
# in the form `projects/{project_id}/topics/{topic_id}`
topic_path = publisher.topic_path(project_id, topic_id)

for message in [
    ("Name", "Phred Phlyntstone"),
    ("DOB", "1/1/1992"),
    ("Sex", "Male"),
    
]:
    # Data must be a bytestring
    data = message[1].encode("utf-8")
    ordering_key = message[0]
    # When you publish a message, the client returns a future.
    future = publisher.publish(topic_path, data=data, ordering_key=ordering_key)
    print(future.result())

print(f"Published messages with ordering keys to {topic_path}.")