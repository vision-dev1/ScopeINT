# codes by vision
import whois
from datetime import datetime

def get_whois_info(domain):
    try:
        w = whois.whois(domain)
        
        creation_date = w.creation_date
        if isinstance(creation_date, list):
            creation_date = creation_date[0]
            
        domain_age = "N/A"
        if creation_date and isinstance(creation_date, datetime):
            today = datetime.now()
            age_delta = today - creation_date
            years = age_delta.days // 365
            months = (age_delta.days % 365) // 30
            domain_age = f"{years}y {months}m"

        privacy_protected = False
        whois_str = str(w).lower()
        privacy_keywords = ["privacy", "proxy", "redacted", "protection", "whoisguard", "contact privacy"]
        if any(keyword in whois_str for keyword in privacy_keywords):
            privacy_protected = True

        return {
            "registrar": w.registrar if w.registrar else "N/A",
            "creation_date": creation_date.isoformat() if creation_date and isinstance(creation_date, datetime) else "N/A",
            "expiry_date": w.expiration_date[0].isoformat() if isinstance(w.expiration_date, list) else (w.expiration_date.isoformat() if w.expiration_date and isinstance(w.expiration_date, datetime) else "N/A"),
            "domain_age": domain_age,
            "name_servers": w.name_servers if isinstance(w.name_servers, list) else [w.name_servers] if w.name_servers else [],
            "privacy_protected": privacy_protected
        }
    except Exception as e:
        return {"error": f"WHOIS Lookup failed: {str(e)}"}

