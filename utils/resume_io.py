from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.units import mm
from reportlab.lib.colors import black
import yaml
from pathlib import Path

class PDFWriter:
    """
    A refined PDF writer that mimics professional résumé formatting:
    - Uses Helvetica-Bold for headings
    - Section spacing, line height, and margin conventions aligned with real-world CVs
    """

    def __init__(self, margin_mm: float = 20.0):
        self.page_size = A4
        self.margin = margin_mm * mm

    def write(self, text: str, output_path: str):
        width, height = self.page_size
        c = canvas.Canvas(output_path, pagesize=A4)
        text_obj = c.beginText(self.margin, height - self.margin)
        text_obj.setFont("Helvetica", 10.5)
        text_obj.setLeading(13)  # line spacing

        lines = text.splitlines()

        for i, line in enumerate(lines):
            line = line.strip()

            if not line:
                text_obj.textLine("")
                continue

            if line.isupper() or line.endswith(":"):
                # Section header: bold
                c.drawText(text_obj)
                text_obj = c.beginText(self.margin, text_obj.getY() - 16)
                text_obj.setFont("Helvetica-Bold", 12)
                text_obj.setFillColor(black)
                text_obj.textLine(line.upper())
                text_obj.setFont("Helvetica", 10.5)
            elif line.startswith("- ") or line.startswith("\u2022"):
                text_obj.textLine(line)
            else:
                text_obj.textLine(line)

        c.drawText(text_obj)
        c.showPage()
        c.save()
        print(f"\u2705 PDF saved: {output_path}")

class IndentDumper(yaml.SafeDumper):
    """
    Custom YAML dumper to handle indentation and formatting.
    """
    def increase_indent(self, flow=False, indentless=False):
        return super(IndentDumper, self).increase_indent(flow, False)

def save_resume(data):
    """
    Save the resume data to a resume.yaml.
    :param data: Dictionary containing resume data.
    """
    with open("resume.yaml", "w", ) as f:
        yaml.dump(data, f, Dumper=IndentDumper, default_flow_style=False, sort_keys=False, allow_unicode=True, width=80)
    print("Resume data saved to resume.yaml")
    
def load_resume():
    """
    Load the resume data from resume.yaml.
    :return: Dictionary containing resume data.
    """
    with open("resume.yaml") as f:
        return yaml.safe_load(f)