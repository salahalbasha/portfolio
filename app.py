from pathlib import Path

import streamlit as st
from PIL import Image

# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV.pdf"
profile_pic = current_dir / "assets" / "profile-pic.png"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Salah Al-Basha"
PAGE_ICON = ":wave:"
NAME = "Salah Al-Basha"
DESCRIPTION = """
Data Analyst | Assisting enterprises by supporting data-driven decision-making.

"""
EMAIL = "salahalbasha12@yahoo.com"
SOCIAL_MEDIA = {
    "LinkedIn": "https://linkedin.com/in/salahalbasha/",
    "GitHub": "https://github.com/salahalbasha/",
}

PROJECTS = {
    "🏆 Pima Indians Diabetes Analysis": {
        "link": "https://salahalbasha-pima-app-yo940c.streamlit.app/",
        "skills_tools": "Python (Pandas, Numpy, Matplotlib, Seaborn), Machine Learning, Data Analysis",
    },
    "🏆 Netflix Movie Recommendation": {
        "link": "https://salahalbasha-movie-app-c5pu9r.streamlit.app/",
        "skills_tools": "Collaborative filtering, Matrix factorization, Recommendation systems",
    },
    "🏆 Analysis of United States Accidents": {
        "link": "https://salahalbasha-accidents-accidents-8nnvpw.streamlit.app/",
        "skills_tools": "Exploratory Data Analysis, BigData Cleaning, Data Visualization",
    },
}

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)


# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    # Add the 'square-link' class to LinkedIn and GitHub links
    if platform == "LinkedIn" or platform == "GitHub":
        cols[index].write(f"<a class='square-link' href='{link}'>{platform}</a>", unsafe_allow_html=True)
    else:
        cols[index].write(f"[{platform}]({link})")


# --- SKILLS ---
st.write('\n')
st.subheader("Hard Skills")
st.write("---")
st.write(
    """
- 🧑🏻‍💻 Programming: Python (Pandas, Numpy, Matplotlib, Seaborn), SQL
- 📊 BI & Analytics tools: Power BI, Tableau, MS Excel
- 📚 Modeling: Logistic regression, linear regression, decition trees
- 💻 Web Development: HTML, CSS
- ⚛️ Version Control: Git, GitHub
- 📽 PM Frameworks: Scrum, Confluence, Trello
- 👷🏻‍♂️ Technical/SaaS: Slack, Markdown, Prompt Engineering
- 📋 Digital Products/Apps: UI/UX, Figma, Canva
"""
)

# --- EDUCATION AND QUALIFICATIONS---
st.write('\n')
st.subheader("Education & Qulifications")
st.write("---")
st.write(
    """
- ✔️ Bachelor's of Applied Mathematics at Carleton
- ✔️ Data Science and Machine Learning Bootcamp at MIT
- ✔️ 2 Years of expereince extracting actionable insights from data
- ✔️ Strong hands-on experience and knowledge in Python, SQL and Excel
- ✔️ Good understanding of statistical principles and their respective applications
"""
)


# Projects & Accomplishments
st.write('\n')
st.subheader("Projects & Accomplishments")
st.write("---")
for project, details in PROJECTS.items():
    st.write(f"[{project}]({details['link']})")
    st.write(f"Skills & Tools: {details['skills_tools']}")
    st.write("---")

# --- WORK HISTORY ---
st.write('\n')
st.subheader("Work History")
st.write("---")

# --- JOB 1
st.write("🚧", "**Technical Support Analyst | Shopify**")
st.write(
    """
- ► Conducted in-depth technical troubleshooting using various tools and technologies to resolve complex merchant issues, while also measuring the KPIs of merchant satisfaction and issue resolution time using BigData analysis techniques.
- ► Analyzed merchant data and provided customized solutions to improve metrics such as conversion rates, customer satisfaction, and average order value using artificial intelligence (AI) and deep learning algorithms.
- ► Developed expertise in Shopify's products and services to provide expert advice to merchants, while also leveraging data analytics to suggest improvements to existing products and services.
- ► Collaborated with cross-functional teams on projects such as Bridge the Gap, the Next Pilot, and the US Capital, using data analysis and reporting to support project goals and track the success of each initiative.
"""
)

# --- JOB 2
st.write('\n')
st.write("🚧", "**Fitness Sales Analyst | GoodLife Fitness**")
st.write(
    """
- ► Analyzed customer data to identify trends and insights that informed sales strategies, including the measurement of key performance indicators (KPIs) such as customer acquisition cost, customer lifetime value, and customer churn rate.
- ► Developed and maintained social media campaigns to increase customer engagement and revenue, using data analytics to track engagement and ROI, and optimize campaign strategies based on predictive and prescriptive analytics algorithms.
- ► Conducted market research and competitive analysis using structured and unstructured data to stay informed of industry trends and customer preferences.
- ► Utilized machine learning techniques such as supervised and unsupervised learning, regression, and classification to identify hidden patterns and insights that helped improve the company's products and services.
"""
)

# --- CIRTIFICATIONS ---

CERTIFICATION = {
    "🎓️ Data Cleaning with Python Certification - Codecadamy": {
        "link": "https://www.codecademy.com/profiles/salahalbasha/certificates/e773a003314c1be60da8388a90a77e78",
    },
    "🎓 Python 3 Certification - Codecadamy": {
        "link": "https://www.codecademy.com/profiles/salahalbasha/certificates/6c152bd262967f8c941c9707ed636bda",
    },
    "🎓 BI Dashboards with Power BI - Codecadamy": {
        "link": "https://www.codecademy.com/profiles/salahalbasha/certificates/1cb76ac48943853ca32c394afeb491c9",
    },
    "🎓 Tableau for Data Visualization - Codecadamy": {
        "link": "https://www.codecademy.com/profiles/salahalbasha/certificates/bb909db0a89b47a59d9bf08a039e28ad",
    },
    "🎓 SQL Certification - Codecadamy": {
        "link": "https://www.codecademy.com/profiles/salahalbasha/certificates/042a4e5884e3eb6ea1f2a12be6abb851",
    },
    "🎓 HTML Certification - Codecadamy": {
        "link": "https://www.codecademy.com/profiles/salahalbasha/certificates/9eb0741e5ebef1f9f58a53bfac67d3a7",
    },
    "🎓 Scrum Product Owner Certified (SPOC)": {
        "link": "",
    },
    "🎓 Introduction to UI and UX Design Certification - Codecadamy": {
        "link": "https://www.codecademy.com/profiles/salahalbasha/certificates/4ccef8d532484ea2aeec3b3b3dbb4f9c",
    },
    "🎓 Command Line Certification - Codecadamy": {
        "link": "https://www.codecademy.com/profiles/salahalbasha/certificates/c87ba0541f8be78bc2f4ba1128233f6f",
    },
}


# -- CERTIFICATIONS --
st.write('\n')
st.subheader("Professional Development")
st.write("---")
for certification, details in CERTIFICATION.items():
    st.write(f"[{certification}]({details['link']})")
    
# -- SOFT SKILLS --
st.subheader("Soft Skills")
st.write("---")
"""
- 🌍 English and Arabic (business-level), French and ASL (elementary level)

- 🌍 Focused on creating accessible and inclusive Data Viz, including implementing information redundancy and using color palettes that are accessible to colorblind viewers
- 🌍 Situational awareness, public speaking and leadership skills
- 🌍 Strong interpersonal skills and routinely reaches out to colleagues to maintain transparency and manifest open communication.
- 🌍 Ability to de-escalate tougher interactions.
- 🌍 Familiar with integration of Agile methodologies in group projects.
"""

