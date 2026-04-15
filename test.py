import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# Set up the page title and logo
st.set_page_config(page_title="TRUE Vox", page_icon="🔊")

# Display Logo 
st.markdown("""
    <div style="text-align: center;">
        <h1 style="color: #4B8BF5;">TRUE Vox</h1>
    </div>
""", unsafe_allow_html=True)

# Welcome text
st.markdown("""
    <div style="text-align: center;">
        <h3>Welcome to the Audio Deepfake Detection Tool</h3>
        <p>Upload an audio file to check if it is a deepfake or real.</p>
    </div>
""", unsafe_allow_html=True)

# File uploader
audio_file = st.file_uploader("Upload Audio File", type=["wav"])

if audio_file is not None:
    st.audio(audio_file, format="audio/wav")
    
    # Simulated accuracy and loss over epochs data (replace with actual training history)
    history = {
        'accuracy': np.random.rand(20),  # Simulated train accuracy over 20 epochs
        'val_accuracy': np.random.rand(20),  # Simulated validation accuracy over 20 epochs
        'loss': np.random.rand(20),  # Simulated train loss over 20 epochs
        'val_loss': np.random.rand(20)  # Simulated validation loss over 20 epochs
    }

    # Create a "Predict" button
    if st.button('Predict'):
        # Simulate model prediction (replace with actual model prediction logic)
        prediction = np.random.choice(['Real', 'Fake'])  # Simulate prediction (real or fake)
        
        # Display prediction result
        if prediction == 'Real':
            st.success("This audio is REAL!", icon="✅")
        else:
            st.warning("This audio may be a FAKE!", icon="⚠️")

        # Plot accuracy over epochs
        st.subheader("Model Accuracy Over Epochs")
        plt.figure(figsize=(10, 5))
        plt.plot(history['accuracy'], label='Train Accuracy')
        plt.plot(history['val_accuracy'], label='Validation Accuracy')
        plt.title('Model Accuracy')
        plt.xlabel('Epochs')
        plt.ylabel('Accuracy')
        plt.legend()
        st.pyplot(plt)

        # Plot loss over epochs
        st.subheader("Model Loss Over Epochs")
        plt.figure(figsize=(10, 5))
        plt.plot(history['loss'], label='Train Loss')
        plt.plot(history['val_loss'], label='Validation Loss')
        plt.title('Model Loss')
        plt.xlabel('Epochs')
        plt.ylabel('Loss')
        plt.legend()
        st.pyplot(plt)
