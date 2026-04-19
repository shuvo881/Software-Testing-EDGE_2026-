import streamlit as st
from main import agent

st.set_page_config(page_title="EDGE Chatbot", page_icon="💬", layout="centered")

st.markdown("""
<style>
#MainMenu, footer, header { visibility: hidden; }
.block-container { max-width: 780px; padding-top: 2rem; }
</style>
""", unsafe_allow_html=True)

# ── Title ─────────────────────────────────────────────────────────────────────
st.title("💬 EDGE Chatbot")
st.caption("Ask anything about the EDGE Bangladesh knowledge base.")
st.divider()

# ── Session state ─────────────────────────────────────────────────────────────
if "messages" not in st.session_state:
    st.session_state.messages = []

# ── Chat history ──────────────────────────────────────────────────────────────
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# ── Input & response ──────────────────────────────────────────────────────────
if prompt := st.chat_input("Type your question…"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Searching knowledge base…"):
            response = agent.run(prompt)
            answer = response.content if hasattr(response, "content") else str(response)
        st.markdown(answer)
        st.session_state.messages.append({"role": "assistant", "content": answer})

# ── Sidebar ───────────────────────────────────────────────────────────────────
with st.sidebar:
    st.header("EDGE Chatbot")
    st.caption("Powered by llama3.2:1b + nomic-embed-text")
    st.divider()
    if st.button("🗑️ Clear chat"):
        st.session_state.messages = []
        st.rerun()