from gemini_client import create_generator_from_env
from resume_io import PDFWriter

if __name__ == "__main__":
    yaml_file = "data.yml"
    pdf_file = "resume.pdf"

    # 1. Generate résumé text
    gen = create_generator_from_env()
    resume_text = gen.generate_resume(yaml_file)

    writer = PDFWriter(margin_mm=20)
    writer.write(resume_text, pdf_file)
