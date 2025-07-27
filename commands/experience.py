import typer
from utils.github_api import GithubAPI
from rich import print
from utils.resume_io import save_resume, load_resume
from rich.console import Console
from rich.progress import track

console = Console()
github_api = GithubAPI()

def add_experience(
        username: str = typer.Argument(...),
        yes: bool = typer.Option(False, "--yes", "-y", help="Skip confirmation prompts")
        ):
    """Add key projects to resume.yaml"""

    repos = github_api.get_repos(username)

    if not repos:
        console.print("[red]❌ No repos found or GitHub error.[/red]")
        return

    try:
        resume = load_resume()
    except FileNotFoundError:
        console.print("[red]❌ No resume found. Run `init` first.[/red]")
        return

    for i, repo in enumerate(repos):
        if not yes:

            # Print repo details
            console.rule(f"[bold yellow]{i+1}. {repo.name}")

            console.print(f"[cyan]Name:[/] {repo.name}")
            console.print(f"[cyan]Description:[/] {repo.description or 'None'}")
            console.print(f"[cyan]Stars:[/] {repo.stargazers_count}")
            console.print(f"[cyan]Language:[/] {repo.language}")
            console.print(f"[cyan]URL:[/] {repo.html_url}")
            console.print()

            console.print(f"→ Add [bold green]{repo.name}[/bold green] to resume?")
            include = typer.confirm("Continue?", default=False)

            if not include:
                continue
            
            else:
                # Optional: Ask user to edit or accept the description
                description = typer.prompt("Custom description?", default=repo.description or "")

                # Add to experience
                resume["repos"].append({
                    "name":repo.name,
                    "description": description,
                    "language": repo.language,
                    "stars": repo.stargazers_count,
                    "forks_count": repo.forks_count,
                    "topics": repo.topics,
                    "html_url": repo.html_url,
                })
        else:
            # Automatically add without confirmation
            resume["repos"].append({
                "name": repo.name,
                "description": repo.description,
                "language": repo.language,
                "stars": repo.stargazers_count,
                "forks_count": repo.forks_count,
                "topics": repo.topics,
                "html_url": repo.html_url,
            })

    save_resume(resume)
    console.print("[green]✅ Updated resume.yaml with new key projects.[/]")