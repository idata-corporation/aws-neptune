import requests
import json

neptune_system_endpoint = 'https://db-neptune-1.cluster-coqlbcjj5hcu.us-east-1.neptune.amazonaws.com:8182/system'

payload = {
  "operation": "createVectorIndex",
  "params": {
    "property": "embedding",
    "dimension": 4,
    "metric": "cosine"
  }
}

headers = {
  'Content-Type': 'application/json'
}

response = requests.post(neptune_system_endpoint, headers=headers, json=payload)

if response.status_code == 200:
    print("Vector index created successfully.")
    print(json.dumps(response.json(), indent=2))
else:
    print(f"Error {response.status_code}:")
    print(response.text)