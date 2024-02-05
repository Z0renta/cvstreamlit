from pathlib import Path

import streamlit as st
from PIL import Image
import pandas as pd
from bokeh.plotting import figure








current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = "./style/main.css"
CV = "./font/cv2023.pdf"
pp = "./font/pp.png"


PAGE_TITLE = "CV WEB Alexis Cazin"
PAGE_ICON = ":wave:"
NAME = "Alexis Cazin"
DESCRIPTION = """
Etudiant en B2 année à Paris Ynov Campus.
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
with open(CV, "rb") as pdf_file:
    print(CV)
    PDFbyte = pdf_file.read()
pp = Image.open(pp)

col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(pp, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Examiné le CV",
        data=PDFbyte,
        file_name=CV.split("\\")[-1],
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
# Load the CSV data into a Pandas DataFrame
data = pd.DataFrame({'Competence': ['Java', 'PHP', 'Python', 'Golang', 'Javascript', 'Html', 'CSS', 'Git', 'SQL', 'Réseaux'], 'Maitrise': [4, 6, 8, 4, 7, 9, 9, 5, 7, 4]})

# Create a Bokeh figure
p = figure(y_range=data['Competence'], height = 300, width=600, title="Competence Maitriser")
p.hbar(y=data['Competence'], right=data['Maitrise'], height=0.9)

# Show the Bokeh figure in Streamlit
st.bokeh_chart(p)


st.write("#")
st.subheader("🌍 Linguistique")

# Load the CSV data into a Pandas DataFrame
data = pd.DataFrame({'Language': ['Anglais', 'Français'], 'Maitrise': [5.5, 8]})

# Create a Bokeh figure
p = figure(y_range=data['Language'], height = 300, width=600, title="Language Maitriser")
p.hbar(y=data['Language'], right=data['Maitrise'], height=0.9)

# Show the Bokeh figure in Streamlit
st.bokeh_chart(p)

# st.write("#")
st.write("---")
# st.write("#")
st.write("#")
st.subheader("Formations")

# Utiliser st.markdown() avec HTML pour créer un bloc de formation stylisé
st.markdown(
    """
    <div style="border: 1px solid #ddd; border-radius: 5px; padding: 10px; box-shadow: 1px 2px 5px #ccc; margin-top: 10px;">
        <p>Baccalauréat 2021/2022 (Physique, Mathématiques et Informatique)</p>
        <p>B2 Informatique</p>
        <p>Paris Ynov Campus, Nanterre - 09.2022 / 04.2027</p>
    </div>
    """,
    unsafe_allow_html=True
)

# st.write("\n")
st.write("---")
# st.write("\n")
st.write("#")

st.subheader("Expérience étudiante")

st.markdown(
    """
    <div style="border: 1px solid #ddd; border-radius: 5px; padding: 10px; box-shadow: 1px 2px 5px #ccc; margin-top: 10px;">
        <p>Jeux réalisés:</p>
        <p>Hangman/Hangman Web - Language: Golang/ HTML</p>
        <p>Snake - Language: Python </p>
        <p>Web développement: </p>
        <p>La réalisation des projets tels que ASCII ART Web via le Hangman - Language: Golang</p>
        <p>Le site Forum - Language: HTML/CSS/Golang/SQL</p>
    </div>
    """,
    unsafe_allow_html=True
)



# st.write("#")
st.write("---")
# st.write("#")

st.subheader("Expériences professionelles")

st.markdown(
    """
    <div style="border: 1px solid #ddd; border-radius: 5px; padding: 10px; box-shadow: 1px 2px 5px #ccc; margin-top: 10px;">
        <p>Ouvrier Polyvalent</p>
        <p>Les vins Richard 01/07/2022 au 01/09/2022 puis 01/07/2023 au 01/09/2023</p>
        <p>Preparateurs de commandes sur Fenwick puis Controlleur au retours vide </p>
    </div>
    """,
    unsafe_allow_html=True
)


# st.write("#")
st.write("---")
# st.write("#")

st.subheader("Mes Intérêts")
st.write("- Littérature japonaise | Basketball | Tenis | Jeux Vidéo ")