import faiss
from sentence_transformers import SentenceTransformer
import ollama

model = SentenceTransformer("all-MiniLM-L6-v2")

documents = []
index = faiss.IndexFlatL2(384)

def chunk_text(text, size=500):
    words = text.split()
    return [" ".join(words[i:i+size]) for i in range(0, len(words), size)]

def add_docs(text):
    chunks = chunk_text(text)
    embeddings = model.encode(chunks)
    print(f"Number of embeddings: {len(embeddings)}")
    index.add(embeddings)
    documents.extend(chunks)
    # save index and documents
    faiss.write_index(index, "faiss_index.idx")
    with open("documents.txt", "w", encoding="utf-8") as f:
        for doc in documents:
            f.write(doc.replace("\n", " ") + "\n")

def ask(question):
    q_emb = model.encode([question])
    print(f"Number of documents in index: {index.ntotal}")
    print(f"Question embedding shape: {q_emb.shape}")
    _, ids = index.search(q_emb, 3)

    context = "\n".join([documents[i] for i in ids[0]])

    prompt = f"""
Answer ONLY using the context below.

Context:
{context}

Question:
{question}
"""
    print(f"Prompt: {prompt}")
    response = ollama.chat(
        model="gpt-oss:20b-cloud",
        #  model="phi",
        messages=[{"role": "user", "content": prompt}]
    )
    print(f"Response: {response}")
    return response["message"]["content"]
