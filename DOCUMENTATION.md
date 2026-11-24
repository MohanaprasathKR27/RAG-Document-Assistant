
# RAG Assignment – Automation in Software Development

## 1. Objective
To build a Retrieval-Augmented Generation (RAG) pipeline using Python, Groq API, Sentence Transformers and ChromaDB.

## 2. Programs Executed
1. first_api.py – Groq API call
2. load.py – PDF loading and text chunking
3. store.py – Embedding generation and storage
4. retrieve.py – Retrieving relevant PDF chunks
5. generate.py – Generating answers using retrieved context

## 3. PDF Details
- PDF: syllabus.pdf
- Total pages: 3
- Chunk size: 200
- Chunk overlap: 40
- Total chunks: 48

## 4. Technologies Used
- Python
- Groq API
- LangChain Text Splitters
- Sentence Transformers
- ChromaDB
- PyPDF

## 5. Question Evaluation
Record the actual results of your five questions below.

| Question | Result |
|---|---|
| Question 1 | Pending |
| Question 2 | Pending |
| Question 3 | Pending |
| Question 4 | Pending |
| Question 5 | Pending |

## 6. RAG Limitation
One incorrect answer: [Write the actual incorrect answer observed]

Reason: The retriever may not have selected the most relevant PDF chunk. This can happen because of chunk size, chunk overlap or similarity matching.

## 7. Conclusion
Successfully implemented a complete RAG pipeline that loads PDF documents, splits text into chunks, generates embeddings, stores them in ChromaDB, retrieves relevant information and generates answers using Groq.
