from github_api import GithubAPI, Repo
def test():
    githubapi = GithubAPI()
    #print(githubapi.get_user("malwani9"))
    #print(githubapi.get_repos("malwani9"))
    repo, skills =  githubapi.get_repo("malwani9", "static-site-generator")
    print(repo)

if __name__ == "__main__":
    test()