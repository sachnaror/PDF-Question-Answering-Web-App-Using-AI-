from django.shortcuts import render

from .forms import PDFUploadForm
from .utils import ask_question, extract_text_from_pdf


def pdf_qa_view(request):
    if request.method == 'POST':
        form = PDFUploadForm(request.POST, request.FILES)
        if form.is_valid():
            pdf = form.cleaned_data['pdf']
            question = form.cleaned_data['question']
            text = extract_text_from_pdf(pdf)
            answer = ask_question(text, question)
            return render(request, 'qa_app/result.html', {'answer': answer})
    else:
        form = PDFUploadForm()
    return render(request, 'qa_app/upload.html', {'form': form})
