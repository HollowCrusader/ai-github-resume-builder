import yaml
import typer
from pathlib import Path


def init(yes: bool = typer.Option(False, "--yes", "-y", help="Skip confirmation prompts")):
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

    # Check if resume.yaml already exists
    path = Path("resume.yaml")
    if path.exists():
        # If it exists and user wants to skip confirmation
        if not yes:
            # Ask user if they want to overwrite
            overwrite = typer.confirm("resume.yaml already exists. Do you want to overwrite it?")
            if overwrite:
                with open(path, "w") as file:
                    yaml.dump(base, file, sort_keys=False)
                    typer.echo("resume.yaml has been overwritten.")
            else:
                typer.echo("Skipping initialization. Existing resume.yaml will not be modified.")
                return
        else:
            # yaml.dump will overwrite the file without confirmation
            with open(path, "w") as file:
                        yaml.dump(base, file, sort_keys=False)
                        typer.echo("resume.yaml has been overwritten.")
    else:
        # If it doesn't exist, create a new file
        with open(path, "w") as file:
            yaml.dump(base, file, sort_keys=False)

            typer.echo("Generating an empty resume.yaml file...")