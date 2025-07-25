from dataclasses import dataclass, field
import httpx
class GithubAPI:
    __BASE_URL = "https://api.github.com"
    def __init__(self):
        pass

    def get_user(username: str):
        url = f"{GithubAPI.__BASE_URL}/users/{username}"

        try:
          response = httpx.get(url)
          response.raise_for_status()
        except httpx.HTTPStatusError as err:
            print(f"{err.response.status_code}: {err.response.text}")

    def get_repos(username: str):
        url = f"{GithubAPI.__BASE_URL}/users/{username}/repos"

        try:
          response = httpx.get(url)
          response.raise_for_status()
        except httpx.HTTPStatusError as err:
            print(f"{err.response.status_code}: {err.response.text}")

    def get_repo(username:str, repo: str):
        url = f"{GithubAPI.__BASE_URL}/repos/{username}/{repo}"

        try:
          response = httpx.get(url)
          response.raise_for_status()
        except httpx.HTTPStatusError as err:
            print(f"{err.response.status_code}: {err.response.text}")



@dataclass
class User:
    login: str
    id: int
    node_id: str
    avatar_url: str
    gravatar_id: str
    url: str
    html_url: str
    followers_url: str
    following_url: str
    gists_url: str
    starred_url: str
    subscriptions_url: str
    organizations_url: str
    repos_url: str
    events_url: str
    received_events_url: str
    type: str
    user_view_type: str
    site_admin: bool
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

@dataclass
class Repo:
    id: int
    node_id: str
    name: str
    full_name: str
    private: bool
    owner: User
    html_url: str
    description: str
    fork: bool
    url: str
    forks_url: str
    keys_url: str
    collaborators_url: str
    teams_url: str
    hooks_url: str
    issue_events_url: str
    events_url: str
    assignees_url: str
    branches_url: str
    tags_url: str
    blobs_url: str
    git_tags_url: str
    git_refs_url: str
    trees_url: str
    statuses_url: str
    languages_url: str
    stargazers_url: str
    contributors_url: str
    subscribers_url: str
    subscription_url: str
    commits_url: str
    git_commits_url: str
    comments_url: str
    issue_comment_url: str
    contents_url: str
    compare_url: str
    merges_url: str
    archive_url: str
    downloads_url: str
    issues_url: str
    pulls_url: str
    milestones_url: str
    notifications_url: str
    labels_url: str
    releases_url: str
    deployments_url: str
    created_at: str
    updated_at: str
    pushed_at: str
    git_url: str
    ssh_url: str
    clone_url: str
    svn_url: str
    homepage: str
    size: int
    stargazers_count: int
    watchers_count: int
    language: str
    has_issues: bool
    has_projects: bool
    has_downloads: bool
    has_wiki: bool
    has_pages: bool
    has_discussions: bool
    forks_count: int
    mirror_url: str | None
    archived: bool
    disabled: bool
    open_issues_count: int
    license: str | None
    allow_forking: bool
    is_template: bool
    web_commit_signoff_required: bool
    topics: list[str] = field(default_factory=list)
    visibility: str
    forks: int
    open_issues: int
    watchers: int
    default_branch: str
    temp_clone_token: str | None
    network_count: int
    subscribers_count: int