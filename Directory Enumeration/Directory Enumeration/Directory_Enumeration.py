import requests,sys
# usage : wordlist + url
file = sys.argv[1]
alll = open(file).read()
words = alll.splitlines()
for word in words:
    dirr = f"http://{sys.argv[2]}/{word}"
    res = requests.get(dirr)
    if res.status_code==404:
        pass
    else:
        print("Directory found!: ", dirr)
