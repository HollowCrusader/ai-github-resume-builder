import typer
from utils.github_api import GithubAPI
from rich import print
from utils.resume_io import save_resume, load_resume
from rich.console import Console
github_api = GithubAPI()

console = Console()

def get_profile(username: str= typer.Argument(...),
                yes: bool = typer.Option(False, "--yes", "-y", help="Skip confirmation prompts")
            ):
    """Add the user's GitHub profile to resume.yaml..."""
    
    typer.echo("Fetching GitHub profile...")
    
    profile = github_api.get_user(username)

    resume = load_resume()
    if resume is None:
        typer.echo("No resume found. Please initialize your resume first.")
        return
    
    with console.status("[bold green]Adding profile to resume...[/bold green]"):
        
        if profile is not None:
            
            resume['login'] = profile.login
            resume["name"] = profile.name
            resume["bio"] = profile.bio
            resume["email"] = profile.email
            resume["location"] = profile.location
            resume["blog"] = profile.blog
            resume["hireable"] = profile.hireable
            resume["twitter_username"] = profile.twitter_username
            resume["company"] = profile.company
            resume["public_repos"] = profile.public_repos
            resume["public_gists"] = profile.public_gists
            resume["followers"] = profile.followers
            resume["following"] = profile.following
            resume["created_at"] = profile.created_at
            resume["updated_at"] = profile.updated_at
            
        save_resume(resume)


        if not profile:
            console.print("[bold red]Failed to fetch profile.[/bold red]")
        else:
            console.print(f"Profile fetched:\n[bold blue]Name:[/bold blue] [bold green]{profile.name}[/bold green]\n[bold blue]Bio:[/bold blue] [bold green]{profile.bio}[/bold green]\n[bold blue]Company:[/bold blue] [bold green]{profile.company}[/bold green]")