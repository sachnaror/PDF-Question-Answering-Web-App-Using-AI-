import fitz  # PyMuPDF


def extract_text_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    text = ""
    for page in doc:
        text += page.get_text()
    return text

def ask_question(text, question):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"Answer the following question based on the content: {text}\n\nQuestion: {question}",
        max_tokens=150
    )
    return response.choices[0].text.strip()
