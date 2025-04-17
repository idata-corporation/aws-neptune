from gremlin_python.driver.driver_remote_connection import DriverRemoteConnection
from gremlin_python.structure import graph

# Replace with your Neptune endpoint
neptune_endpoint = 'db-neptune-1.cluster-coqlbcjj5hcu.us-east-1.neptune.amazonaws.com:8182'

try:
    # Create a DriverRemoteConnection with increased timeouts (optional, but good practice)
    conn = DriverRemoteConnection(
        f'wss://{neptune_endpoint}/gremlin',
        'g',
        read_timeout=60,
        write_timeout=60,
    )

    # Create a Graph object and traversal source
    graph = graph.Graph()
    g = graph.traversal().withRemote(conn)

    # Example: Adding a document node with a vector embedding
    document_id = "doc123"
    vector_embedding = [0.1, 0.5, 0.2, 0.8]  # This is the key:  A standard Python list.
    text_content = "This is some sample text."

    g.addV('document') \
        .property('id', document_id) \
        .property('text', text_content) \
        .property('embedding', vector([0.1, 0.5, 0.2, 0.8])) \
        .next()

    #g.addV('document').property('id', document_id).property('text', text_content).property('embedding', vector_embedding).next()

    # Example: Adding another document node
    #document_id_2 = "doc456"
    #vector_embedding_2 = [0.9, 0.2, 0.7, 0.3]
    #text_content_2 = "Another piece of information."

    #g.addV('document').property('id', document_id_2).property('text', text_content_2).property('embedding', vector_embedding_2).next()

    print("Nodes added successfully.")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    conn.close()
