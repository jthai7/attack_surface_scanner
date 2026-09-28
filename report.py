def write_report(results, filename="report.md"):
    with open(filename, "w") as f:
        f.write("# Attack Surface Report\n\n")
        for result in results:
            f.write(f"## {result['subdomain']}\n")
            f.write(f"- IP: {result['ip']}\n")
            f.write(f"- HTTP Status: {result['status_code']}\n")
            expiry = result['cert_expiry_days']
            # if HTTP Status: None, there will be no expiry data
            expiry_output = f"{expiry} days" if expiry is not None else "N/A (no HTTPS)"
            f.write(f"- Cert expires in: {expiry_output} \n")
            f.write(f"- Flags: {', '.join(result['flags'])}\n\n")