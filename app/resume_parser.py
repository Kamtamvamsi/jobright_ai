import fitz

# =========================================
# Extract Text from PDF
# =========================================

def extract_text_from_pdf(pdf_file):

    text = ""

    try:

        # Open PDF
        pdf_document = fitz.open(
            stream=pdf_file.read(),
            filetype="pdf"
        )

        # Read all pages
        for page in pdf_document:

            text += page.get_text()

        pdf_document.close()

        return text

    except Exception as e:

        return f"Error reading PDF: {str(e)}"