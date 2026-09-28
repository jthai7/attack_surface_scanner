import requests

# check the different subdomains
def get_subdomains(domain):
    url = f"https://crt.sh/?q=%25.{domain}&output=json"
    response = requests.get(url)

    # fallback for invalid JSON
    try:
        data = response.json()
    except requests.exceptions.JSONDecodeError:
        print(f"Warning: crt.sh returned invalid data for {domain} (status {response.status_code}). Try again.")

    # remove duplicates with sets
    subdomains = set()
    for entry in data:
        # separate multiple names separated by newlines
        names = entry['name_value'].split('\n')
        for name in names:
            subdomains.add(name.strip())

    return subdomains

if __name__ == '__main__':
    domain = "google.com"
    subs = get_subdomains(domain)
    print(f"Found {len(subs)} subdomains")
    for s in sorted (subs):
        print(f" {s}")