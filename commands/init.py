import yaml
import typer
from pathlib import Path


def init():
    """Initialize an empty resume.yaml file."""
    base = {
        "login": "",
        "name": "",
        "company":"",
        "blog":"",
        "email": "",
        "hireable": False,
        "bio":"",
        "location": "",
        "twitter_username":"",
        "followers": 0,
        "following": 0,
        "created_at": "",
        "updated_at": "",
        "public_repos": 0,
        "public_gists": 0,
        "repos":[],
    }

    path = Path("resume.yaml")
    if path.exists():
        typer.echo("resume.yaml already exists. Skipping initialization.")
    else:
        with open(path, "w") as file:
            yaml.dump(base, file, sort_keys=False)

            typer.echo("Generating an empty resume.yaml file...")