import streamlit as st
import plotly.graph_objects as go
from src.pipeline import load_pipeline
st.caption("Direction Provinciale • Outil d'aide à la décision")
st.title("⚖️ Comparaison de deux établissements")
df = load_pipeline()
col1, col2 = st.columns(2)
with col1:
    ecole1 = st.selectbox(
        "Premier établissement",
        sorted(df["nom_ecole"].unique()),
        key="ecole1"
    )
with col2:
    ecole2 = st.selectbox(
        "Deuxième établissement",
        sorted(df["nom_ecole"].unique()),
        index=1,
        key="ecole2"
    )
row1 = df[df["nom_ecole"] == ecole1].iloc[0]
row2 = df[df["nom_ecole"] == ecole2].iloc[0]
st.divider()
left, right = st.columns(2)
with left:
    st.subheader(ecole1)
    st.write(f"**Province :** {row1['province']}")
    st.write(f"**Type :** {row1['type_ecole']}")
    st.write(f"**Milieu :** {row1['milieu']}")
    st.write(f"**Typologie :** {row1['typologie']}")
with right:
    st.subheader(ecole2)
    st.write(f"**Province :** {row2['province']}")
    st.write(f"**Type :** {row2['type_ecole']}")
    st.write(f"**Milieu :** {row2['milieu']}")
    st.write(f"**Typologie :** {row2['typologie']}")
st.divider()
categories = [
    "Résultats",
    "Disponibilité",
    "Mobilisation",
    "Enseignants",
    "Historique",
    "Couverture",
    "Contraintes"
]
scores1 = [
    row1["score_d1_resultats"],
    row1["score_d2_disponibilite"],
    row1["score_d3_mobilisation"],
    row1["score_d4_enseignants"],
    row1["score_d5_historique"],
    row1["score_d6_couverture"],
    row1["score_d7_contraintes"]
]
scores2 = [
    row2["score_d1_resultats"],
    row2["score_d2_disponibilite"],
    row2["score_d3_mobilisation"],
    row2["score_d4_enseignants"],
    row2["score_d5_historique"],
    row2["score_d6_couverture"],
    row2["score_d7_contraintes"]
]
fig = go.Figure()
fig.add_trace(
    go.Scatterpolar(
        r=scores1,
        theta=categories,
        fill="toself",
        name=ecole1
    )
)
fig.add_trace(
    go.Scatterpolar(
        r=scores2,
        theta=categories,
        fill="toself",
        name=ecole2
    )
)
fig.update_layout(
    polar=dict(
        radialaxis=dict(
            visible=True,
            range=[0, 100]
        )
    ),
    height=650
)
st.plotly_chart(fig, use_container_width=True)
st.divider()
comparison = {
    "Dimension": categories,
    ecole1: [round(x, 1) for x in scores1],
    ecole2: [round(x, 1) for x in scores2]
}
st.subheader("Comparaison des dimensions")
st.dataframe(
    comparison,
    use_container_width=True,
    hide_index=True
)
st.divider()
left, right = st.columns(2)
with left:
    st.subheader(f"Plan d'action - {ecole1}")
    for action in row1["recommandations"]:
        st.info(action)
with right:
    st.subheader(f"Plan d'action - {ecole2}")
    for action in row2["recommandations"]:
        st.info(action)