import typer
from utils.gemini_client import create_generator_from_env
from utils.resume_io import PDFWriter

def generate_resume():
    """Generate a resume from the resume.yaml file."""

    yaml_file = "resume.yaml"
    pdf_file = "resume.pdf"

    gen = create_generator_from_env()
    resume_text = gen.generate_resume(yaml_file)

    writer = PDFWriter(margin_mm=20)
    writer.write(resume_text, pdf_file)
    
    typer.echo("Generating resume from resume.yaml...")
    # Logic to read resume.yaml and generate the resume would go here