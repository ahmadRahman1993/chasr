import streamlit as st


# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


# Streamlit app title
st.title("CHASR BOT")

# React to user input
if prompt := st.chat_input("Ask your question about academic integrity:"):
    # Display user message in chat message container
    st.chat_message("user").markdown(prompt)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

    response = "This is a mock response simulating GPT-4's output for testing purposes."
    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        st.markdown(response)
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})

# Link to the university's academic integrity policy page
#st.markdown("For detailed information, visit the .")

# Rest of your Streamlit code...
# Disclaimer at the top of the page
st.warning("⚠️ Disclaimer: This tool is experimental and intended for testing purposes only.")
