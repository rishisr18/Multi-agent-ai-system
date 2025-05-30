# Multi-Agent AI System

A modular AI system that accepts inputs in **PDF**, **JSON**, or **Email (text)** formats, classifies the input format and intent, and routes it to specialized agents for processing. The system maintains shared context using Redis to enable chaining, traceability, and enhanced collaboration between agents.

---

## Features

- **Classifier Agent**  
  Classifies input format (PDF, JSON, Email) and detects intent (e.g., Invoice, RFQ, Complaint).

- **JSON Agent**  
  Processes structured JSON payloads, reformats to target schema, and flags anomalies or missing fields.

- **Email Agent**  
  Extracts sender, intent, urgency, and formats the email content for CRM-style usage.

- **Shared Memory Module**  
  Uses Redis to store source, type, timestamp, extracted values, and conversation ID accessible across agents.

- **Open-Source LLM Integration**  
  Uses Openai for intent detection and classification instead of OpenAI API.

- **Streamlit Frontend**  
  Simple UI to upload files, view classification and extracted results interactively.

---

## Tech Stack

- **Python 3.9+**
- **Redis** (for shared memory/context)
- **PyMuPDF** (for PDF parsing)
- **Streamlit** (frontend UI)
- Other libraries: `json`, `email`, `subprocess`, etc.

---



