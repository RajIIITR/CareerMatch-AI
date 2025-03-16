# Import all necessary libraries here
import streamlit as st
import google.generativeai as genai
import PyPDF2 as pdf
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()
GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')

# Configure the Gemini API
genai.configure(api_key=GOOGLE_API_KEY)