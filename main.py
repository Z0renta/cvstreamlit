from pathlib import Path

import streamlit as st
from PIL import Image
import pandas as pd
from bokeh.plotting import figure








current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "style" / "main.css"
resume_file = current_dir / "assets" / "cv2023.pdf"
profile_pic = current_dir / "assets" / "pp.png"


PAGE_TITLE = "CV WEB Alexis Cazin"
PAGE_ICON = ":wave:"
NAME = "Alexis Cazin"
DESCRIPTION = """
Etudiant en 2eme année à Paris Ynov Campus.
"""
EMAIL = "alexis.czin@gmail.com"
EMAIL2 = "alexis.cazin@ynov.com"
SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/alexis-cazin-b19836260/",
    "GitHub": "https://github.com/Z0renta",
}

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)

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

st.write("#")
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")

st.write("#")
st.subheader("Competénces")
st.write(
    """
- ✔️ CAPACITES D’ANALYSE
- ✔️ ESPRIT DE RESPONSABILITE
- ✔️ TRAVAIL EN EQUIPE
- ✔️ CAPACITE D’ADAPTATION
- ✔️ GESTION DU STRESS

"""
)

st.write("#")
st.subheader("Competénces en informatiques")
st.write(
    """
Java | Php | Python (POO, bibliothèques de
Data) | Golang | C# | C++ | Javascript |
HTML | CSS | Git | Dart/Flutter | Symfony
| SQL | NoSQL | Gestion de DevOps |
Maths DataScience | Docker | UX/UI | La gestion de reseaux, (windows server,
ubuntu, debian)

"""
)



st.write("#")
st.subheader("Data Skills")
st.write(
    """
- 👩‍💻 Programmation: Python (Scikit-learn, Pandas), SQL, Seaborn, BautifulSoup
- 📊 Data Visualisation: PowerBi, Seaborn, Plotly
- 📚 Modelation: Logistic regression, linear regression, decition trees
- 🗄️ Databases: Postgres, MongoDB, MySQL
"""
)

st.write("#")
st.subheader("🌍 Langues")

# Load the CSV data into a Pandas DataFrame
data = pd.DataFrame({'Language': ['Anglais', 'Français', 'Russe'], 'Scores': [6, 9, 10]})

# Create a Bokeh figure
p = figure(y_range=data['Language'], height = 300, width=600, title="Language Scores")
p.hbar(y=data['Language'], right=data['Scores'], height=0.9)

# Show the Bokeh figure in Streamlit
st.bokeh_chart(p)

# st.write("#")
st.write("---")
# st.write("#")

st.subheader("Formations")

st.write(" - 📚 Baccalauréat (Physique, Mathématiques et Informatique)")
st.write("École de l'ambassade de la Fédération de Russie, Vietnam(Vung Tau) - 09.2016 / 06.2019")
st.write(" - 📙 Mastère Informatique")
st.write("Paris Ynov Campus, Nanterre - 09.2020 / 04.2025")

# st.write("\n")
st.write("---")
# st.write("\n")

st.subheader("Expérience étudiant")

st.write("🏴 Data projects")

st.write("- ➖ La problématique :")
st.write("- Est-ce que les types de restaurants des pays d'Europe influent-ils sur l'IMC? le travail avec les datasets et la réponse à ce problème à l'aide de données")
st.write("- - 🛠 Technologies: plotly, matplotlib, numpy, pandas")
st.write("- ➖ Scraping des données de carrefour et les affichage sur Streamlit avec des graphiques")
st.write("- - 🛠 Technologies: Selenium, Streamlit, MongoDb")



st.write("🏴 Les jeux:")

st.write("- ➖ Pacman Web")
st.write("- - 🛠 Technologies: Pure JS, POO en JS")
st.write("- ➖ Le jeu des dames avec une interface graphique")
st.write("- - 🛠 Technologies: POO Java, Gestion de sockets, BDD")


st.write("🏴 Web développement:")

st.write("- ➖ La réalisation des projets tels que ASCII ART Web ")
st.write("- - 🛠 Technologies: Golang")
st.write("- ➖ Le site Forum")
st.write("- - 🛠 Technologies: PHP, sql")
st.write("- ➖ L'affichage des données mongodb sur une page Web et les filtrer, la barre de recherche")
st.write("- - 🛠 Technologies: HTML, CSS, JS, Express, NoSql")

# st.write("#")
st.write("---")
# st.write("#")

st.subheader("Expériences professionelles")
st.write("📈 Mentor")
st.write("- Ynov Campus, Nanterre - Depuis 07.2022")
st.write("- - 📐 Le travail avec les élèves B1 et B2, enseignements pédagogiques, aide à la réalisation de leurs projets selon le cursus")

# st.write("#")
st.write("---")
# st.write("#")

st.subheader("Intérêts")
st.write("- ⚽️ | 🏀 | 🥊 | 🦾 | 🎧 | 🎵")