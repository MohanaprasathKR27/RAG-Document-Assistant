
from sentence_transformers import SentenceTransformer
import chromadb
from load import chunks

# Step 1: Load embedding model
print("Loading embedding model...")
embedder = SentenceTransformer("all-MiniLM-L6-v2")

# Step 2: Create ChromaDB client
client = chromadb.PersistentClient(path="./chroma_db")

# Step 3: Create collection
collection = client.get_or_create_collection("syllabus_200")

# Step 4: Convert chunks into embeddings
print("Creating embeddings...")
embeddings = embedder.encode(chunks).tolist()

# Step 5: Store chunks and embeddings
collection.add(
    documents=chunks,
    embeddings=embeddings,
    ids=[f"chunk-{i}" for i in range(len(chunks))]
)

# Step 6: Display output
print("Indexed all chunks into the vector store")
print(f"Total chunks stored: {len(chunks)}")
