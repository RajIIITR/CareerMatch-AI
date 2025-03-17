# CareerMatch-AI

CareerMatch-AI is an AI-powered tool designed to help job seekers evaluate their resumes against job descriptions. It provides ATS-friendly match scores, profile summaries, and optimization suggestions to enhance resume effectiveness.

## 🚀 Features
- 📄 **Resume & Job Description Analysis**: Upload your resume and job description to get an AI-generated match score.
- 🎯 **ATS-Friendly Suggestions**: Improve your resume with insights tailored to Applicant Tracking Systems (ATS).
- 📝 **Profile Summary Generation**: Get a professional summary generated based on your resume and job description.
- 🌐 **Interactive Web App**: Built using Streamlit for an easy-to-use interface.

## 🛠️ Technologies Used
- **Python** 🐍
- **Streamlit** (for deployment and user interface)
- **Google Generative AI** (Used Gemini-2.0-Flash model as our LLM model)
- **PyPDF2** (for parsing PDF resumes)
- **python-dotenv** (for environment variable management)

## 📌 How to Run Locally

### Installation Steps
1. **Clone the Repository**
   ```bash
   git clone https://github.com/RajIIITR/CareerMatch-AI.git
   cd CareerMatch-AI
   ```

2. **Create a Virtual Environment (Recommended)**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On macOS/Linux
   venv\Scripts\activate  # On Windows
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up API Keys**
   - Create a `.env` file in the project root.
   - Add your API key for Google Generative AI:
     ```env
     GOOGLE_API_KEY=your_api_key_here
     ```

5. **Run the Application**
   ```bash
   streamlit run app.py
   ```

6. **Access the Web App**
   - Open `http://localhost:8501` in your browser.

## 📋 Requirements
- Python 3.10
- Streamlit
- PyPDF2
- python-dotenv
- Google Generative
---

⭐ **Star this repository** if you find it useful!
