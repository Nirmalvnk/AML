# import os
# import streamlit as st
# from dotenv import load_dotenv

# from langchain_community.vectorstores import Chroma
# from langchain_huggingface import HuggingFaceEmbeddings

# from langchain_classic.chains import create_retrieval_chain
# # from langchain.chains.combine_documents import create_stuff_documents_chain
# from langchain_classic.chains.combine_documents import create_stuff_documents_chain
# from langchain_core.prompts import ChatPromptTemplate

# from langchain_groq import ChatGroq

# load_dotenv()

# CHROMA_PATH = "chroma_db"

# st.title("🤖 Nirmal Details Chatbot")
# st.write("Ask anything about Nirmal Kumar")

# # Embeddings
# embeddings = HuggingFaceEmbeddings(
#     model_name="sentence-transformers/all-MiniLM-L6-v2"
# )

# # Load Chroma
# db = Chroma(
#     persist_directory=CHROMA_PATH,
#     embedding_function=embeddings
# )

# retriever = db.as_retriever()

# # Groq model
# llm = ChatGroq(
#     model="llama-3.1-8b-instant",
#     temperature=0.6
# )

# # Prompt
# prompt = ChatPromptTemplate.from_template("""
# You are a chatbot that answers questions about Nirmal Kumar.

# Rules:
# - Only answer questions related to professional or public information.
# - Do NOT answer personal relationship questions.
# - If asked about lover, girlfriend, boyfriend, or relationship, say:
#   "Sorry, I cannot provide personal relationship information."

# <context>
# {context}
# </context>

# Question: {input}
# """)
# # ("""
# # Answer the question using the provided context.

# # <context>
# # {context}
# # </context>

# # Question: {input}
# # """)

# document_chain = create_stuff_documents_chain(llm, prompt)

# qa = create_retrieval_chain(retriever, document_chain)

# # query = st.text_input("Ask a question")

# # if query:
# #     response = qa.invoke({"input": query})
# #     st.write("### Answer")
# #     st.write(response["answer"])

# # Guardrail keywords
# blocked_keywords = [
#     "lover",
#     "girlfriend",
#     "boyfriend",
#     "relationship",
#     "dating",
#     "married",
#     "wife",
#     "husband"
# ]

# query = st.text_input("Ask a question")

# if query:

#     if any(word in query.lower() for word in blocked_keywords):
#         st.write("⚠️ Sorry, I cannot provide personal or relationship information about Nirmal.")
    
#     else:
#         response = qa.invoke({"input": query})
#         st.write("### Answer")
#         st.write(response["answer"])



import os
import streamlit as st
from dotenv import load_dotenv

from langchain_community.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

from langchain_classic.chains import create_retrieval_chain
from langchain_classic.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate

from langchain_groq import ChatGroq

load_dotenv()

CHROMA_PATH = "chroma_db"

st.title("🤖 Nirmal Details Chatbot")
st.write("Ask anything about Nirmal Kumar")

# Embeddings
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# Load Chroma
db = Chroma(
    persist_directory=CHROMA_PATH,
    embedding_function=embeddings
)

retriever = db.as_retriever()

# Groq model
llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0.6
)

# Prompt
prompt = ChatPromptTemplate.from_template("""
You are a chatbot that answers questions about Nirmal Kumar.

Rules:
- Only answer questions related to professional or public information.
- Do NOT answer personal relationship questions.
- If asked about lover, girlfriend, boyfriend, or relationship, say:
  "Sorry, I cannot provide personal relationship information."

<context>
{context}
</context>

Question: {input}
""")

document_chain = create_stuff_documents_chain(llm, prompt)

qa = create_retrieval_chain(retriever, document_chain)

# Guardrail keywords
blocked_keywords = [
    "lover","girlfriend","boyfriend","relationship",
    "dating","married","wife","husband"
]

# Store chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input (GPT style)
query = st.chat_input("Ask a question")

if query:

    # Show user message
    st.session_state.messages.append({"role": "user", "content": query})
    with st.chat_message("user"):
        st.markdown(query)

    # Guardrail check
    if any(word in query.lower() for word in blocked_keywords):
        answer = "⚠️ Sorry, I cannot provide personal or relationship information about Nirmal."

    else:
        response = qa.invoke({"input": query})
        answer = response["answer"]

    # Show assistant message
    with st.chat_message("assistant"):
        st.markdown(answer)

    st.session_state.messages.append({"role": "assistant", "content": answer})