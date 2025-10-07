import streamlit as st
import joblib
import numpy as np
import pandas as pd

# === Load the trained model ===
model = joblib.load("xgb_xg_diff_with_teams.pkl")

# === Define the UI ===
st.title("📊 Brasileirão xG Difference Predictor")

st.write("""
Enter the trailing xG stats and select the teams to get a prediction for **xG Difference (Home - Away)**.
""")

# === Define input options ===
# NOTE: Replace this list with the actual teams used during training for full accuracy
teams = sorted([        'Cruzeiro',         'Flamengo',        'Fortaleza',
           'Grêmio',        'Juventude',        'São Paulo',
            'Bahia',        'Palmeiras',    'Vasco da Gama',
    'RB Bragantino',    'Botafogo (RJ)',            'Ceará',
      'Corinthians', 'Atlético Mineiro',       'Fluminense',
    'Internacional',         'Mirassol',           'Santos',
     'Sport Recife',          'Vitória'])

home_team = st.selectbox("🏠 Home Team", teams)
away_team = st.selectbox("🛫 Away Team", teams)

# Prevent user from selecting same team
if home_team == away_team:
    st.warning("Home and Away teams cannot be the same.")

# Numerical input fields
home_xg_trailing = st.number_input("Home xG Trailing (avg xG in recent games)", value=1.0, step=0.1)
home_xga_trailing = st.number_input("Home xGA Trailing (avg xGA in recent games)", value=1.0, step=0.1)
away_xg_trailing = st.number_input("Away xG Trailing (avg xG in recent games)", value=1.0, step=0.1)
away_xga_trailing = st.number_input("Away xGA Trailing (avg xGA in recent games)", value=1.0, step=0.1)

# === Make prediction ===
if st.button("🔮 Predict xG Difference"):
    if home_team == away_team:
        st.error("Please select different teams.")
    else:
        # Create a single-row DataFrame to match the training input
        input_df = pd.DataFrame([{
            'home_team': home_team,
            'away_team': away_team,
            'home_xg_trailing': home_xg_trailing,
            'home_xga_trailing': home_xga_trailing,
            'away_xg_trailing': away_xg_trailing,
            'away_xga_trailing': away_xga_trailing
        }])

        # Predict using the pipeline (which includes preprocessing)
        prediction = model.predict(input_df)[0]

        st.success(f"📈 Predicted xG Difference (Home - Away): {prediction:.2f}")
