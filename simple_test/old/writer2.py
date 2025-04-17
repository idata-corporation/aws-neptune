import requests
import json

# Replace this with your actual Neptune HTTPS endpoint
neptune_endpoint = 'https://db-neptune-1.cluster-coqlbcjj5hcu.us-east-1.neptune.amazonaws.com:8182/gremlin'

# Construct Gremlin query as a string
query = """
g.addV('document').
  property('id', 'doc123').
  property('embedding', [0.1, 0.5, 0.2, 0.8])
"""

# Construct payload
payload = {
    "gremlin": query
}

# Send the POST request
response = requests.post(neptune_endpoint, json=payload)

# Handle the response
if response.status_code == 200:
    print("Vertex added successfully!")
    print(json.dumps(response.json(), indent=2))
else:
    print(f"Error {response.status_code}:")
    print(response.text)