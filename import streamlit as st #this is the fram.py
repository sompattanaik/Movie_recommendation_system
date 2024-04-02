import streamlit as st #this is the framework in python that we will use to build app
import pickle 
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer
from imdb import IMDb 


similarity = pickle.load(open("D:\DS project\netflix project\recommendor_app\cosine_similarity.pkl", 'rb')) #loading our cosine_sim pickle file
movie_dict = pickle.load(open("D:\DS project\netflix project\recommendor_app\movie_dict.pkl", 'rb')) #loading our movie_dict file 
movies = pd.DataFrame(movie_dict)

programme_list=movies['title'].to_list()