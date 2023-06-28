from docx import Document
import re


def replace_parameters(doc, parameters):
    for paragraph in doc.paragraphs:
        for run in paragraph.runs:
            text = run.text
            for param, value in parameters.items():
                pattern = r"\$\{" + re.escape(param) + r"\}"
                text = re.sub(pattern, value, text)
            run.text = text


def process_docx_file(input_file, output_file, **parameters):
    doc = Document(input_file)
    replace_parameters(doc, parameters)
    doc.save(output_file)
