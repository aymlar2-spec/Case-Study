import streamlit as st
import plotly.express as px

from src.pipeline import load_pipeline

st.title("📊 Tableau de bord")

df = load_pipeline()

st.sidebar.header("Filtres")

province = st.sidebar.multiselect(
    "Province",
    sorted(df["province"].unique()),
    default=sorted(df["province"].unique())
)

type_ecole = st.sidebar.multiselect(
    "Type d'établissement",
    sorted(df["type_ecole"].unique()),
    default=sorted(df["type_ecole"].unique())
)

milieu = st.sidebar.multiselect(
    "Milieu",
    sorted(df["milieu"].unique()),
    default=sorted(df["milieu"].unique())
)

typologie = st.sidebar.multiselect(
    "Typologie",
    sorted(df["typologie"].unique()),
    default=sorted(df["typologie"].unique())
)

filtered_df = df[
    (df["province"].isin(province))
    & (df["type_ecole"].isin(type_ecole))
    & (df["milieu"].isin(milieu))
    & (df["typologie"].isin(typologie))
]

col1, col2, col3, col4 = st.columns(4)

col1.metric("Établissements", len(filtered_df))
col2.metric("Provinces", filtered_df["province"].nunique())
col3.metric("Typologies", filtered_df["typologie"].nunique())
col4.metric("Élèves", int(filtered_df["effectif_eleves"].sum()))

st.divider()

st.subheader("Répartition des typologies")

typology_count = (
    filtered_df["typologie"]
    .value_counts()
    .reset_index()
)

typology_count.columns = ["Typologie", "Nombre"]

fig = px.bar(
    typology_count,
    x="Typologie",
    y="Nombre",
    text="Nombre"
)

fig.update_layout(
    xaxis_title="",
    yaxis_title="Nombre d'établissements",
    xaxis_tickangle=-20
)

st.plotly_chart(fig, use_container_width=True)

st.divider()

st.subheader("Score moyen par dimension")

dimension_df = {
    "Dimension": [
        "Résultats",
        "Disponibilité",
        "Mobilisation",
        "Enseignants",
        "Historique",
        "Couverture",
        "Contraintes"
    ],
    "Score": [
        round(filtered_df["score_d1_resultats"].mean(), 1),
        round(filtered_df["score_d2_disponibilite"].mean(), 1),
        round(filtered_df["score_d3_mobilisation"].mean(), 1),
        round(filtered_df["score_d4_enseignants"].mean(), 1),
        round(filtered_df["score_d5_historique"].mean(), 1),
        round(filtered_df["score_d6_couverture"].mean(), 1),
        round(filtered_df["score_d7_contraintes"].mean(), 1),
    ]
}

fig = px.bar(
    dimension_df,
    x="Dimension",
    y="Score",
    text_auto=".1f"
)

fig.update_layout(
    yaxis_range=[0, 100],
    xaxis_title="",
    yaxis_title="Score moyen"
)

st.plotly_chart(fig, use_container_width=True)

st.divider()

st.subheader("Établissements")

display_df = filtered_df[
    [
        "nom_ecole",
        "province",
        "type_ecole",
        "milieu",
        "typologie",
        "score_d1_resultats",
        "score_d2_disponibilite",
        "score_d3_mobilisation",
        "score_d4_enseignants",
        "score_d5_historique",
        "score_d6_couverture",
        "score_d7_contraintes",
    ]
].rename(
    columns={
        "nom_ecole": "Établissement",
        "province": "Province",
        "type_ecole": "Type",
        "milieu": "Milieu",
        "typologie": "Typologie",
        "score_d1_resultats": "Résultats",
        "score_d2_disponibilite": "Disponibilité",
        "score_d3_mobilisation": "Mobilisation",
        "score_d4_enseignants": "Enseignants",
        "score_d5_historique": "Historique",
        "score_d6_couverture": "Couverture",
        "score_d7_contraintes": "Contraintes",
    }
)

display_df = display_df.round(1)

st.dataframe(
    display_df,
    use_container_width=True,
    hide_index=True
)