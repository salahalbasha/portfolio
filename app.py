from pathlib import Path
from PIL import Image
import streamlit as st
from PIL import Image

# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV.pdf"
profile_pic = current_dir / "assets" / "profile-pic.png"

# --- GENERAL SETTINGS ---
PAGE_TITLE = "Portfolio | Salah Al-Basha"
PAGE_ICON = ":wave:"
NAME = "Salah Al-Basha"
DESCRIPTION = """
Analyst | Assisting enterprises by supporting data-driven decision-making.

"""
EMAIL = "salahalbasha12@yahoo.com"
SOCIAL_MEDIA = {
    "LinkedIn": "https://linkedin.com/in/salahalbasha/",
    "GitHub": "https://github.com/salahalbasha/",
}

PROJECTS = {
    "🏆 Pima Indians Diabetes Analysis": {
        "link": "https://salahalbasha-pima-app-yo940c.streamlit.app/",
        "skills_tools": "Python, Pandas, Numpy, Matplotlib, Seaborn, Machine Learning, Data Analysis",
        "description": "Explore diabetes factors using data analysis techniques on a dataset from the Pima tribe. The objective is to understand factors related to diabetes within the Pima tribe and explore potential associations between variables.",
    },
    "🏆 Movie Recommendation System": {
        "link": "https://salahalbasha-movie-app-c5pu9r.streamlit.app/",
        "skills_tools": "Collaborative filtering, Matrix factorization, Recommendation systems",
        "description": "This project builds a recommendation system for online streaming platforms, like Netflix, to suggest relevant movies based on user interactions. Various recommendation techniques are employed, including rank-based and collaborative filtering. The system utilizes a ratings dataset to analyze user preferences and make personalized recommendations. The project aims to enhance customer satisfaction and increase platform revenue.",
    },
    "🏆 Analysis of United States Accidents": {
        "link": "https://salahalbasha-accidents-accidents-8nnvpw.streamlit.app/",
        "skills_tools": "Exploratory Data Analysis, Data Cleaning, Data Visualization, BigData",
        "description": "This project analyzes a real-world dataset of car accidents in the United States to uncover insights on accident frequency, distribution, and potential causes. By examining approximately 2.8 million records, the project aims to improve road safety and promote safe driving practices.",
    },
}

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

# --- LOAD CSS, PDF & PROFILE PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


# Toggle Button State (initialize to Light Mode)
# is_dark_mode = st.checkbox("Dark Mode", value=False, key="dark_mode_checkbox")


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

# --- EDUCATION---
st.write('\n')
st.subheader("Education")
st.write("---")
st.write("###### 🎓 B.Math, background in Computer Science at Carleton")
st.write("###### 🎓️ Data Science and Machine Learning at MIT")

# --- WORK HISTORY ---
st.write('\n')
st.subheader("Work History")
st.write("---")

# --- JOB 1
st.write("#### 🚧 Software Engineer | Chana Company Inc.")
st.write(
    """
- ► Built a recommendation system using collaborative filtering and matrix factorization to provide personalized movie recommendations based on user ratings.
- ► Examined 2.8 million US accident records, performed exploratory data analysis, implemented data cleaning techniques, and used data visualization tools to improve road safety and promote safe driving practices.
- ► Collaborating with cross-functional teams to gather requirements, analyze user needs, and propose innovative solutions.
- ► Conducting thorough testing and debugging of software applications to ensure optimal performance and reliability.
"""
)

# --- JOB 2
st.write("#### 🚧 AI Engineer | Lomdi AI")
st.write(
    """
- ► Developed and maintained an innovative entertainment app for real-time conversations with celebrities and fictional characters using Python.
- ► Leveraged Cloud Computing technologies to ensure scalability and optimize app performance for a large user base.
- ► Implemented Google PaLM as the language processor to generate dynamic and context-aware responses in conversations.
- ► Utilized Vertex AI for advanced machine learning capabilities, enhancing the app's conversational experience.
"""
)

