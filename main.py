import typer
from commands import init, experience, render

app = typer.Typer()

def run_all(username:str = typer.Argument(...),help="Run all commands"):
    """Run all commands in sequence."""
    init.init()
    experience.add_experience(username)
    experience.get_profile(username)
    render.generate_resume()

app.command()(init.init)
app.command()(experience.add_experience)
app.command()(experience.get_profile)
app.command()(render.generate_resume)
app.command()(run_all)


if __name__ == "__main__":
    app()
