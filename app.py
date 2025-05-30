# app.py
import streamlit as st
from agents.classifier_agent import ClassifierAgent
from memory.memory_store import MemoryStore
from utils.file_parser import parse_input, parse_pdf
import redis

redis_client = redis.Redis(host="localhost", port=6379, db=0)
memory = MemoryStore(redis_client)
classifier = ClassifierAgent(memory)

st.title("📂 Multi-Agent AI System")

uploaded_file = st.file_uploader("Upload JSON / Email (.txt) / PDF", type=["json", "txt", "pdf"])
if uploaded_file:
    if uploaded_file.name.endswith(".pdf"):
        file_path = f"temp_{uploaded_file.name}"
        with open(file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())
        parsed_input = parse_pdf(file_path)
    else:
        content = uploaded_file.read().decode("utf-8")
        parsed_input = parse_input(content)

    classifier.handle_input(parsed_input)
    st.success("✅ File processed successfully!")

    st.subheader("📦 Redis Memory Store")
    memory_contents = {
        key.decode(): redis_client.get(key).decode(errors='ignore')
        for key in redis_client.keys()
    }
    st.json(memory_contents)
