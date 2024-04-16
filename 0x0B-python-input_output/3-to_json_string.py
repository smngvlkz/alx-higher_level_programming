#!//usr/bin/python3
import json

def to_json_string(my_obj):
    """
    Returns the JSON representation of an object (string).

    Args:
        my_obj: Object to be converted toa JSON string.

    Returns:
        str: JSON string representation of `my_obj`.

    Raises:
        TypeError: `my_object if is not JSON serializable.
    """
    return json.dumps(my_obj)
