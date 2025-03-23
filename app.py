import streamlit as st
from chatbot_agent import ChatBot

CHATBOT = ChatBot()
st.title("ChatBot")

# client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

# if "openai_model" not in st.session_state:
#     st.session_state["openai_model"] = "gpt-3.5-turbo"

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input():
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    print("prompt", prompt)
    with st.chat_message("assistant"):
        output = CHATBOT.invoke(prompt)
        print(output)
        response = st.markdown(output)
    st.session_state.messages.append({"role": "assistant", "content": output})