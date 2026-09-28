from cert_inspect import get_cert_info
from risk_assessor import assess_risk
from security_header_check import check_security_headers
from subdomain_finder import get_subdomains
from dns_check import resolve_domain
from http_check import check_http
from report import write_report

domain = input("Enter your domain: ").strip().lower()
subs = get_subdomains(domain)

results = []
for sub in subs:
    ips = resolve_domain(sub)
    if not ips:
        continue
    print(f"Checking {sub}...")
    scheme, status = check_http(sub)
    cert_info = get_cert_info(sub) if scheme == "https://" else {}
    if scheme == "https://":
        header_result = check_security_headers(sub)
        missing_headers = header_result["missing"] if header_result else []
    else:
        missing_headers = []
    flags = assess_risk(cert_info, missing_headers) if cert_info else ["No HTTPS"]

    results.append({
        "subdomain": sub,
        "ip": ips,
        "status_code": status,
        "cert_expiry_days": cert_info.get("days_until_expiry"),
        "flags": flags
    })

write_report(results)