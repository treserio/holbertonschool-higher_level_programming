#!/usr/bin/python3
'''Use github api to pull last 10 commits in repo by name'''


if __name__ == '__main__':
    import requests
    import sys

    repo = sys.argv[1]
    ownr = sys.argv[2]

    req = requests.get(
        'https://api.github.com/repos/{}/{}/commits'
        .format(ownr, repo)
    )
    jsonStr = req.json()

    for i in range(10):
        sha = jsonStr[i]['sha']
        own = jsonStr[i]['commit']['author']['name']
        print('{}: {}'.format(sha, own))
