import streamlit as st
import PyPDF2
import pyttsx3

# Function to read a PDF aloud
def read_pdf_aloud(pdf_file, speech_rate):
    try:
        # Create a PDF Reader object
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        num_pages = len(pdf_reader.pages)

        # Initialize the text-to-speech engine
        tts_engine = pyttsx3.init()

        # Set the speech rate
        tts_engine.setProperty('rate', speech_rate)

        # Extract and read text from each page
        for page_num in range(num_pages):
            page = pdf_reader.pages[page_num]
            text = page.extract_text()

            # Check if text was extracted
            if text.strip():
                st.write(f"**Reading page {page_num + 1}...**")
                st.text(text)  # Display text on the Streamlit app

                # Speak the text aloud
                tts_engine.say(text)
                tts_engine.runAndWait()
            else:
                st.warning(f"Page {page_num + 1} has no readable text.")
    except Exception as e:
        st.error(f"An error occurred while reading the PDF: {e}")

# Streamlit app interface
def main():
    st.title("PDF Reader with Voice")
    st.write("Upload a PDF file, and it will be read aloud. You can also adjust the speech speed.")

    # File uploader for PDF
    uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])

    # Speech rate slider
    speech_rate = st.slider("Speech Rate (words per minute)", min_value=100, max_value=300, value=150, step=10)

    # Read PDF button
    if st.button("Read PDF Aloud"):
        if uploaded_file:
            st.success("Reading the PDF. Please wait...")
            read_pdf_aloud(uploaded_file, speech_rate)
        else:
            st.error("Please upload a PDF file first.")

if __name__ == "__main__":
    main()
