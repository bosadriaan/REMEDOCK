import chromadb
from chromadb import Settings

chroma_client = chromadb.HttpClient(host='different-insect-production.up.railway.app', port=443, ssl=True)
print(chroma_client.heartbeat())

from chromadb.utils import embedding_functions

embedding_fn = embedding_functions.SentenceTransformerEmbeddingFunction(
    model_name='BAAI/bge-base-zh-v1.5'
)

collection = chroma_client.get_or_create_collection(
    "demo",
    embedding_function=embedding_fn
)
collection = chroma_client.get_or_create_collection(name="test") 

collection.add(
    documents=["lorem ipsum...", "doc2", "doc3"],
    metadatas=[{"chapter": "3", "verse": "16"}, {"chapter": "3", "verse": "5"}, {"chapter": "29", "verse": "11"}],
    ids=["id1", "id2", "id3"]
)
print(collection.count())
