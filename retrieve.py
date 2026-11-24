
from sentence_transformers import SentenceTransformer
import chromadb

# Load embedding model
embedder = SentenceTransformer("all-MiniLM-L6-v2")

# Connect to ChromaDB
client = chromadb.PersistentClient(path="./chroma_db")
collection = client.get_or_create_collection("syllabus")

# Function to retrieve relevant chunks
def retrieve(query, k=3):
    query_vec = embedder.encode([query]).tolist()

    results = collection.query(
        query_embeddings=query_vec,
        n_results=k
    )

    return results["documents"][0]

# Ask a question
question = "What is the main assignment in this PDF?"

# Retrieve matching chunks
top_chunks = retrieve(question)

# Display results
print("RETRIEVED RELEVANT CHUNKS")

for i, chunk in enumerate(top_chunks):
    print(f"\n--- Match {i+1} ---")
    print(chunk[:300])
