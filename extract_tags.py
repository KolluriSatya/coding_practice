import os
import requests

def get_commit_tags(commit_sha):
    repo = os.environ['GITHUB_REPOSITORY']
    headers = {
        'Authorization': f'token {os.environ["GITHUB_TOKEN"]}',
        'Accept': 'application/vnd.github.v3+json'
    }
    response = requests.get(f'https://api.github.com/repos/{repo}/commits/{commit_sha}/tags', headers=headers)
    if response.status_code == 200:
        tags = response.json()
        return [tag['name'] for tag in tags]
    return None

def get_all_commits():
    repo = os.environ['GITHUB_REPOSITORY']
    headers = {
        'Authorization': f'token {os.environ["GITHUB_TOKEN"]}',
        'Accept': 'application/vnd.github.v3+json'
    }
    response = requests.get(f'https://api.github.com/repos/{repo}/commits', headers=headers)
    if response.status_code == 200:
        commits = response.json()
        return [commit['sha'] for commit in commits]
    return None

commits = get_all_commits()
if commits:
    for commit_sha in commits:
        tags = get_commit_tags(commit_sha)
        if tags:
            print(f"Commit {commit_sha} has tags: {', '.join(tags)}")
        else:
            print(f"No tags found for commit {commit_sha}")
else:
    print("Failed to fetch commit details.")
