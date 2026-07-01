import pandas as pd

def assign_typology(df: pd.DataFrame) -> pd.DataFrame:
    """
    Attribue une typologie principale à partir
    d'une combinaison de dimensions.
    """
    def classify(row):
        if (
            row["score_d1_resultats"] >= 70
            and row["score_d3_mobilisation"] >= 60
            and row["score_d6_couverture"] >= 80
            and row["score_d7_contraintes"] >= 70
        ):
            return "Prêt au déploiement"
        if row["score_d7_contraintes"] < 50:
            return "Contraintes opérationnelles"
        if (
            row["score_d1_resultats"] < 50
            and row["score_d3_mobilisation"] >= 50
        ):
            return "Priorité pédagogique"
        if (
            row["score_d2_disponibilite"] < 20
            and row["score_d4_enseignants"] < 35
        ):
            return "Ressources à renforcer"
        return "Accompagnement prioritaire"
    df["typologie"] = df.apply(classify, axis=1)
    return df

def generate_profile(df: pd.DataFrame) -> pd.DataFrame:
    """
    Génère un profil détaillé par dimension.
    """
    dimensions = {
        "D1 - Résultats d'apprentissage": "score_d1_resultats",
        "D2 - Disponibilité": "score_d2_disponibilite",
        "D3 - Mobilisation": "score_d3_mobilisation",
        "D4 - Enseignants mobilisés": "score_d4_enseignants",
        "D5 - Historique": "score_d5_historique",
        "D6 - Couverture": "score_d6_couverture",
        "D7 - Contraintes": "score_d7_contraintes"
    }
    def level(score):
        if score >= 80:
            return "Fort"
        elif score >= 60:
            return "Satisfaisant"
        elif score >= 40:
            return "À renforcer"
        else:
            return "Critique"
    def build_profile(row):
        profile = {}
        for dimension, column in dimensions.items():
            profile[dimension] = {
                "score": round(row[column], 1),
                "niveau": level(row[column])
            }
        return profile
    df["profil_detaille"] = df.apply(build_profile, axis=1)
    return df