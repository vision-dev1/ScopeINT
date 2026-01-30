# codes by vision
import json
import os
from datetime import datetime
from fpdf import FPDF
from utils.banner import get_text_banner

class ScopeReport(FPDF):
    def header(self):
        self.set_font('Courier', 'B', 8)
        self.set_text_color(100, 100, 100)
        self.cell(0, 10, 'ScopeINT OSINT Report', 0, 0, 'R')
        self.ln(10)

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'C')

def save_json_report(results, output_dir="reports"):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    filename = f"scopeint_{results['domain']}.json"
    path = os.path.join(output_dir, filename)
    
    report_data = {
        "tool_name": "ScopeINT",
        "scan_time": datetime.now().isoformat(),
        "domain": results["domain"],
        "risk_score": results["risk_score"],
        "results": results
    }
    
    with open(path, "w") as f:
        json.dump(report_data, f, indent=4)
    return path

def save_pdf_report(results, output_dir="reports"):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        
    filename = f"scopeint_{results['domain']}.pdf"
    path = os.path.join(output_dir, filename)
    
    pdf = ScopeReport()
    pdf.set_margins(15, 15, 15)
    pdf.add_page()
    
    pdf.set_font("Courier", 'B', 24)
    pdf.cell(0, 15, "ScopeINT", ln=True, align='C')
    pdf.set_font("Courier", 'I', 12)
    pdf.cell(0, 10, "Domain Intelligence & OSINT Framework", ln=True, align='C')
    pdf.set_font("Courier", size=10)
    pdf.cell(0, 10, "GitHub: vision-dev1", ln=True, align='C')
    pdf.ln(10)
    
    pdf.set_font("Arial", 'B', 16)
    pdf.cell(0, 10, f"Domain Scan: {results['domain']}", ln=True)
    pdf.set_font("Arial", size=10)
    pdf.cell(0, 10, f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}", ln=True)
    pdf.ln(5)
    
    pdf.set_font("Arial", 'B', 14)
    risk = results["risk_score"]
    pdf.set_fill_color(240, 240, 240)
    pdf.cell(0, 10, f"Risk Score: {risk['score']}/100 - {risk['level']}", ln=True, fill=True)
    pdf.set_font("Arial", size=10)
    for exp in risk["explanations"]:
        pdf.multi_cell(180, 5, f"- {exp}")
    pdf.ln(10)
    
    sections = [
        ("WHOIS Intelligence", results["whois"]),
        ("DNS Records Summary", {k: ", ".join(v[:3]) for k, v in results["dns"]["records"].items() if v}),
        ("Security Configuration", results["dns"]["security"]),
        ("SSL/TLS Analysis", results["ssl"]),
        ("HTTP Header Analysis", {"Server": results["headers"].get("Server"), "Missing": results["headers"].get("missing_headers")})
    ]
    
    for title, data in sections:
        pdf.set_font("Arial", 'B', 12)
        pdf.set_fill_color(230, 240, 255)
        pdf.cell(0, 8, title, ln=True, fill=True)
        pdf.set_font("Courier", size=8)
        
        if isinstance(data, dict):
            for k, v in data.items():
                value_str = str(v)
                if len(value_str) > 100:
                    value_str = value_str[:97] + "..."
                pdf.multi_cell(180, 5, f"{k}: {value_str}")
        elif isinstance(data, list):
            for item in data:
                pdf.multi_cell(180, 5, f"- {item}")
        else:
            pdf.multi_cell(180, 5, str(data))
        pdf.ln(3)
        
    pdf.output(path)
    return path

