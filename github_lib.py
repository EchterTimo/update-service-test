from github import Github, Commit


def get_latest_version_name():
    g = Github()

    owner = 'EchterTimo'
    repo_name = 'update-service-test'

    repo = g.get_repo(f'{owner}/{repo_name}')
    latest_commit = repo.get_commits(sha='main')[0]

    latest_commit: Commit = repo.get_commits(sha='main')[0]
    latest_commit_sha = latest_commit.sha

    file_content = repo.get_contents(
        path='version.txt',
        ref=latest_commit_sha
    )
    version_content = file_content.decoded_content.decode('utf-8')

    return version_content
