import streamlit as st
import pickle
movies=pickle.load(open("movies_list.pkl",'rb'))
movies_list=movies['title'].values
st.header("Movie Recommender sytem")
st.selectbox("Select movie from dropdown",movies_list)