import streamlit as st
from pathlib import Path

# 1. Page Configuration
st.set_page_config(
    page_title="Iqra Gulzar | Digital CV",
    page_icon="💠",
    layout="centered"
)

# 2. Ultimate High-Visibility CSS
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@400;600;800&display=swap');
    
    .main { 
        background-color: #000000;
        background-image: 
            linear-gradient(rgba(0, 212, 255, 0.05) 1px, transparent 1px),
            linear-gradient(90deg, rgba(0, 212, 255, 0.05) 1px, transparent 1px);
        background-size: 50px 50px;
        position: relative;
        overflow: hidden;
        font-family: 'Outfit', sans-serif; 
    }
    
    /* Binary Rain Effect */
    .main::before {
        content: "0101011010101010101010101101010101101010101010101010110101010110101010101010101011010101";
        position: fixed;
        top: 0; left: 0; width: 100%; height: 100%;
        color: rgba(0, 212, 255, 0.03);
        font-family: monospace;
        font-size: 14px;
        line-height: 1;
        white-space: pre-wrap;
        animation: matrixRain 20s linear infinite;
        pointer-events: none;
        z-index: 0;
    }

    @keyframes matrixRain {
        from { transform: translateY(-100%); }
        to { transform: translateY(100%); }
    }
    
    .main::before {
        content: "";
        position: fixed;
        top: 0; left: 0; width: 100%; height: 100%;
        background: linear-gradient(0deg, transparent, rgba(0, 212, 255, 0.1), transparent);
        height: 100px;
        width: 100%;
        animation: dataStream 8s linear infinite;
        pointer-events: none;
        z-index: 0;
    }

    @keyframes dataStream {
        0% { transform: translateY(-100px); opacity: 0; }
        10% { opacity: 1; }
        90% { opacity: 1; }
        100% { transform: translateY(100vh); opacity: 0; }
    }

    @keyframes gradient {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }
    
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    h1, h2, h3, h4 { 
        color: #00d4ff !important; 
        font-weight: 800 !important; 
        text-shadow: 0 0 10px rgba(0, 212, 255, 0.5);
        letter-spacing: 2px;
        text-transform: uppercase;
    }
    
    p, li, span { color: #ffffff !important; font-size: 1.1rem; line-height: 1.6; }
    
    .cv-card {
        background: rgba(10, 10, 10, 0.9);
        border: 1px solid rgba(0, 212, 255, 0.3);
        border-left: 5px solid #00d4ff;
        border-radius: 0.5rem 1.5rem 1.5rem 0.5rem;
        padding: 2rem;
        margin-bottom: 2rem;
        box-shadow: 0 0 20px rgba(0, 212, 255, 0.1);
        transition: all 0.3s ease;
    }
    
    .cv-card:hover {
        background: rgba(20, 20, 20, 0.95);
        border-left-width: 10px;
        box-shadow: 0 0 30px rgba(0, 212, 255, 0.3);
    }
    
    .unified-badge {
        display: inline-block;
        background-color: #00d4ff;
        color: #000000 !important;
        padding: 0.35rem 0.8rem;
        border-radius: 0.4rem;
        font-size: 0.85rem;
        font-weight: 800;
        margin: 0.3rem;
        box-shadow: 0 0 10px rgba(0, 212, 255, 0.3);
        transition: all 0.3s ease;
    }
    
    .unified-badge:hover {
        transform: scale(1.1);
        background-color: #ffffff;
        box-shadow: 0 0 20px #00d4ff;
    }

    /* Clean static style for the image */
    img {
        border: 4px solid #00d4ff;
        border-radius: 50%;
        box-shadow: 0 0 30px rgba(0, 212, 255, 0.5);
    }
    .contact-link {
        color: #00d4ff !important;
        text-decoration: none;
        transition: all 0.3s ease;
    }
    
    .contact-link:hover {
        text-shadow: 0 0 10px #00d4ff;
        color: #ffffff !important;
    }
</style>
""", unsafe_allow_html=True)

# 3. Main Header
st.markdown('<div style="text-align: center;">', unsafe_allow_html=True)
img_path = r"D:\Documents\Image (3).jpeg"
if Path(img_path).exists():
    st.image(img_path, width=180)
elif Path("iqra_profile_pic_1778410587478.png").exists():
    st.image("iqra_profile_pic_1778410587478.png", width=180)
else:
    st.write("📷 Photo")
st.markdown(f"""
    <h1 style="font-size: 3.5rem; margin-top: 0; margin-bottom: 1rem;">Iqra Gulzar</h1>
    <p style="color: #00d4ff !important; font-weight: 700; margin-bottom: 2rem;">
        📍 Abu Dhabi, UAE  •  📱 <a href="https://wa.me/971506224979?text=Hello%20Iqra,%20I%20saw%20your%20portfolio%20and%20would%20like%20to%20connect." target="_blank" class="contact-link">+971 50 622 4979</a>  •  📧 <a href="https://mail.google.com/mail/?view=cm&fs=1&to=gulzariqra87@gmail.com&su=Inquiry%20regarding%20Portfolio%20-%20Iqra%20Gulzar" target="_blank" class="contact-link">gulzariqra87@gmail.com</a>  •  🔗 <a href="https://linkedin.com/in/iqra-gulzar-049a23209" target="_blank" class="contact-link">LinkedIn</a>
    </p>
</div>
""", unsafe_allow_html=True)

st.divider()

# 4. Content Sections
st.header("Professional Summary")
st.markdown("""
<div class="cv-card">
    Motivated IT professional and Support Engineer with expertise in ELV system design, pre-sales engineering, cybersecurity, and digital infrastructure. Experienced in preparing technical documentation, coordinating with stakeholders, and troubleshooting Windows and Linux environments. Currently pursuing MSc in Data Science and Artificial Intelligence with a strong interest in data-driven solutions and emerging technologies. Recognized for adaptability, communication skills, and collaborative teamwork.
</div>
""", unsafe_allow_html=True)

# Experience
st.header("Work Experience")
st.markdown("### Support Engineer – Syssense")
st.markdown("*Abu Dhabi, UAE | 2023 — 2025*")
st.markdown("""
<div class="cv-card">
<ul>
    <li>Designed and estimated ELV Extra Low Voltage systems including CCTV, Structured Cabling Systems, Access Control Systems, Background Music Systems, intercom systems, and automated gate barrier solutions.</li>
    <li>Prepared layout drawings, Bills of Quantities, technical submittals, and cost estimations for tenders and pre-sales activities.</li>
    <li>Coordinated with vendors, consultants, and clients to ensure compliance with project specifications and timely approvals.</li>
    <li>Managed Annual Maintenance Contract documentation and service reporting.</li>
    <li>Designed the company profile and developed the corporate website to enhance branding and digital presence.</li>
    <li>Installed, configured, and troubleshot Windows systems and IT infrastructure to ensure operational efficiency.</li>
</ul>
</div>
""", unsafe_allow_html=True)

# Job 2
st.markdown("### Cybersecurity Intern – Jamia Co-operative Bank")
st.markdown("*Delhi, India | 2022*")
st.markdown("""
<div class="cv-card">
<ul>
    <li>Identified potential system vulnerabilities and supported implementation of security controls.</li>
    <li>Assisted in maintaining secure network operations and system integrity.</li>
    <li>Contributed to strengthening digital infrastructure within a financial environment.</li>
</ul>
</div>
""", unsafe_allow_html=True)

# Education
st.header("Education")
st.markdown("""
<div class="cv-card">
    <p><strong>MSc Data Science & AI</strong> | Middlesex University Dubai (2025—Present)</p>
    <p><strong>B.Tech Information Systems</strong> | MAHE Dubai | GPA: 8.68/10</p>
</div>
""", unsafe_allow_html=True)

# Skills
st.header("Technical & Professional Skills")
all_skills = [
    "AWS", "BOQ Preparation", "Cloud Computing", "Computer Vision", "Cybersecurity", 
    "Data Analysis", "ELV System Design", "ETL Pipeline", "Google Cloud", "Java", 
    "Linux", "Microsoft Office", "NLP", "Networking", "NumPy", "Pandas", "Power BI", 
    "Pre-sales Engineering", "Predictive Modelling", "Python", "RAG System", 
    "RStudio", "SQL", "Scikit-Learn", "Statistical Analysis", "Tableau", 
    "Technical Submittals", "TensorFlow", "Vercel", "Machine Learning"
]
badge_html = '<div>'
for skill in sorted(all_skills):
    badge_html += f'<span class="unified-badge">{skill}</span>'
badge_html += '</div>'
st.markdown(badge_html, unsafe_allow_html=True)

# Certifications
st.header("Professional Certifications")
certs = [
    "IT Essentials", "Cybersecurity Essentials", 
    "Computer Networks", "IoT Connecting Things", 
    "Routing and Switching", "Enterprise Networking Security", 
    "Linux Administration System", "Database Management Essentials"
]
cert_html = '<div>'
for cert in certs:
    cert_html += f'<span class="unified-badge">{cert}</span>'
cert_html += '</div>'
st.markdown(cert_html, unsafe_allow_html=True)



st.markdown("<br><p style='text-align:center; color:#475569;'> 2026 Iqra Gulzar |  Portfolio</p>", unsafe_allow_html=True)
