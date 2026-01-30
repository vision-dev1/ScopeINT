# codes by vision
import dns.resolver
import requests
import json

def get_dns_info(domain):
    results = {
        "records": {},
        "security": {
            "spf": None,
            "dmarc": None
        },
        "subdomains": []
    }
    
    record_types = ['A', 'AAAA', 'MX', 'TXT', 'NS']
    
    for record in record_types:
        try:
            answers = dns.resolver.resolve(domain, record)
            results["records"][record] = [str(rdata) for rdata in answers]
        except Exception:
            results["records"][record] = []

    for txt in results["records"].get("TXT", []):
        if "v=spf1" in txt.lower():
            results["security"]["spf"] = txt
            break
            
    try:
        dmarc_answers = dns.resolver.resolve(f"_dmarc.{domain}", "TXT")
        for rdata in dmarc_answers:
            if "v=DMARC1" in str(rdata):
                results["security"]["dmarc"] = str(rdata)
                break
    except Exception:
        pass

    try:
        url = f"https://crt.sh/?q=%.{domain}&output=json"
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            data = response.json()
            subdomains = set()
            for entry in data:
                name_value = entry.get("name_value", "")
                for sub in name_value.split("\n"):
                    if not sub.startswith("*."):
                        subdomains.add(sub.strip())
            results["subdomains"] = sorted(list(subdomains))[:50]
    except Exception:
        pass

    return results

