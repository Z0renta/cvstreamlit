from pathlib import Path

# import streamlit as st
# from PIL import Image
# import pandas as pd
# from bokeh.plotting import figure








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