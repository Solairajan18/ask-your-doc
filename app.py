import streamlit as st
from loaders import extract_text
from rag import add_docs, ask

st.set_page_config(page_title="Ask Your Docs")

st.title("📄 Ask Your Docs (RAG Chatbot)")

if "chat" not in st.session_state:
    st.session_state.chat = []

uploaded_files = st.file_uploader(
    "Upload documents",
    type=["pdf", "docx", "xlsx", "pptx", "txt", "json"],
    accept_multiple_files=True
)

if uploaded_files:
    for file in uploaded_files:
        text = extract_text(file)
        add_docs(text)
    st.success("Documents indexed successfully!")

question = st.text_input("Ask a question")

if question:
    answer = ask(question)
    st.session_state.chat.append((question, answer))

for q, a in st.session_state.chat:
    st.markdown(f"**You:** {q}")
    st.markdown(f"**Bot:** {a}")
