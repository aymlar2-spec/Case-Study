import streamlit as st

st.set_page_config(
    page_title="Outil d'aide à la décision",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("📊 Outil d'aide à la décision")

st.markdown("""
### Priorisation des établissements pour le soutien scolaire

Cette application permet d'analyser les établissements scolaires à partir de sept dimensions d'évaluation.

Les fonctionnalités principales sont :

- 📊 Tableau de bord décisionnel
- 🏫 Analyse détaillée d'un établissement
- 📋 Vue d'ensemble des établissements
- ⚖️ Comparaison de deux établissements

L'objectif est d'aider la Direction Provinciale à identifier les leviers d'action prioritaires pour le déploiement du soutien scolaire.
""")

st.info(
    "Utilisez le menu situé à gauche pour accéder aux différentes fonctionnalités."
)