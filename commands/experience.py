import typer
from utils.github_api import GithubAPI
from rich import print
from utils.resume_io import save_resume, load_resume
github_api = GithubAPI()

def add_experience(username: str = typer.Argument(...)):
    """Add an experience entry to the resume.yaml file."""

    skill_list = []
    skill_weights = {}
    repos = github_api.get_repos(username)

    print(repos)

    resume = load_resume()

    if resume is None:
        typer.echo("No resume found. Please initialize your resume first.")
        return
    
    if not isinstance(resume.get("repos"), list):

        resume["repos"] = []

    if repos is not None:
        for repo in repos:
            resume["repos"].append({
                "name":repo.name,
                "description": repo.description,
                "language": repo.language,
                "stars": repo.stargazers_count,
                "forks_count": repo.forks_count,
                "topics": repo.topics,
                "html_url": repo.html_url,
            })

    save_resume(resume)

    typer.echo("Adding experience to resume.yaml...")
    # Logic to add experience to resume.yaml would go here