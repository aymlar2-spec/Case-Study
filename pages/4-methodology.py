import streamlit as st

st.title("📘 Méthodologie")

st.markdown("""
## Objectif

Cette application constitue un outil d'aide à la décision destiné à accompagner la priorisation des établissements scolaires dans le cadre du déploiement du soutien scolaire.

## Démarche

Le processus comprend :

1. Prétraitement des données.
2. Construction d'indicateurs.
3. Calcul des 7 sous-scores.
4. Attribution d'une typologie selon des règles métier.
5. Génération automatique de recommandations.
6. Production d'un rapport décisionnel.

## Les sept dimensions

- Résultats d'apprentissage
- Disponibilité des ressources
- Mobilisation des enseignants
- Ressources humaines mobilisées
- Historique du dispositif
- Couverture des élèves
- Contraintes opérationnelles

## Remarque

Conformément au cahier des charges, l'analyse repose principalement sur les sous-scores par dimension. Le score global est uniquement utilisé comme indicateur de synthèse et ne sert ni à classer les établissements ni à déterminer leur typologie.
""")