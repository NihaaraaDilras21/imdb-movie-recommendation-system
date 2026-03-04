import streamlit as st
from recommendation import recommend, df

st.set_page_config(page_title="Movie Recommender", page_icon="🎬")

st.title("🎬 Movie Recommendation System")

# 🔎 Search functionality
search_query = st.text_input("Search for a movie:")

movie_list = df["Movie Name"].tolist()

if search_query:
    filtered_movies = [movie for movie in movie_list if search_query.lower() in movie.lower()]
else:
    filtered_movies = movie_list

selected_movie = st.selectbox("Select a movie:", filtered_movies)

if st.button("Recommend"):
    
    # Show selected movie storyline
    storyline = df[df["Movie Name"] == selected_movie]["Storyline"].values[0]
    
    st.subheader("📖 Storyline:")
    st.write(storyline)
    
    # Get recommendations
    recommendations = recommend(selected_movie)
    
    st.subheader("🎯 Recommended Movies:")
    
    for movie, _ in recommendations:
    
      rec_storyline = df[df["Movie Name"] == movie]["Storyline"].values[0]
    
      with st.container():
          st.markdown(f"### 🎬 {movie}")
          st.write(rec_storyline)
          st.divider()