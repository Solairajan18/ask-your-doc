# 📄 Ask Your Docs – Simple RAG Chatbot

A **simple RAG-based “Ask Your Docs” chatbot** built using **free and open-source tools only**.  
Users can upload documents and ask questions, and the chatbot answers **strictly from the uploaded documents** using Retrieval-Augmented Generation (RAG).

This project is intended as a **working demo**, not production software, and can be completed in **2–3 hours**.

---

## ✨ Features

- Single-page web UI (Streamlit)
- Upload and process multiple document formats:
  - PDF
  - Word (.docx)
  - Excel (.xlsx)
  - PowerPoint (.pptx)
  - TXT
  - JSON
- Ask natural-language questions about uploaded documents
- Answers generated **only from document content**
- Chat history displayed on the same page
- Runs fully **offline and locally**
- No paid APIs, no cloud services

---

## 🧠 Tech Stack

| Layer         | Tool                |
|--------------|---------------------|
| Frontend UI  | Streamlit           |
| Backend      | Python              |
| SLM (Local)  | Ollama              |
| Model        | Phi                 |
| Embeddings   | sentence-transformers|
| Embedding Model | all-MiniLM-L6-v2 |
| Embedding Dim | 384                |
| Vector DB    | FAISS (local)       |

---

## 🏗️ Architecture (RAG Flow)

1. User uploads documents via the UI
2. Documents are parsed into raw text
3. Text is split into chunks
4. Each chunk is converted into an embedding
5. Embeddings are stored in FAISS
6. User question is embedded
7. FAISS retrieves the most relevant chunks
8. Retrieved context + question is sent to the local SLM
9. Answer is displayed in the UI

---

## 📂 Project Structure

ask-your-doc/
│
├── app.py           # Streamlit UI and chat logic
├── rag.py           # RAG pipeline (FAISS + Ollama)
├── loaders.py       # Document parsing logic
├── requirements.txt # Python dependencies
└── data/
    └── faiss_index/ # (Optional) persistent vector store

---

## 🚀 Setup Instructions

### 1️⃣ Install Ollama

Download and install Ollama:

https://ollama.com/download

Pull the Phi model:
```bash
ollama pull phi
```

Test Ollama:
```bash
ollama run phi
```

### 2️⃣ Create and Activate Virtual Environment
```bash
python -m venv venv
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### 3️⃣ Install Python Dependencies
```bash
pip install -r requirements.txt
```

### ▶️ Run the Application
```bash
streamlit run app.py
```

Open your browser:

http://localhost:8501

---

## ⚙️ Key Configuration Details

- Embedding model: all-MiniLM-L6-v2
- Embedding dimension: 384
- Chunk size: 300–500 words
- Top-K retrieval: 2–3 chunks
- Phi context window: ~2048 tokens

---

## ⚠️ Common Mistakes to Avoid

- Forgetting to start Ollama before running the app
- Using the wrong FAISS embedding dimension
- Creating very large text chunks
- Expecting answers outside the uploaded documents
- Treating model warnings as errors (most are safe to ignore)

---

## ✅ Project Status

- Beginner-friendly
- Fully local execution
- Free-tier and open-source only
- Suitable for:
  - Learning RAG
  - Interview demos
  - GitHub portfolio projects

---


## ✅ Minimum Requirements (Working Demo)

| Component | Requirement |
|-----------|------------|
| OS        | Windows 10+, macOS, or Linux |
| CPU       | 4-core CPU (Intel i5 / Ryzen 5 or equivalent) |
| RAM       | 8 GB RAM |
| Disk Space| ~5–8 GB free |
| Python    | 3.9 – 3.11 |
| Internet  | Required only for first-time model download |

---

## 📌 Possible Enhancements (Optional)

- Show source chunks below each answer
- Persist FAISS index to disk
- Add document metadata and filtering
- Switch Phi → Mistral or Phi-3
- Add multi-document comparison

---

## 📜 License

MIT License  
Free to use, modify, and share.

---

## 👤 Author

**Solai Rajan**  
[https://www.solairajan.space/](https://www.solairajan.space/)
