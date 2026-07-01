import streamlit as st
import plotly.graph_objects as go
from src.pipeline import load_pipeline
st.caption("Direction Provinciale • Outil d'aide à la décision")
st.title("🏫 Analyse d'un établissement")
df = load_pipeline()
ecole = st.selectbox(
    "Sélectionnez un établissement",
    sorted(df["nom_ecole"].unique())
)
row = df[df["nom_ecole"] == ecole].iloc[0]
left, right = st.columns([2, 1])
with left:
    st.subheader("Informations générales")
    st.write(f"**Établissement :** {row['nom_ecole']}")
    st.write(f"**Province :** {row['province']}")
    st.write(f"**Type :** {row['type_ecole']}")
    st.write(f"**Milieu :** {row['milieu']}")
with right:
    st.subheader("Typologie")
    if row["typologie"] == "Prêt au déploiement":
        st.success(row["typologie"])
    elif row["typologie"] == "Accompagnement prioritaire":
        st.error(row["typologie"])
    elif row["typologie"] == "Ressources à renforcer":
        st.warning(row["typologie"])
    elif row["typologie"] == "Priorité pédagogique":
        st.info(row["typologie"])
    else:
        st.warning(row["typologie"])
st.divider()
c1, c2, c3, c4 = st.columns(4)
c1.metric(
    "Résultats",
    f"{row['score_d1_resultats']:.1f}/100"
)
c2.metric(
    "Couverture",
    f"{row['score_d6_couverture']:.1f}/100"
)
c3.metric(
    "Mobilisation",
    f"{row['score_d3_mobilisation']:.1f}/100"
)
c4.metric(
    "Contraintes",
    f"{row['score_d7_contraintes']:.1f}/100"
)
st.divider()
left, right = st.columns([1.3, 1])
with left:
    st.subheader("📈 Radar des dimensions")
    categories = [
        "Résultats",
        "Disponibilité",
        "Mobilisation",
        "Enseignants",
        "Historique",
        "Couverture",
        "Contraintes"
    ]
    values = [
        row["score_d1_resultats"],
        row["score_d2_disponibilite"],
        row["score_d3_mobilisation"],
        row["score_d4_enseignants"],
        row["score_d5_historique"],
        row["score_d6_couverture"],
        row["score_d7_contraintes"]
    ]
    fig = go.Figure()
    fig.add_trace(
        go.Scatterpolar(
            r=values,
            theta=categories,
            fill="toself",
            name=row["nom_ecole"]
        )
    )
    fig.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, 100]
            )
        ),
        showlegend=False,
        height=500
    )
    st.plotly_chart(fig, use_container_width=True)
with right:
    st.subheader("📋 Profil détaillé")
    for dimension, infos in row["profil_detaille"].items():
        st.write(f"**{dimension}**")
        st.progress(infos["score"] / 100)
        st.caption(
            f"{infos['score']:.1f}/100 • {infos['niveau']}"
        )
st.divider()
st.subheader("🎯 Plan d'action recommandé")
for action in row["recommandations"]:
    st.info(action)
st.divider()
st.subheader("📄 Rapport décisionnel")
with st.expander("Afficher le rapport complet"):
    st.text(row["rapport"])
st.download_button(
    label="📥 Télécharger le rapport (.txt)",
    data=row["rapport"],
    file_name=f"rapport_{row['nom_ecole']}.txt",
    mime="text/plain"
)