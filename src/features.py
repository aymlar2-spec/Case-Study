import pandas as pd

def create_features(df: pd.DataFrame) -> pd.DataFrame:
    """
    Crée les indicateurs nécessaires au modèle de scoring.
    """
    df["indice_disponibilite"] = (
        df["nb_creneaux"] /
        df["nb_eleves_eligibles"].replace(0, 1)
    )

    return df