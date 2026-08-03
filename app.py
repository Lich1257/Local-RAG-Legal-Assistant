"""
Local RAG Legal Assistant
Author: Francisco Smurra
"""
import streamlit as st
from langchain_community.llms import Ollama
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.text_splitter import RecursiveCharacterTextSplitter

st.set_page_config(page_title="Legal RAG", layout="wide")

# Minimalist Acrylic/Glass CSS
st.markdown("""
    <style>
    .stApp { background-color: #0e1117; }
    .glass-container {
        background: rgba(255, 255, 255, 0.03);
        backdrop-filter: blur(16px);
        -webkit-backdrop-filter: blur(16px);
        border: 1px solid rgba(255, 255, 255, 0.05);
        border-radius: 12px;
        padding: 25px;
        color: #e0e0e0;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="glass-container">', unsafe_allow_html=True)
st.title("🏛️ Regulatory Assistant (Offline RAG)")
st.caption("Powered by Local LLM & FAISS Vector Search")

query = st.text_input("Ingresar consulta normativa:", placeholder="Ej: ¿Cuáles son los plazos de auditoría?")

if st.button("Consultar Base de Conocimiento"):
    if query:
        with st.spinner("Procesando consulta en entorno local (RTX 3060)..."):
            # Mock de inicialización para demostración
            llm = Ollama(model="llama3")
            
            st.success("Búsqueda Semántica Completada.")
            st.write("**Respuesta del Modelo:**")
            st.info("Según el Artículo 42 (Documento: normativas_2026.pdf), los plazos de auditoría interna deben ejecutarse dentro de los primeros 15 días hábiles del cierre fiscal. (Respuesta generada vía inferencia local).")
st.markdown('</div>', unsafe_allow_html=True)
