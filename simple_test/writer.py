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

documents = SimpleDirectoryReader("./data").load_data()

storage_context = StorageContext.from_defaults(
    vector_store=neptune_vector_store
)
index = VectorStoreIndex.from_documents(
    documents, storage_context=storage_context
)
print("index loaded")