# --- JOB 3
st.write("#### 🚧 Analyst | Shopify")
st.write(
    """
- ► Conducted in-depth technical troubleshooting using various tools and technologies to resolve complex merchant issues, while also measuring the KPIs of merchant satisfaction and issue resolution time using BigData analysis techniques.
- ► Analyzed merchant data and provided customized solutions to improve metrics such as conversion rates, customer satisfaction, and average order value using artificial intelligence (AI) and deep learning algorithms.
- ► Developed expertise in Shopify's products and services to provide expert advice to merchants, while also leveraging data analytics to suggest improvements to existing products and services.
- ► Collaborated with cross-functional teams on projects such as Bridge the Gap, the Next Pilot, and the US Capital, using data analysis and reporting to support project goals and track the success of each initiative.
"""
)

# --- JOB 4
st.write('\n')
st.write("#### 🚧 Fitness Sales Analyst | GoodLife Fitness")
st.write(
    """
- ► Analyzed customer data to identify trends and insights that informed sales strategies, including the measurement of key performance indicators (KPIs) such as customer acquisition cost, customer lifetime value, and customer churn rate.
- ► Developed and maintained social media campaigns to increase customer engagement and revenue, using data analytics to track engagement and ROI, and optimize campaign strategies based on predictive and prescriptive analytics algorithms.
- ► Conducted market research and competitive analysis using structured and unstructured data to stay informed of industry trends and customer preferences.
- ► Utilized machine learning techniques such as supervised and unsupervised learning, regression, and classification to identify hidden patterns and insights that helped improve the company's products and services.
"""
)

# Projects
st.write('\n')
st.subheader("Projects")
st.write("---")
for project, details in PROJECTS.items():
    st.write(f"### [{project}]({details['link']})")
    st.write(f"**Description**: {details['description']}")

    skills_tools = details['skills_tools'].split(", ")
    skills_html = " ".join(f"<span class='skills-box'>{skill_tool}</span>" for skill_tool in skills_tools)
    st.markdown(skills_html, unsafe_allow_html=True)

    st.write("---")

# --- SKILLS ---
st.write('\n')
st.subheader("Hard Skills")
st.write("---")
st.write(
    """
- 🧑🏻‍💻 Programming: Python (Pandas, Numpy, Matplotlib, Seaborn), SQL
- 📊 BI & Analytics tools: Power BI, Tableau, MS Excel
- ⚛️ AI Tools: Google PaLM, Vertex AI, Cloud Computing
- 📚 Modeling: Logistic regression, linear regression, decision trees
- 💻 Web Development: HTML, CSS
- 📽 PM Frameworks: Scrum, Confluence, Trello
- 👷🏻‍♂️ Technical/SaaS: Slack, Markdown, Prompt Engineering
- 📋 Digital Products/Apps: UI/UX, Figma, Canva
"""
)

# --- CERTIFICATIONS ---

