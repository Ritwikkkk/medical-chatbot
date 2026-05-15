import streamlit as st
from datetime import datetime
import json


# Helper function for placeholder responses
def generate_placeholder_response(user_query: str, model_type: str) -> str:
    """
    Generate a placeholder response. Replace this with your actual chatbot logic.
    """
    responses = {
        "Medical Assistant": f"Based on your question about '{user_query[:50]}...', I can provide medical information. Please note this is not a substitute for professional medical advice. If you're experiencing serious symptoms, please consult a healthcare provider immediately.",
        "General Health Info": f"Regarding '{user_query[:50]}...', here's some general health information. This is educational content and shouldn't replace professional medical consultation.",
        "Symptom Checker": f"For your concern about '{user_query[:50]}...', this could be related to several conditions. However, only a medical professional can provide an accurate diagnosis. Please consult a doctor if symptoms persist."
    }
    
    return responses.get(model_type, "I'm here to help with medical information. Please ask your question clearly.")


# Configure page
st.set_page_config(
    page_title="Medical Chatbot",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
    <style>
    .main {
        padding-top: 2rem;
    }
    .stChatMessage {
        margin-bottom: 1rem;
    }
    </style>
    """, unsafe_allow_html=True)

# Initialize session state for chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
if "user_input" not in st.session_state:
    st.session_state.user_input = ""

# Sidebar
with st.sidebar:
    st.title("⚙️ Settings")
    
    st.markdown("---")
    
    # Model selection
    model_type = st.selectbox(
        "Select Model",
        ["Medical Assistant", "General Health Info", "Symptom Checker"],
        help="Choose the type of medical assistance you need"
    )
    
    st.markdown("---")
    
    # Temperature/response variation
    temperature = st.slider(
        "Response Creativity",
        min_value=0.0,
        max_value=1.0,
        value=0.5,
        help="Lower = more factual, Higher = more creative"
    )
    
    st.markdown("---")
    
    # Clear chat button
    if st.button("🗑️ Clear Chat History", use_container_width=True):
        st.session_state.chat_history = []
        st.success("Chat history cleared!")
    
    st.markdown("---")
    
    # Information
    st.markdown("""
    **About this Chatbot:**
    - Provides medical information and health guidance
    - Not a substitute for professional medical advice
    - Always consult a doctor for serious concerns
    """)

# Main chat area
st.title("🏥 Medical Chatbot Assistant")
st.markdown("Welcome! Ask me any medical or health-related questions. I'm here to help provide information and guidance.")

st.markdown("---")

# Display chat history
chat_container = st.container()
with chat_container:
    for message in st.session_state.chat_history:
        with st.chat_message(message["role"], avatar="👤" if message["role"] == "user" else "🤖"):
            st.markdown(message["content"])
            st.caption(f"_{message['timestamp']}_")

# User input section
st.markdown("---")

# Create columns for input and button
col1, col2 = st.columns([0.92, 0.08])

with col1:
    user_message = st.chat_input(
        placeholder="Type your medical question here...",
        key="chat_input"
    )

# Process user message
if user_message:
    # Add user message to chat history
    timestamp = datetime.now().strftime("%H:%M:%S")
    st.session_state.chat_history.append({
        "role": "user",
        "content": user_message,
        "timestamp": timestamp
    })
    
    # Display user message
    with st.chat_message("user", avatar="👤"):
        st.markdown(user_message)
        st.caption(f"_{timestamp}_")
    
    # Generate bot response (placeholder - integrate your actual chatbot logic here)
    with st.chat_message("assistant", avatar="🤖"):
        with st.spinner("Analyzing your question..."):
            # TODO: Replace this with your actual chatbot API/model call
            # Example: response = get_chatbot_response(user_message, model_type, temperature)
            
            # Placeholder response logic
            response = generate_placeholder_response(user_message, model_type)
            
            response_timestamp = datetime.now().strftime("%H:%M:%S")
            st.markdown(response)
            st.caption(f"_{response_timestamp}_")
    
    # Add bot response to chat history
    st.session_state.chat_history.append({
        "role": "assistant",
        "content": response,
        "timestamp": response_timestamp
    })
    
    # Rerun to update chat display
    st.rerun()

# Helper function for placeholder responses
def generate_placeholder_response(user_query: str, model_type: str) -> str:
    """
    Generate a placeholder response. Replace this with your actual chatbot logic.
    """
    responses = {
        "Medical Assistant": f"Based on your question about '{user_query[:50]}...', I can provide medical information. Please note this is not a substitute for professional medical advice. If you're experiencing serious symptoms, please consult a healthcare provider immediately.",
        "General Health Info": f"Regarding '{user_query[:50]}...', here's some general health information. This is educational content and shouldn't replace professional medical consultation.",
        "Symptom Checker": f"For your concern about '{user_query[:50]}...', this could be related to several conditions. However, only a medical professional can provide an accurate diagnosis. Please consult a doctor if symptoms persist."
    }
    
    return responses.get(model_type, "I'm here to help with medical information. Please ask your question clearly.")

# Footer
st.markdown("---")
st.markdown("""
    <div style='text-align: center; color: gray; font-size: small;'>
    ⚠️ <b>Disclaimer:</b> This chatbot provides general information only and is not a substitute for professional medical advice. 
    Always consult a qualified healthcare provider for diagnosis and treatment.
    </div>
    """, unsafe_allow_html=True)
