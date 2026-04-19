import streamlit as st
from main import ask

st.set_page_config(page_title="EDGE Chatbot", page_icon="💬", layout="centered")

st.markdown("""
<style>
#MainMenu, footer, header { visibility: hidden; }
.block-container { max-width: 780px; padding-top: 2rem; }
</style>
""", unsafe_allow_html=True)

st.title("💬 EDGE Chatbot")
st.caption("Ask anything about the EDGE Bangladesh knowledge base.")
st.divider()

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

if prompt := st.chat_input("Type your question…"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Searching knowledge base…"):
            answer = ask(prompt)
        st.markdown(answer)
        st.session_state.messages.append({"role": "assistant", "content": answer})

with st.sidebar:
    st.header("EDGE Chatbot")
    st.caption("Powered by llama3.2:1b + nomic-embed-text")
    st.divider()
    if st.button("🗑️ Clear chat"):
        st.session_state.messages = []
        st.rerun()