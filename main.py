from pathlib import Path

import streamlit as st
from PIL import Image
import pandas as pd
from bokeh.plotting import figure








current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "style" / "main.css"
resume_file = current_dir / "assets" / "cv2023.pdf"
pp = current_dir / "assets" / "pp.png"


PAGE_TITLE = "CV WEB Alexis Cazin"
PAGE_ICON = ":wave:"
NAME = "Alexis Cazin"
DESCRIPTION = """
Etudiant en 2eme année à Paris Ynov Campus.
"""
EMAIL = "alexis.czin@gmail.com"
EMAIL2 = "alexis.cazin@ynov.com"
SOCIAL = {
    "LinkedIn": "https://www.linkedin.com/in/alexis-cazin-b19836260/",
    "GitHub": "https://github.com/Z0renta",
}

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
pp = Image.open(pp)

col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(pp, width=230)

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
    st.write("📫", EMAIL2)

st.write("#")
cols = st.columns(len(SOCIAL))
for index, (platform, link) in enumerate(SOCIAL.items()):
    cols[index].write(f"[{platform}]({link})")

st.write("#")
st.subheader("Competénces")
st.write(
    """
- ✔️ CAPACITES D’ANALYSE
- ✔️ TRAVAIL EN EQUIPE
- ✔️ CAPACITE D’ADAPTATION
- ✔️ GESTION DU STRESS

"""
)

st.write("#")
st.subheader("Competénces en informatiques")
st.write(
    """
Java | Php | Python (POO)| 
Golang | Javascript |
HTML | CSS | Git |
SQL | La gestion de reseaux,
(windows server, ubuntu, debian)

"""
)

st.write("#")
st.subheader("🌍 Langues")

# Load the CSV data into a Pandas DataFrame
data = pd.DataFrame({'Language': ['Anglais', 'Français'], 'Scores': [5.5, 8]})

# Create a Bokeh figure
p = figure(y_range=data['Language'], height = 300, width=600, title="Language Scores")
p.hbar(y=data['Language'], right=data['Scores'], height=0.9)

# Show the Bokeh figure in Streamlit
st.bokeh_chart(p)

# st.write("#")
st.write("---")
# st.write("#")

st.subheader("Formations")

st.write(" -  Baccalauréat 2021/2022 (Physique, Mathématiques et Informatique)")
st.write(" -  B2 Informatique")
st.write("Paris Ynov Campus, Nanterre - 09.2022 / 04.2027")

# st.write("\n")
st.write("---")
# st.write("\n")

st.subheader("Expérience étudiante")


st.write("Jeux réaliser")

st.write("- Hangman/Hangman Web")
st.write("- - Language: Golang/ HTML ")
st.write("- Snake")
st.write("- - Language: Python")


st.write("🏴 Web développement:")

st.write("- ➖ La réalisation des projets tels que ASCII ART Web ")
st.write("- - 🛠 Technologies: Golang")
st.write("- ➖ Le site Forum")
st.write("- - Language: HTML/CSS/Golang/SQL")

# st.write("#")
st.write("---")
# st.write("#")

st.subheader("Expériences professionelles")
st.write("Ouvrier Polyvalent")
st.write("- Les vins Richard 01/07/2022 au 01/09/2022 puis 01/07/2023 au 01/09/2023")
st.write("- - Preparateurs de commandes sur Fenwick puis Controlleur au retours vide ")

# st.write("#")
st.write("---")
# st.write("#")

st.subheader("Mes Intérêts")
st.write("- Littérature japonaise | Basketball | Tenis | Jeux Vidéo ")