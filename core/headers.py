# codes by vision
import requests

def get_header_info(domain):
    results = {
        "headers": {},
        "missing_headers": [],
        "server": None,
        "tech": []
    }
    
    security_headers = [
        "Content-Security-Policy",
        "Strict-Transport-Security",
        "X-Frame-Options",
        "X-Content-Type-Options",
        "Referrer-Policy",
        "Permissions-Policy"
    ]
    
    try:
        url = f"https://{domain}"
        response = requests.get(url, timeout=10, allow_redirects=True)
        
        results["headers"] = dict(response.headers)
        results["server"] = response.headers.get("Server")
        
        for header in security_headers:
            if header not in response.headers:
                results["missing_headers"].append(header)
                
        x_powered_by = response.headers.get("X-Powered-By")
        if x_powered_by:
            results["tech"].append(x_powered_by)
            
        return results
    except Exception as e:
        return {"error": f"Header analysis failed: {str(e)}"}

