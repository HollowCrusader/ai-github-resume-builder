import typer
from utils.gemini_client import create_generator_from_env
from utils.resume_io import PDFWriter, load_resume
from rich.spinner import Spinner
from rich.console import Console

console = Console()

def generate_resume():
    """Generate a resume from the resume.yaml file and save it as a PDF."""


    """
    This function reads the resume.yaml file, generates the resume text using
    the configured AI model, and writes the output to a PDF file.
    """
    yaml_file = "resume.yaml"
    pdf_file = "resume.pdf"

    try:
        resume = load_resume()
        
    except FileNotFoundError:
        console.print("[red]❌ &#x26cxc No resume found. Please run `init` first.[/red]")
        return

    #Gemini's generator
    typer.echo("Initializing Gemini AI...")
    gen = create_generator_from_env()

    with console.status("[bold green]Generating resume...[/bold green]") as status:
        resume_text = gen.generate_resume(yaml_file)
    

    with console.status("[bold green]Writing to PDF...[/bold green]"):
        # Create a PDFWriter instance with a margin of 20mm
        writer = PDFWriter(margin_mm=20)
        writer.write(resume_text, pdf_file)
    
    console.print(f"[bold green]Resume generated successfully![/bold green] Saved to {pdf_file}")
    # Logic to read resume.yaml and generate the resume would go here