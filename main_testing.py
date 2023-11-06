

import chromadb
chroma_client = chromadb.HttpClient(host='localhost', port=8000)

collection = chroma_client.get_or_create_collection(name="my_collection3")

collection.add(
    
    documents=["This is a document", "This is another document"],
    metadatas=[{"source": "my_source"}, {"source": "my_source"}],
    ids=["id1", "id2"]
)

results = collection.query(
    query_texts=["This is a query document"],
    n_results=2
)

print(results)