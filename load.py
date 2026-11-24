
from pypdf import PdfReader
from langchain_text_splitters import RecursiveCharacterTextSplitter

# Step 1: Load the PDF
reader = PdfReader("syllabus.pdf")

# Step 2: Extract text from all pages
raw_text = "\n".join(
    page.extract_text() or "" for page in reader.pages
)

# Step 3: Create a text splitter
splitter = RecursiveCharacterTextSplitter(
    chunk_size=200,
    chunk_overlap=40
)

# Step 4: Split the extracted text into chunks
chunks = splitter.split_text(raw_text)

# Step 5: Display the output
print("PDF LOADING AND CHUNKING")

print(f"Total pages: {len(reader.pages)}")
print(f"Extracted {len(chunks)} chunks from the PDF")

print("\nFirst chunk:")
if chunks:
    print(chunks[0][:500])
else:
    print("No text extracted from PDF.")
