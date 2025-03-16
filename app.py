# Import the required modules from src package
from src import st, GOOGLE_API_KEY
from src.helper import get_gemini_response, input_pdf_text
from src.prompt import input_prompt

def main():
    """Main function to run the Streamlit application"""
    
    # App title and description
    st.title("Smart Resume Analyzer")
    st.text("Improve Your Resume with Our Smart Resume Analyzer")

    # Check if API key is loaded
    if not GOOGLE_API_KEY:
        st.error("API Key not found! Check your .env file.")
        st.stop()

    # User inputs
    jd = st.text_area("Paste the Job Description")
    uploaded_file = st.file_uploader("Upload your Resume", type="pdf", help="Please upload a PDF file")

    # Submit button
    submit = st.button("Submit")

    if submit:
        if uploaded_file is not None:
            try:
                # Process the uploaded resume
                with st.spinner("Analyzing your resume..."):
                    text = input_pdf_text(uploaded_file)
                    response = get_gemini_response(input_prompt.format(text=text, jd=jd))
                
                # Display results
                st.subheader("Analysis Results")
                st.write(response)
            except Exception as e:
                st.error(f"An error occurred: {str(e)}")
        else:
            st.error("Please upload a resume PDF file")

if __name__ == "__main__":
    main()