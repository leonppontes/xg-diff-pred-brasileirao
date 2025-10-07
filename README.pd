# 🇧🇷 xG Brasileirão Predictor

[![Streamlit App](https://img.shields.io/badge/Live%20App-Streamlit-brightgreen?logo=streamlit)](https://xgbrasileirao.streamlit.app/)

Welcome to the **xG Brasileirão Predictor** — a simple and powerful web app that uses **machine learning and expected goals (xG)** data to estimate the difference in scoring chances between home and away teams in Brazilian Série A matches.

You can try the app live here:  
👉 [https://xgbrasileirao.streamlit.app/](https://xgbrasileirao.streamlit.app/)

---

## 🎯 What Does This App Do?

This app allows you to:
- Select two teams from the 2025 Brasileirão Série A
- Enter recent expected goal (xG) stats for both teams
- Instantly see the predicted **xG difference** (home - away), using a trained **XGBoost regression model**

It’s a data-driven way to preview how two teams might perform based on their recent attacking and defensive trends.

---

## ⚽ What Is Expected Goal (xG)?

**Expected Goals (xG)** is a metric that estimates the quality of a scoring chance, based on historical shot data.

Instead of just looking at the final score, xG answers:
> *"How many goals were the teams **expected** to score based on the quality of their chances?"*

This makes it a **more accurate reflection of performance** than the final score, which can be affected by luck, great goalkeeping, or missed sitters.

### Why Use xG?
- It shows how well a team **created and defended chances**
- It smooths out randomness in results
- It helps compare teams beyond just wins/losses

---

## 📚 Data Source — `soccerdata` Library

This project uses the [`soccerdata`](https://pypi.org/project/soccerdata/) Python library to collect historical match data and advanced stats, including xG, for the **Brasileirão Série A 2025 season**.

`soccerdata` is an excellent tool for downloading structured football data from multiple sources like FBref, Understat, and FiveThirtyEight.

---

## 📊 Features and Target

The machine learning model was trained using data from past matches with the following:

### 🧮 Input Features
- `home_team`: Name of the home team
- `away_team`: Name of the away team
- `home_xg_trailing`: Average expected goals for the home team in last 3 games
- `home_xga_trailing`: Average expected goals against the home team in last 3 games
- `away_xg_trailing`: Average expected goals for the away team in last 3 games
- `away_xga_trailing`: Average expected goals against the away team in last 3 games

### 🎯 Target Variable
- `xg_difference`: The difference between home and away xG (`home_xg - away_xg`), representing the predicted quality gap between teams.

---

## 🚀 How to Use the App

1. **Visit the app**:  
   👉 [https://xgbrasileirao.streamlit.app/](https://xgbrasileirao.streamlit.app/)

2. **Choose the home and away teams** from the dropdowns.

3. **Enter the recent xG and xGA averages** for each team — these can be computed from recent matches.

4. Click **"Predict xG Difference"** to instantly see the model’s prediction.

   > Positive values mean the home team is expected to perform better; negative values favor the away team.

---

## 💡 Example Use Cases
- Pre-match tactical analysis
- Betting strategy research
- Fantasy football decision-making
- Comparing performance beyond final scores

---

## 🧠 Model Info

- Model: `XGBoost Regressor`
- Preprocessing: `OneHotEncoding` for team names, numeric features passed directly
- Tuning: `RandomizedSearchCV` with hundreds of hyperparameter combinations
- Exported: Entire pipeline (preprocessing + model) saved using `joblib`



---

## 🤝 Acknowledgements

- [`soccerdata`](https://github.com/RobMulla/soccerdata) for football data scraping
- [Streamlit](https://streamlit.io) for building quick interactive apps
- [XGBoost](https://xgboost.ai/) for scalable and fast machine learning

