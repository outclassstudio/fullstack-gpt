import streamlit as st
import time

st.set_page_config(page_title="DocumentGPT", page_icon="📔")
st.title("DocumentGPT")

if "messages" not in st.session_state:
    st.session_state["messages"] = []


def send_message(message, role, save=True):
    with st.chat_message(role):
        st.write(message)
    if save:
        st.session_state["messages"].append({"message": message, "role": role})


for msg in st.session_state["messages"]:
    send_message(msg["message"], msg["role"], save=False)


message = st.chat_input("AI에게 질문을 남겨보아요")

if message:
    send_message(message, "human")
    time.sleep(2)
    send_message(f"You said: {message}", "ai")
