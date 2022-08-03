"""Publishes multiple messages to a Pub/Sub topic with an error handler."""
from google.api_core.exceptions import NotFound
from google.cloud.pubsub import PublisherClient
from google.protobuf.json_format import MessageToJson
from google.pubsub_v1.types import Encoding

# TODO(developer)
project_id = "pub-sub-672022"
topic_id = "writetobigquery"





publisher_client = PublisherClient()
topic_path = publisher_client.topic_path(project_id, topic_id)
class User:
    def __init__(self,Name,DOB,Sex) -> None:
        
        self.Name=Name
        self.DOB=DOB
        self.Sex=Sex

try:
    # Get the topic encoding type.
    topic = publisher_client.get_topic(request={"topic": topic_path})
    encoding = topic.schema_settings.encoding

    # Instantiate a protoc-generated class defined in `us-states.proto`.
    user = User("test","1/1/1990","Male")
    

    # Encode the data according to the message serialization type.
    if encoding == Encoding.BINARY:
        data = user.SerializeToString()
        print(f"Preparing a binary-encoded message:\n{data}")
    elif encoding == Encoding.JSON:
        json_object = MessageToJson(user)
        data = str(json_object).encode("utf-8")
        print(f"Preparing a JSON-encoded message:\n{data}")
    else:
        print(f"No encoding specified in {topic_path}. Abort.")
        exit(0)

    future = publisher_client.publish(topic_path, data)
    print(f"Published message ID: {future.result()}")

except NotFound:
    print(f"{topic_id} not found.")