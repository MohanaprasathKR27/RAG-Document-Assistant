
from sentence_transformers import SentenceTransformer
import chromadb
from groq import Groq
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Connect to Groq
groq_client = Groq(api_key=os.environ["GROQ_API_KEY"])

# Load embedding model
embedder = SentenceTransformer("all-MiniLM-L6-v2")

# Connect to ChromaDB
client = chromadb.PersistentClient(path="./chroma_db")
collection = client.get_or_create_collection("syllabus")

# Ask a question
question = "What is the main assignment in this PDF?"

# Convert question into embedding
query_embedding = embedder.encode([question]).tolist()

# Retrieve relevant PDF chunks
results = collection.query(
    query_embeddings=query_embedding,
    n_results=3
)

context = "\n\n".join(results["documents"][0])

# Generate answer using Groq
response = groq_client.chat.completions.create(
    model="openai/gpt-oss-120b",
    messages=[
        {
            "role": "system",
            "content": "Answer the question using only the provided PDF context. If the answer is not present, say so."
        },
        {
            "role": "user",
            "content": f"Context:\n{context}\n\nQuestion: {question}"
        }
    ],
    temperature=0.3
)

# Display answer
print("\nQUESTION:")
print(question)

print("\nAI GENERATED ANSWER:")
print(response.choices[0].message.content)
