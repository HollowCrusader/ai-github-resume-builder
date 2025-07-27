from dataclasses import field
from tokenize import Ignore
import pydantic
import httpx
import hishel


# GitHub API wrapper class with caching and response modeling
class GithubAPI:
    __BASE_URL = "https://api.github.com"

    # Configure in-memory caching for repeated requests
    __storage = hishel.InMemoryStorage(capacity=30)
    __client = hishel.CacheClient(storage=__storage)

    def __init__(self):
        pass

    @classmethod
    def get_user(cls, username: str):
        """
        Fetches user profile data.
        Returns a validated User model or prints an error message.
        """
        url = f"{GithubAPI.__BASE_URL}/users/{username}"

        try:
            response = cls.__client.get(url)
            response.raise_for_status()
            user = User.model_validate(response.json())

            return user
        
        except pydantic.ValidationError as ve:
            print(f"Validation failed: {ve}")
        except httpx.HTTPStatusError as he:
            print(f"{he.response.status_code}: {he.response.text}")
        except Exception as err:
            print(f"Unexpected error: {err}")

    @classmethod
    def get_repos(cls, username: str):
        """
        Fetches a list of repositories for the given user, limited to 5 repos.
        Sorted by most recently pushed.
        Returns a list of validated Repo models.
        """
        url = f"{GithubAPI.__BASE_URL}/users/{username}/repos"

        try:
          response = cls.__client.get(url, params={"per_page": 5, "sort": "pushed", "direction": "desc"})
          response.raise_for_status()
          repos_json = response.json()
          repositories: list[Repo] = [Repo(**repo_data) for repo_data in repos_json]

          return repositories
        
        except pydantic.ValidationError as ve:
            print(f"Validation failed: {ve}")
        except httpx.HTTPStatusError as he:
            print(f"{he.response.status_code}: {he.response.text}")
        except Exception as err:
            print(f"Unexpected error: {err}")

    @classmethod
    def get_repo(cls, username: str, repo: str):
        """
        Fetches detailed information about a specific repository.
        Also retrieves and returns the languages used in the repo.
        Returns a tuple: (Repo model, dict of languages).
        """
        url = f"{GithubAPI.__BASE_URL}/repos/{username}/{repo}"

        try:
          response = cls.__client.get(url)
          response.raise_for_status()
          repository = Repo.model_validate(response.json())

          lang_response = cls.__client.get(repository.languages_url)
          response.raise_for_status()
          skills: dict[str, int] = lang_response.json()

          return repository, skills
        
        except pydantic.ValidationError as ve:
            print(f"Validation failed: {ve}")
        except httpx.HTTPStatusError as he:
            print(f"{he.response.status_code}: {he.response.text}")
        except Exception as err:
            print(f"Unexpected error: {err}")


# Pydantic model for GitHub user profile
class User(pydantic.BaseModel):
    login: str
    id: int
    name: str
    company: str | None
    blog: str
    location: str
    email: str | None
    hireable: str | None
    bio: str | None
    twitter_username: str | None
    public_repos: int
    public_gists: int
    followers: int
    following: int
    created_at: str
    updated_at: str

# Pydantic model for GitHub repository data
class Repo(pydantic.BaseModel):
    id: int
    name: str
    description: str | None
    html_url: str
    languages_url: str
    stargazers_count: int
    language: str | None
    forks_count: int
    topics: list[str] = field(default_factory=list)