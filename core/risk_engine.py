# codes by vision
from datetime import datetime

def calculate_risk(scan_data):
    score = 0
    explanations = []
    
    whois = scan_data.get("whois", {})
    creation_date_str = whois.get("creation_date")
    if creation_date_str:
        creation_date = datetime.fromisoformat(creation_date_str)
        age_days = (datetime.now() - creation_date.replace(tzinfo=None)).days
        if age_days < 30:
            score += 40
            explanations.append("Domain is very new (< 30 days), high risk of phishing.")
        elif age_days < 180:
            score += 20
            explanations.append("Domain is relatively new (< 6 months).")
    else:
        score += 15
        explanations.append("Could not determine domain age.")

    dns_data = scan_data.get("dns", {})
    security = dns_data.get("security", {})
    if not security.get("spf"):
        score += 15
        explanations.append("Missing SPF record: Risk of email spoofing.")
    if not security.get("dmarc"):
        score += 15
        explanations.append("Missing DMARC record: Risk of unauthorized email usage.")

    headers = scan_data.get("headers", {})
    missing = headers.get("missing_headers", [])
    if "Content-Security-Policy" in missing:
        score += 10
        explanations.append("Missing CSP: Risk of XSS and content injection.")
    if "Strict-Transport-Security" in missing:
        score += 10
        explanations.append("Missing HSTS: Risk of Man-in-the-Middle attacks over HTTP.")
    if "X-Frame-Options" in missing:
        score += 5
        explanations.append("Missing X-Frame-Options: Risk of Clickjacking.")

    ssl_data = scan_data.get("ssl", {})
    if ssl_data.get("expired"):
        score += 30
        explanations.append("SSL Certificate is expired.")
    if ssl_data.get("weak_tls"):
        score += 20
        explanations.append("Weak TLS versions detected (TLS 1.0/1.1).")

    score = min(score, 100)
    
    level = "Low"
    if score > 70:
        level = "High"
    elif score > 30:
        level = "Medium"
        
    return {
        "score": score,
        "level": level,
        "explanations": explanations
    }

