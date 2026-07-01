# 📊 Decision Support System for School Prioritization

## Overview

This project was developed as part of a technical case study to design a Decision Support System (DSS) for prioritizing schools eligible for the deployment of an educational support program.

Instead of producing a simple ranking, the application evaluates each school across multiple complementary dimensions, assigns an automatic typology, and generates decision-oriented recommendations to support educational authorities.

---

## Objectives

- Clean and preprocess educational data.
- Build meaningful indicators.
- Compute a multidimensional scoring model.
- Generate a complete profile for each school.
- Automatically assign a school typology.
- Produce tailored recommendations.
- Provide an interactive dashboard for decision-makers.

---

## Technologies

- Python
- Pandas
- Scikit-learn
- Plotly
- Streamlit
- OpenPyXL

---

## Project Structure

```
Case_Study/
│
├── .streamlit/
│   └── config.toml
│
├── assets/
│
├── data/
│
├── pages/
│   ├── dashboard.py
│   ├── school_analysis.py
│   ├── comparison.py
│   └── methodology.py
│
├── src/
│   ├── preprocessing.py
│   ├── features.py
│   ├── scoring.py
│   ├── profiling.py
│   ├── recommendations.py
│   ├── reporting.py
│   └── pipeline.py
│
├── app.py
├── requirements.txt
└── README.md
```

---

## Decision Model

The decision model evaluates schools using seven complementary dimensions:

| Dimension | Description |
|-----------|-------------|
| D1 | Learning outcomes |
| D2 | Resource availability |
| D3 | Teacher mobilization |
| D4 | Mobilized teaching staff |
| D5 | Previous support experience |
| D6 | Support coverage |
| D7 | Operational constraints |

Each dimension is independently scored on a scale from **0 to 100**.

A weighted global score is also computed as a synthesis indicator, while decision-making primarily relies on the multidimensional profile and the automatically assigned typology.

---

## Application Features

### 📊 Dashboard

- Interactive filters
- Key performance indicators
- Typology distribution
- Average scores by dimension
- Interactive data table

### 🏫 School Analysis

- School profile
- Radar chart
- Detailed dimension analysis
- Automatic recommendations
- Decision report

### ⚖️ School Comparison

- Comparison of two schools
- Radar comparison
- Comparative scores
- Recommended actions

### 📘 Methodology

- Scoring approach
- Typology rules
- Decision model explanation

---

## Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git
```

Go to the project folder:

```bash
cd YOUR_REPOSITORY
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
streamlit run app.py
```

---

## Author

**Ayman Largou**

Engineering Student

Decision Support System • Educational Data Analytics