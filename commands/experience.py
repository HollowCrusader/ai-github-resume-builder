import typer
from utils.github_api import GithubAPI
github_api = GithubAPI()

def add_experience():
    """Add an experience entry to the resume.yaml file."""
    
    typer.echo("Adding experience to resume.yaml...")
    # Logic to add experience to resume.yaml would go here

def get_profile(username: str= typer.Argument(..., help="GitHub username to fetch profile")):
    """Fetch the user's GitHub profile."""
    
    typer.echo("Fetching GitHub profile...")
    
    profile = github_api.get_user(username)
    
    if not profile:
        typer.echo("Failed to fetch profile.")
    else:
        typer.echo(f"Profile fetched:\n Name: {profile['name']}\n Bio: {profile['bio']}")