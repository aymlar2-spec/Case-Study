import pandas as pd

def generate_report(df: pd.DataFrame) -> pd.DataFrame:
    """
    Génère une synthèse décisionnelle pour chaque établissement.
    """
    def build_report(row):
        strengths = []
        weaknesses = []
        if row["score_d1_resultats"] >= 70:
            strengths.append("Excellents résultats d'apprentissage.")
        if row["score_d3_mobilisation"] >= 70:
            strengths.append("Bonne mobilisation des enseignants.")
        if row["score_d6_couverture"] >= 80:
            strengths.append("Couverture élevée du dispositif.")
        if row["score_d7_contraintes"] >= 80:
            strengths.append("Contraintes opérationnelles limitées.")
        if row["score_d1_resultats"] < 50:
            weaknesses.append("Résultats d'apprentissage insuffisants.")
        if row["score_d2_disponibilite"] < 40:
            weaknesses.append("Disponibilité insuffisante des créneaux.")
        if row["score_d3_mobilisation"] < 50:
            weaknesses.append("Mobilisation des enseignants insuffisante.")
        if row["score_d4_enseignants"] < 40:
            weaknesses.append("Nombre d'enseignants mobilisés insuffisant.")
        if row["score_d5_historique"] < 50:
            weaknesses.append("Historique du dispositif peu favorable.")
        if row["score_d6_couverture"] < 60:
            weaknesses.append("Faible couverture des élèves éligibles.")
        if row["score_d7_contraintes"] < 60:
            weaknesses.append("Contraintes opérationnelles importantes.")
        if not strengths:
            strengths.append("Aucun point fort majeur identifié.")
        if not weaknesses:
            weaknesses.append("Aucun point faible critique identifié.")
        diagnostic = {
            "Prêt au déploiement":
                "Les principaux indicateurs sont satisfaisants. L'établissement est prêt pour un déploiement efficace du dispositif de soutien.",
            "Priorité pédagogique":
                "Les ressources sont présentes mais les résultats d'apprentissage nécessitent un accompagnement pédagogique ciblé.",
            "Ressources à renforcer":
                "Le principal frein concerne les ressources humaines ou matérielles nécessaires au déploiement du dispositif.",
            "Contraintes opérationnelles":
                "Les contraintes locales constituent le principal facteur limitant et nécessitent un accompagnement spécifique.",
            "Accompagnement prioritaire":
                "Plusieurs dimensions présentent des faiblesses importantes. Un plan d'accompagnement global est recommandé."
        }
        summary = ""
        for dimension, infos in row["profil_detaille"].items():
            summary += (
                f"• {dimension:<35}"
                f"{infos['score']:>6.1f}/100   "
                f"{infos['niveau']}\n"
            )
        report = f"""

ÉTABLISSEMENT : {row["nom_ecole"]}

TYPOLOGIE

{row["typologie"]}

SYNTHÈSE PAR AXE

{summary}

DIAGNOSTIC

{diagnostic[row["typologie"]]}

POINTS FORTS

• """ + "\n• ".join(strengths) + """

POINTS À RENFORCER

• """ + "\n• ".join(weaknesses) + """

PLAN D'ACTION PRIORITAIRE

"""
        for i, action in enumerate(row["recommandations"], start=1):
            report += f"{i}. {action}\n"
        return report
    df["rapport"] = df.apply(build_report, axis=1)
    return df