import ssl
import certifi
import socket
from datetime import datetime

def get_cert_info(hostname, port=443):
    # set up standard secure TLS configuration
    context = ssl.create_default_context(cafile=certifi.where())
    try:
        # open raw TCP connection to hostname on port 443
        with socket.create_connection((hostname, port), timeout=5) as sock:
            # TLS handshake
            with context.wrap_socket(sock, server_hostname=hostname) as ssock:
                # get data from certificate
                cert = ssock.getpeercert()
                tls_version = ssock.version()

                expire_str = cert['notAfter']
                expire_date = datetime.strptime(expire_str, '%b %d %H:%M:%S %Y %Z')
                days_left = (expire_date - datetime.now()).days

                return {
                    "issuer": dict(x[0] for x in cert['issuer']),
                    "expires": expire_date,
                    "days_until_expiry": days_left,
                    "tls_version": tls_version,
                }
    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    cert_info = get_cert_info("google.com")
    print(cert_info)