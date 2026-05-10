import streamlit as st
from pathlib import Path

# --- PAGE CONFIG ---
st.set_page_config(
    page_title="Iqra Gulzar | AI Portfolio",
    page_icon="🤖",
    layout="centered"
)

# --- MASTERPIECE STYLING (Neural AI Dashboard) ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@400;600;800&display=swap');
    
    /* 1. Futuristic AI Background */
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
    
    /* Data Stream Effect */
    .main::before {
        content: "";
        position: fixed;
        top: 0; left: 0; width: 100%; height: 100%;
        background: linear-gradient(0deg, transparent, rgba(0, 212, 255, 0.1), transparent);
        height: 150px;
        width: 100%;
        animation: dataFlow 10s linear infinite;
        pointer-events: none;
        z-index: 0;
    }

    @keyframes dataFlow {
        0% { transform: translateY(-150px); opacity: 0; }
        10% { opacity: 1; }
        90% { opacity: 1; }
        100% { transform: translateY(100vh); opacity: 0; }
    }
    
    /* 2. Hide Streamlit Branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* 3. Typography */
    h1, h2, h3 { 
        color: #00d4ff !important; 
        font-weight: 800 !important; 
        text-shadow: 0 0 10px rgba(0, 212, 255, 0.5);
        letter-spacing: 1px;
        text-transform: uppercase;
        margin-top: 2rem !important;
    }
    
    p, li, span { color: #ffffff !important; font-size: 1.1rem; line-height: 1.6; }
    
    /* 4. Neural Dashboard Cards */
    .cv-card {
        background: rgba(10, 10, 10, 0.95);
        border: 1px solid rgba(0, 212, 255, 0.2);
        border-left: 5px solid #00d4ff;
        border-radius: 0.5rem 1.5rem 1.5rem 0.5rem;
        padding: 2rem;
        margin-bottom: 2rem;
        box-shadow: 0 0 25px rgba(0, 212, 255, 0.05);
        transition: all 0.3s ease-in-out;
    }
    
    .cv-card:hover {
        background: rgba(20, 20, 20, 0.98);
        border-left-width: 12px;
        box-shadow: 0 0 40px rgba(0, 212, 255, 0.25);
        transform: scale(1.01);
    }
    
    /* 5. Glowing Technical Badges */
    .unified-badge {
        display: inline-block;
        background-color: #00d4ff;
        color: #000000 !important;
        padding: 0.4rem 1rem;
        border-radius: 0.5rem;
        font-size: 0.9rem;
        font-weight: 800;
        margin: 0.4rem;
        box-shadow: 0 0 15px rgba(0, 212, 255, 0.4);
        transition: all 0.3s ease;
    }
    
    .unified-badge:hover {
        transform: scale(1.15) rotate(1deg);
        background-color: #ffffff;
        box-shadow: 0 0 25px #00d4ff;
    }

    /* 6. Contact Hub Styling */
    .contact-link {
        color: #00d4ff !important;
        text-decoration: none;
        transition: all 0.3s ease;
        font-weight: 700;
    }
    
    .contact-link:hover {
        text-shadow: 0 0 15px #00d4ff;
        color: #ffffff !important;
    }

    /* 7. Profile Image Masterpiece */
    .stImage img {
        border: 4px solid #00d4ff;
        border-radius: 15px;
        box-shadow: 0 0 40px rgba(0, 212, 255, 0.6);
        transition: all 0.5s ease;
    }
</style>
""", unsafe_allow_html=True)

# --- HEADER SECTION (Screenshot Fidelity) ---
col_img, col_info = st.columns([1, 2])

with col_img:
    if Path("profile.jpg").exists():
        st.image("profile.jpg", width=220)
    else:
        st.write("📷 Photo")

st.markdown('<h1>IQRA GULZAR</h1>', unsafe_allow_html=True)

st.markdown(f"""
    <p style="font-size: 1.15rem; margin-bottom: 2.5rem;">
        📍 Abu Dhabi, UAE  •  
        📱 <a href="https://wa.me/971506224979?text=Hello%20Iqra,%20I%20saw%20your%20portfolio%20and%20would%20like%20to%20connect." target="_blank" class="contact-link">+971 50 622 4979</a>  •  
        📧 <a href="https://mail.google.com/mail/?view=cm&fs=1&to=gulzariqra87@gmail.com&su=Inquiry%20regarding%20Portfolio%20-%20Iqra%20Gulzar" target="_blank" class="contact-link">gulzariqra87@gmail.com</a>  •  
        🔗 <a href="https://linkedin.com/in/iqra-gulzar-049a23209" target="_blank" class="contact-link">LinkedIn</a>
    </p>
""", unsafe_allow_html=True)

st.divider()

# --- CONTENT SECTIONS ---
st.header("Professional Summary")
st.markdown("""
<div class="cv-card">
    Motivated IT professional and Support Engineer with expertise in ELV system design, pre-sales engineering, cybersecurity, and digital infrastructure. Experienced in preparing technical documentation, coordinating with stakeholders, and troubleshooting Windows and Linux environments. Currently pursuing MSc in Data Science and Artificial Intelligence with a strong interest in data-driven solutions and emerging technologies. Recognized for adaptability, communication skills, and collaborative teamwork.
</div>
""", unsafe_allow_html=True)

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

st.header("Education")
st.markdown("""
<div class="cv-card">
    <p><strong>MSc Data Science & AI</strong> | Middlesex University Dubai (2025—Present)</p>
    <p><strong>B.Tech Information Systems</strong> | MAHE Dubai | GPA: 8.68/10</p>
</div>
""", unsafe_allow_html=True)

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

st.markdown("<br><p style='text-align:center; color:#475569;'>© 2026 Iqra Gulzar | Portfolio</p>", unsafe_allow_html=True)
