from sklearn.preprocessing import MinMaxScaler
import pandas as pd

WEIGHTS = {
    "score_d1_resultats": 0.25,
    "score_d2_disponibilite": 0.15,
    "score_d3_mobilisation": 0.20,
    "score_d4_enseignants": 0.10,
    "score_d5_historique": 0.10,
    "score_d6_couverture": 0.15,
    "score_d7_contraintes": 0.05
}

def normalize_minmax(series: pd.Series) -> pd.Series:
    """
    Normalise une série entre 0 et 100.
    """
    scaler = MinMaxScaler(feature_range=(0, 100))
    normalized = scaler.fit_transform(series.values.reshape(-1, 1))
    return pd.Series(
        normalized.flatten(),
        index=series.index
    )

def score_d1_results(df: pd.DataFrame) -> pd.DataFrame:
    """
    D1 : Résultats d'apprentissage.
    """
    df["score_d1_resultats"] = df["taux_maitrise"]
    return df

def score_d2_availability(df: pd.DataFrame) -> pd.DataFrame:
    """
    D2 : Disponibilité des classes.
    Le score est calculé à partir de l'indice de disponibilité
    puis normalisé entre 0 et 100.
    """
    df["score_d2_disponibilite"] = normalize_minmax(
        df["indice_disponibilite"]
    )
    return df

def score_d3_teacher_mobilization(df: pd.DataFrame) -> pd.DataFrame:
    """
    D3 : Mobilisation des enseignants.
    Le score correspond directement au taux de mobilisation.
    """
    df["score_d3_mobilisation"] = df["taux_mobilisation"]* 100
    return df

def score_d4_mobilized_teachers(df: pd.DataFrame) -> pd.DataFrame:
    """
    D4 : Enseignants déjà mobilisés.
    Le score est obtenu après normalisation
    du nombre d'enseignants mobilisés.
    """
    df["score_d4_enseignants"] = normalize_minmax(
        df["nb_enseignants_mobilises"]
    )
    return df

def score_d5_history(df: pd.DataFrame) -> pd.DataFrame:
    """
    D5 : Historique du soutien étalé.
    """
    def history_score(row):
        if row["soutien_precedent"] == "Oui":
            if row["impact_precedent"] == "Amélioration notable":
                return 100
            elif row["impact_precedent"] == "Amélioration limitée":
                return 75
            elif row["impact_precedent"] == "Aucune amélioration observée":
                return 40
            elif row["impact_precedent"] == "Impact non mesuré":
                return 50
            else:
                return 50
        return 20
    df["score_d5_historique"] = df.apply(history_score, axis=1)
    return df

def score_d6_coverage(df: pd.DataFrame) -> pd.DataFrame:
    """
    D6 : Couverture du soutien.
    Le score correspond au taux de couverture converti sur 100.
    """
    df["score_d6_couverture"] = df["taux_couverture"] * 100
    return df

def score_d7_constraints(df: pd.DataFrame) -> pd.DataFrame:
    """
    D7 : Contraintes opérationnelles.
    Le score est calculé à partir de :
    - l'absentéisme,
    - l'enclavement,
    - le turnover.
    """
    enclavement_scores = {
        "Faible": 100,
        "Moyen": 60,
        "Élevé": 20
    }
    turnover_scores = {
        "Faible": 100,
        "Moyen": 60,
        "Élevé": 20
    }
    df["score_absenteisme"] = 100 - df["taux_absenteisme"]
    df["score_enclavement"] = df["enclavement"].map(enclavement_scores)
    df["score_turnover"] = df["turnover"].map(turnover_scores)
    df["score_d7_contraintes"] = (
        df[
            [
                "score_absenteisme",
                "score_enclavement",
                "score_turnover"
            ]
        ].mean(axis=1)
    )
    return df
def calculate_global_score(df: pd.DataFrame) -> pd.DataFrame:
    """
    Calcule le score global pondéré.
    """
    df["score_global"] = 0
    for column, weight in WEIGHTS.items():
        df["score_global"] += df[column] * weight
    return df
