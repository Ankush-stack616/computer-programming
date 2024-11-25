# Convert a dictionary into a JSON string and back.

import json

dictionary = {'name': 'Alice', 'age': 25, 'city': 'New York'}
json_string = json.dumps(dictionary)
print("JSON string:", json_string)
print("Converted back to dictionary:", json.loads(json_string))

