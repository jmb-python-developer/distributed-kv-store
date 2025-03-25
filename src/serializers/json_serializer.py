import json
from typing import Dict, Any, Union

from src.storage.serializer_interface import SerializerInterface
from src.utils.exceptions import SerializationError


class JSONSerializer(SerializerInterface):
    def serialize(self, data: Dict[str, Any]) -> Union[str, bytes]:
        try:
            return json.dumps(data)
        except (TypeError, ValueError) as e:
            raise SerializationError(f"Failed to serialize data to json {str(data)}")

    def deserialize(self, data: Union[str, bytes]) -> Dict[str, Any]:
        try:
            return json.loads(data)
        except (json.JSONDecodeError, TypeError) as e:
            raise SerializationError(f"Failed to deserialize JSON data: {str(e)}")
