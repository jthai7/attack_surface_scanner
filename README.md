# External Attack Surface Scanner

Given a domain, the scanner discovers its subdomains and determines whether each one is still active, whether the TLS configuration is healthy, and flags any security concerns worth investigating.

## Description
The external attack surface scanner takes a domain and discovers subdomains using certificate transparency logs. Next, the scanner tests which of the subdomains resolve to an IP address and which serve a webpage by sending requests over HTTP/HTTPS. For the live subdomains, the certificate information and security header information is pulled. The report includes each subdomain's IP address, HTTP status, and certificate expiration. The report flags subdomains that lack HTTPS, have a certificate nearing expiration, use a weak or deprecated TLS version, or are missing security headers.

## Installation
Developed and tested on Python 3.12.

1. Clone the repository:
```bash
   git clone https://github.com/jthai7/attack_surface_scanner.git
   cd attack_surface_scanner
```

2. (Recommended) Create and activate a virtual environment:
```bash
   python3 -m venv .venv
   source .venv/bin/activate      # macOS/Linux
   .venv\Scripts\activate         # Windows
```

3. Install dependencies:
```bash
   pip install -r requirements.txt
```

## Usage

Run the scanner from the project root:

```bash
python main.py
```

When prompted, enter a root domain (for example `example.com`), without `https://` or `www.`:

```
Enter your domain: example.com
```

The scanner discovers subdomains, checks each one, and writes the results to `report.md` in the project folder. Each run overwrites the previous report, so rename or move a report you want to keep.

A full scan can take several minutes, since each subdomain may involve multiple network requests. If the certificate transparency lookup returns an error (crt.sh is occasionally unavailable), wait a moment and run it again.

## Example Output
A snippet of a scan of google.com on September 17, 2026, trimmed to two entries.

> ## Attack Surface Report
>
> ## ecc-test.sandbox.google.com
> - IP: ['192.178.164.81']
> - HTTP Status: 200
> - Cert expires in: 70 days
> - Flags: Missing security headers: Strict-Transport-Security, X-Frame-Options
>
> ## google.com.by
> - IP: ['142.251.218.196']
> - HTTP Status: 200
> - Cert expires in: 45 days 
> - Flags: Missing security headers: Strict-Transport-Security, X-Content-Type-Options
