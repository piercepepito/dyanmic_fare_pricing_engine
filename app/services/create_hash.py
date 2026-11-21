import hashlib
import json

def create_hash(fare_input: dict) -> str:
    """
    converts a dictionary into a hash 256

    Args:
        fare_input: the input to calculate the date
    Returns:
        str: the converted hash as a hexadecimal string
    """
    #convert dict into a json string, and into bytes
    raw_fare_bytes = json.dumps(fare_input, 
                                sort_keys=True, 
                                separators= (",", ":"),
                                default=str).encode("utf-8")

    return hashlib.sha256(raw_fare_bytes).hexdigest()