CERTIFICATION = {
    "️️️✔️ Data Science and Machine Learning: Making Data-Driven Decisions - MIT": {
        "link": "https://verify.mygreatlearning.com/verify/QSMAMQYD",
    },
    "️️️✔️ Data Cleaning with Python Certification - Codecadamy": {
        "link": "https://www.codecademy.com/profiles/salahalbasha/certificates/e773a003314c1be60da8388a90a77e78",
    },
    "✔️ Python 3 Certification - Codecadamy": {
        "link": "https://www.codecademy.com/profiles/salahalbasha/certificates/6c152bd262967f8c941c9707ed636bda",
    },
    "✔️ BI Dashboards with Power BI - Codecadamy": {
        "link": "https://www.codecademy.com/profiles/salahalbasha/certificates/1cb76ac48943853ca32c394afeb491c9",
    },
    "✔️ Tableau for Data Visualization - Codecadamy": {
        "link": "https://www.codecademy.com/profiles/salahalbasha/certificates/bb909db0a89b47a59d9bf08a039e28ad",
    },
    "✔️ SQL Certification - Codecadamy": {
        "link": "https://www.codecademy.com/profiles/salahalbasha/certificates/042a4e5884e3eb6ea1f2a12be6abb851",
    },
    "✔️ HTML Certification - Codecadamy": {
        "link": "https://www.codecademy.com/profiles/salahalbasha/certificates/9eb0741e5ebef1f9f58a53bfac67d3a7",
    },
    "✔️ Scrum Product Owner Certified (SPOC)": {
        "link": "",
    },
    "✔️ Introduction to UI and UX Design Certification - Codecadamy": {
        "link": "https://www.codecademy.com/profiles/salahalbasha/certificates/4ccef8d532484ea2aeec3b3b3dbb4f9c",
    },
    "✔️ Command Line Certification - Codecadamy": {
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
st.write("🌍 Focused on creating accessible and inclusive data visualization, including implementing information redundancy and using color palettes that are accessible to colorblind viewers.")
st.write("🌍 Situational awareness, public speaking and leadership skills.")
st.write("🌍 Strong teamwork and interpersonal skills.")
st.write("🌍 Experienced in conflict resolution.")
st.write("🌍 Familiar with Scrum and other Agile methodologies.")
st.write("🌍 Bilingual: English and Arabic.")


# Dark mode light mode toggle CSS
st.markdown("""
<style>
  @import url('https://fonts.googleapis.com/css2?family=Readex+Pro:wght@300;400;500;600;700&display=swap');


* {font-family: 'Readex Pro';}


a {
    text-decoration: none;
    color: white !important;
    font-weight: 500;
}

a:hover {
    color: #d33682 !important;
    text-decoration: none;
}

ul {list-style-type: none;}

hr {
    margin-top: 0px;
    margin-bottom: 5%;
}

#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}

a.square-link {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  width: 200px;
  height: 50px;
  border-radius: 8px;
  background-color: transparent;
  border: 2px solid white;
  color: white !important;
  font-weight: 500;
  text-decoration: none;
  font-size: 16px;
  transition: border-color 0.3s ease;
}

a.square-link:hover {
  border-color: #d33682;
}

.skills-box {
  display: inline-block;
  background-color: #f0f0f0;
  color: #333;
  padding: 6px 12px;
  border-radius: 4px;
  margin-right: 10px;
  margin-bottom: 10px;
}

* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}
body {
  width: 100%;
  height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-direction: column;
}
label {
  position: relative;
  width: 480px;
  height: 180px;
  display: block;
  background: url('images/images1.gif');
  background-size: cover;
  background-position: center;
  border: 10px solid rgba(198, 247, 253, 0.3);
  border-radius: 100px;
  cursor: pointer;
  transition: 1s ease;
  box-shadow: 0 0 25px rgba(0, 0, 0, 0.2);
}
label::after {
  content: '';
  position: absolute;
  height: 110px;
  width: 110px;
  background: #f2f2f2;
  border-radius: 50%;
  top: 25px;
  left: 30px;
  transition: 0.8s ease;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.2);
}
label::before {
  content: '';
  position: absolute;
  height: 110px;
  width: 110px;
  border: 10px solid rgba(198, 247, 253, 0.3);
  border-radius: 50%;
  top: 15px;
  left: 20px;
  transition: 0.8s ease;
  box-shadow: 0 0 50px rgba(0, 0, 0, 0.18);
}
.background {
  position: absolute;
  width: 100%;
  height: 100vh;
  background: #9ad6f7;
  z-index: -1;
  transition: all 1s ease;
}

input:checked ~ label::after {
  left: 430px;
  transform: translateX(-100%);
  background: #777ba5;
}
input:checked ~ label::before {
  left: 440px;
  border: 10px solid rgba(90, 79, 136, 0.2);
  transform: translateX(-100%);
}
input:checked ~ label {
  background: url('images/images2.gif');
  background-size: cover;
  background-position: center;
  border: 10px solid rgba(90, 79, 136, 0.2);
}
input:checked ~ .background {
  background: #0e377c;
}
input {
  display: none;
}
</style>
""", unsafe_allow_html=True)

