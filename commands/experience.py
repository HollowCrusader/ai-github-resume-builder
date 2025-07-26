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

def get_profile(username: str= typer.Argument(...)):
    """Add the user's GitHub profile to resume.yaml..."""
    
    typer.echo("Fetching GitHub profile...")
    
    profile = github_api.get_user(username)

    resume = load_resume()
    if resume is None:
        typer.echo("No resume found. Please initialize your resume first.")
        return

    if profile is not None:
        print(profile.company)
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
        typer.echo("Failed to fetch profile.")
    else:
        typer.echo(f"Profile fetched:\n Name: {profile.name}\n Bio: {profile.bio}")