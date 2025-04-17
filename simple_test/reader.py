from llama_index.vector_stores.neptune import NeptuneAnalyticsVectorStore
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader
from llama_index.core import StorageContext
from IPython.display import Markdown, display

graph_identifier = "g-88svw29re1"
embed_dim = 1536

neptune_vector_store = NeptuneAnalyticsVectorStore(
    graph_identifier=graph_identifier,
    embedding_dimension=embed_dim
)

storage_context = StorageContext.from_defaults(
    vector_store=neptune_vector_store
)

print("Loading index from existing Neptune vector store...")
index = VectorStoreIndex(
    nodes=[], # No new documents/nodes to add
    storage_context=storage_context
)
print("Index loaded successfully.")

query_engine = index.as_query_engine()

query_text = "What is the main topic discussed in the documents?"
response = query_engine.query(query_text)

# Print the response
print("\nQuery:", query_text)
print("Response:", response)