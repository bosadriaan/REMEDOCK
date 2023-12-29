import chromadb
from chromadb import Settings

chroma_client = chromadb.HttpClient(host='different-insect-production.up.railway.app', port=80)
print(chroma_client.heartbeat())

from chromadb.utils import embedding_functions

embedding_fn = embedding_functions.SentenceTransformerEmbeddingFunction(
    model_name='BAAI/bge-base-zh-v1.5'
)

collection = chroma_client.get_or_create_collection(
    "demo",
    embedding_function=embedding_fn
)
collection = chroma_client.create_collection(name="test") 

