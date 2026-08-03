# Local RAG Legal Assistant

## Overview
An offline, privacy-first Retrieval-Augmented Generation (RAG) system built to query sensitive regulatory documents and internal manuals without relying on external APIs. 

## ⚙️ Architecture & Benchmarks
- **Vector Database:** FAISS for local embeddings storage.
- **LLM Engine:** Quantized Llama 3 (8B) via Ollama.
- **Hardware Benchmarks (Desktop RTX 3060):**
  - **VRAM Usage:** ~5.8 GB (INT4 Quantization)
  - **Inference Speed:** ~45 tokens/second
  - **CPU Overhead:** < 15% during retrieval.
- **UI/UX:** Streamlit with a custom acrylic/glassmorphism minimalist aesthetic.

## Installation
```bash
pip install -r requirements.txt
ollama pull llama3
streamlit run app.py
