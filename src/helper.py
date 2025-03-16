from src import genai, pdf


#Get gemini Response
def get_gemini_response(input):
    model = genai.GenerativeModel("gemini-2.0-flash")
    response = model.generate_content(input)
    return response.text


#Extract text from a PDF file
def input_pdf_text(uploaded_file):
    reader = pdf.PdfReader(uploaded_file)
    text = ""
    for page_num in range(len(reader.pages)):
        page = reader.pages[page_num]
        text += str(page.extract_text())
    return text