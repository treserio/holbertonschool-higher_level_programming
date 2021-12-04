#!/usr/bin/python3
'''Use github api to pull last 10 commits in repo by name'''


if __name__ == '__main__':
    import requests
    import sys

    repo = sys.argv[1]
    ownr = sys.argv[2]

    def time_sort(L):
        t_in = L['commit']['author']['date']
        date = t_in.split('T')[0]
        date_t = t_in.split('T')[1]

        yr = date.split('-')[0]
        mon = date.split('-')[1]
        day = date.split('-')[2]

        hr = date_t.split(':')[0]
        mn = date_t.split(':')[1]
        sc = date_t.split(':')[2][:-1]

        return yr, mon, day, hr, mn, sc

    req = requests.get(
        'https://api.github.com/repos/{}/{}/commits'
        .format(ownr, repo)
    )
    jsonStr = req.json()
    print("\n".join('{}: {}'.format(i['sha'], i['commit']['author']['name'])
                    for i in sorted(jsonStr, key=time_sort)[:10]))
