# codes by vision
import ssl
import socket
from datetime import datetime, timezone
from cryptography import x509
from cryptography.hazmat.backends import default_backend

def get_ssl_info(domain):
    results = {
        "issuer": None,
        "valid_from": None,
        "valid_to": None,
        "expired": False,
        "days_to_expiry": None,
        "weak_tls": False
    }
    
    try:
        context = ssl.create_default_context()
        with socket.create_connection((domain, 443), timeout=5) as sock:
            with context.wrap_socket(sock, server_hostname=domain) as ssock:
                cert_bin = ssock.getpeercert(binary_form=True)
                cert = x509.load_der_x509_certificate(cert_bin, default_backend())
                
                results["issuer"] = cert.issuer.rfc4514_string()
                results["valid_from"] = cert.not_valid_before_utc.isoformat()
                results["valid_to"] = cert.not_valid_after_utc.isoformat()
                
                today = datetime.now(timezone.utc)
                results["expired"] = today > cert.not_valid_after_utc
                
                delta = cert.not_valid_after_utc - today
                results["days_to_expiry"] = delta.days
                
                cipher = ssock.cipher()
                if cipher and "TLSv1" in cipher[1]:
                    results["weak_tls"] = True
                    
        return results
    except Exception as e:
        return {"error": f"SSL Scan failed: {str(e)}"}

