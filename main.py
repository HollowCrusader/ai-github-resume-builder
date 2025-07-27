import typer
from commands import init, experience, render, profile

app = typer.Typer()

# Run all commands in sequence
def run_all(username:str = typer.Argument(...), yes: bool = typer.Option(False, "--yes", "-y", help="Skip confirmation prompts")):
    """Run all commands in sequence."""
    init.init(yes)
    experience.add_experience(username, yes=yes)
    profile.get_profile(username)
    render.generate_resume()

# Register commands
app.command()(init.init)
app.command()(experience.add_experience)
app.command()(profile.get_profile)
app.command()(render.generate_resume)
app.command()(run_all)

#Main entry point
if __name__ == "__main__":
    app()
