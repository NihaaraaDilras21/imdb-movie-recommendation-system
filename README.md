# 🎬 Movie Recommendation System

A content-based movie recommendation system built using:

- Python
- Selenium (Web Scraping)
- Pandas
- TF-IDF Vectorization
- Cosine Similarity
- Streamlit (Web App)

## 📌 Features
- Scrapes IMDb movie data
- Uses NLP to compute similarity between storylines
- Recommends top 5 similar movies
- Interactive Streamlit UI
- Search functionality

## 🧠 How It Works
1. Movie storylines are converted into TF-IDF vectors.
2. Cosine similarity is computed between movies.
3. Top similar movies are recommended.

## 🚀 Run Locally

```bash
pip install -r requirements.txt
streamlit run app.py
