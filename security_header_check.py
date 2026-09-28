import requests

def check_security_headers(hostname):
    try:
        # get request
        r = requests.get(f"https://{hostname}", timeout=5)
        headers = r.headers
        missing = []
        # check for and return any missing required headers
        for h in ["Strict-Transport-Security", "X-Frame-Options", "X-Content-Type-Options"]:
            if h not in headers:
                missing.append(h)
        # use final_url because of links redirecting
        return {"missing": missing, "final_url": r.url}
    except requests.exceptions.RequestException:
        return None

if __name__ == "__main__":
    result = check_security_headers("google.com")
    print(result)
