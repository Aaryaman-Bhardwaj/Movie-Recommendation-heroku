import streamlit as st
import pickle
import pandas as pd
import requests

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:11]
    recommended_movies = []
    posters = []
    for i in movies_list:
        title = movies.loc[i[0]].title
        id = movies.loc[i[0]].imdb_title_id
        recommended_movies.append(title)
        posters.append(callApi(id))
    return recommended_movies, posters

def callApi(id):
    url = "http://www.omdbapi.com/?i=" + id + "&apikey=6f243955"
    response = requests.request("GET", url)
    data = response.json()
    return data['Poster']

movies_dict = pickle.load(open('indian_movies_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl', 'rb'))

st.title("Recommender System")

selected_movie = st.selectbox("Select a  movie", movies['title'].values)

if st.button("Recommend"):
    recommendations, posters = recommend(selected_movie)
    print(recommendations)
    print(posters)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(recommendations[0])
        st.image(posters[0])
    with col2:
        st.text(recommendations[1])
        st.image(posters[1])

    with col3:
        st.text(recommendations[2])
        st.image(posters[2])
    with col4:
        st.text(recommendations[3])
        st.image(posters[3])
    with col5:
        st.text(recommendations[4])
        st.image(posters[4])