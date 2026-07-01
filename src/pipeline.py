import pandas as pd
import streamlit as st

from src.preprocessing import load_data, clean_data
from src.features import create_features
from src.scoring import (
    score_d1_results,
    score_d2_availability,
    score_d3_teacher_mobilization,
    score_d4_mobilized_teachers,
    score_d5_history,
    score_d6_coverage,
    score_d7_constraints,
    calculate_global_score
)
from src.profiling import (
    assign_typology,
    generate_profile
)
from src.recommendations import generate_recommendations
from src.reporting import generate_report


FILE_PATH = "data/Données fictives - Étude de Cas - Aymane.xlsx"

@st.cache_data
def load_pipeline():

    df = load_data(FILE_PATH)

    df = clean_data(df)

    df = create_features(df)

    df = score_d1_results(df)
    df = score_d2_availability(df)
    df = score_d3_teacher_mobilization(df)
    df = score_d4_mobilized_teachers(df)
    df = score_d5_history(df)
    df = score_d6_coverage(df)
    df = score_d7_constraints(df)

    df = calculate_global_score(df)

    df = assign_typology(df)

    df = generate_profile(df)

    df = generate_recommendations(df)

    df = generate_report(df)

    return df