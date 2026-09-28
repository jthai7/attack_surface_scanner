import dns.resolver
from subdomain_finder import get_subdomains

# check if subdomains resolve
def resolve_domain(hostname):
    try:
        answers = dns.resolver.resolve(hostname, 'A')
        return [str(a) for a in answers]
    # if it does not resolve, then the log entry is dead
    except Exception:
        return None

if __name__ == "__main__":
    test_subs = get_subdomains("google.com")
    for sub in test_subs:
        ips = resolve_domain(sub)
        if ips:
            print(f"{sub} -> {ips}")
        else:
            print(f"{sub} -> DOES NOT RESOLVE")
