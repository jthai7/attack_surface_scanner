from cert_inspect import get_cert_info
from security_header_check import check_security_headers

def assess_risk(cert_info, missing_headers):
    flags = []
    if cert_info.get("days_until_expiry", 999) < 30:
        flags.append("Certificate expiring soon")
    if cert_info.get("tls_version") in ["TLSv1.1", "TLSv1.2"]:
        flags.append("Weak/deprecated TLS version")
    if missing_headers:
        flags.append(f"Missing security headers: {', '.join(missing_headers)}")
    if flags:
        return flags
    else:
        return ["No issues found"]

if __name__ == "__main__":
    domain = "google.com"
    cert_info = get_cert_info(domain)
    header_result = check_security_headers(domain)
    missing_headers = header_result["missing"]
    flags = assess_risk(cert_info, missing_headers)
    print(flags)