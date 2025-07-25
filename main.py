import typer
from commands import init, experience, skills, render

app = typer.Typer()

app.command()(init.initialize_resume)
app.command()(experience.add_experience)
app.command()(skills.add_skills)
app.command()(render.generate_resume)

if __name__ == "__main__":
    app()
