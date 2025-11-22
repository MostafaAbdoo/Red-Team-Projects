import requests,sys
file = sys.argv[1]
one = open(file).read()
subs = one.splitlines()
for sub in subs:
    sub_domain=f"http://{sub}.{sys.argv[2]}"
    try:
        requests.get(sub_domain)
    except requests.ConnectionError:
        pass
    else:
        print("Valid Subdomain: ", sub_domain)
