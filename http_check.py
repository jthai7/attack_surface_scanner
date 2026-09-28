import requests

# check if live subdomains serve a website
def check_http(hostname):
    for scheme in ["https://", "http://"]:
        try:
            r = requests.get(scheme + hostname, timeout=5)
            return scheme, r.status_code
        except requests.exceptions.RequestException:
            continue
    # if the ip resolves but has no website
    return None, None
