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
    "🏆 Pima Indians Diabetes Analysis - Exploring the Factors Behind the Disease among Pima Tribe Women": "https://youtu.be/Sb0A9i6d320",
    "🏆 Hotel Booking Cancellation Prediction - Classification and Hypothesis Testing": "https://youtu.be/3egaMfE9388",
    "🏆 US Accidents - Exploratory Data Analysis": "https://pythonandvba.com/mytoolbelt/",
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
    cols[index].write(f"[{platform}]({link})")

# --- SKILLS ---
st.write('\n')
st.subheader("Hard Skills")
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
st.write(
    """
- ✔️ Bachelor's of Applied Mathematics at Carleton
- ✔️ Data Science and Machine Learning at MIT
- ✔️ 2 Years of expereince extracting actionable insights from data
- ✔️ Strong hands on experience and knowledge in Python, SQL and Excel
- ✔️ Good understanding of statistical principles and their respective applications
"""
)

# --- Projects & Accomplishments ---
st.write('\n')
st.subheader("Projects & Accomplishments")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")


# --- WORK HISTORY ---
st.write('\n')
st.subheader("Work History")
st.write("---")

# --- JOB 1
st.write("🚧", "**Technical Support Analyst | Shopify**")
st.write("11/2021 - 09/2022")
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
st.write("11/2020 - 11/2021")
st.write(
    """
- ► Analyzed customer data to identify trends and insights that informed sales strategies, including the measurement of key performance indicators (KPIs) such as customer acquisition cost, customer lifetime value, and customer churn rate.
- ► Developed and maintained social media campaigns to increase customer engagement and revenue, using data analytics to track engagement and ROI, and optimize campaign strategies based on predictive and prescriptive analytics algorithms.
- ► Conducted market research and competitive analysis using structured and unstructured data to stay informed of industry trends and customer preferences.
- ► Utilized machine learning techniques such as supervised and unsupervised learning, regression, and classification to identify hidden patterns and insights that helped improve the company's products and services.
"""
)

