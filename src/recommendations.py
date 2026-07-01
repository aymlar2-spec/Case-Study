import pandas as pd

def generate_recommendations(df: pd.DataFrame) -> pd.DataFrame:
    """
    Génère des recommandations personnalisées
    à partir de la typologie et des sous-scores.
    """
    def recommendation(row):
        actions = []
        if row["typologie"] == "Prêt au déploiement":
            actions.append(
                "Maintenir les bonnes pratiques et capitaliser sur l'expérience de l'établissement."
            )
        elif row["typologie"] == "Priorité pédagogique":
            actions.append(
                "Mettre en œuvre un accompagnement pédagogique ciblé afin d'améliorer les acquis des élèves."
            )
        elif row["typologie"] == "Ressources à renforcer":
            actions.append(
                "Renforcer les ressources humaines et organisationnelles nécessaires au déploiement du soutien."
            )
        elif row["typologie"] == "Contraintes opérationnelles":
            actions.append(
                "Prévoir un accompagnement spécifique tenant compte des contraintes locales."
            )
        else:
            actions.append(
                "Mettre en place un plan d'accompagnement global avant le déploiement du dispositif."
            )
        if row["score_d1_resultats"] < 50:
            actions.append(
                "Renforcer les activités pédagogiques ciblées pour améliorer les résultats d'apprentissage."
            )
        if row["score_d2_disponibilite"] < 40:
            actions.append(
                "Augmenter le nombre de créneaux ou optimiser l'utilisation des salles disponibles."
            )
        if row["score_d3_mobilisation"] < 50:
            actions.append(
                "Sensibiliser et mobiliser davantage les enseignants."
            )
        if row["score_d4_enseignants"] < 40:
            actions.append(
                "Identifier et former davantage d'enseignants pour participer au soutien."
            )
        if row["score_d5_historique"] < 50:
            actions.append(
                "Mettre en place un meilleur suivi et une évaluation du dispositif de soutien."
            )
        if row["score_d6_couverture"] < 60:
            actions.append(
                "Étendre progressivement la couverture afin d'atteindre davantage d'élèves éligibles."
            )
        if row["score_d7_contraintes"] < 60:
            actions.append(
                "Prévoir un accompagnement spécifique lié aux contraintes d'enclavement, d'absentéisme ou de turnover."
            )
        if len(actions) == 1 and row["typologie"] == "Prêt au déploiement":
            actions.append(
                "Poursuivre le suivi des indicateurs afin de maintenir le niveau de performance."
            )
        return actions
    df["recommandations"] = df.apply(recommendation, axis=1)
    return df