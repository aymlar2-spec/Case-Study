import pandas as pd 
def load_data(file_path: str) -> pd.DataFrame:
    """
    Charge le fichier Excel.
    """
    df = pd.read_excel(file_path)
    return df 
def clean_data(df: pd.DataFrame) -> pd.DataFrame: 
    """
    Nettoyage et préparation des données.
    """
    df.columns = df.columns.str.strip()
    for col in df.select_dtypes(include="object").columns:
        df[col] = df[col].astype(str).str.strip()
    column_mapping = {
    "Code école": "code_ecole",
    "Nom école (fictif)": "nom_ecole",
    "Province": "province",
    "Type (EP/CP)": "type_ecole",
    "Milieu": "milieu",
    "Effectif élèves": "effectif_eleves",
    "Nb élèves éligibles au soutien (Post-TARL)": "nb_eleves_eligibles",
    "Taux de maîtrise Post-TARL (%)": "taux_maitrise",
    "Nb élèves bénéficiant actuellement du soutien": "nb_eleves_soutenus",
    "Nb créneaux/salles disponibles pour le soutien (/semaine)": "nb_creneaux",
    "Effectif enseignants": "effectif_enseignants",
    "Nb enseignants mobilisés pour le soutien": "nb_enseignants_mobilises",
    "Soutien étalé réalisé l'année précédente": "soutien_precedent",
    "Impact observé l'année précédente": "impact_precedent",
    "Taux d'absentéisme élèves aux séances (%)": "taux_absenteisme",
    "Enclavement de l'école": "enclavement",
    "Turnover des enseignants": "turnover",
    "Fiabilité de la saisie Massar": "fiabilite_massar",
    "Taux de couverture du soutien (%)": "taux_couverture",
    "Taux de mobilisation des enseignants (%)": "taux_mobilisation"
    }

    df.rename(columns=column_mapping, inplace=True)
    return df
