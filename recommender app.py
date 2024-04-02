import streamlit as st
import pandas as pd
from pickle import load
import os

# Load Netflix dataframe
def load_data():
    folder_path = "D:/supriya/"  # Adjust this path to your folder
    netflix_cluster_path = os.path.join(folder_path, "netflix_content.sav")
    netflix_sim_df_path = os.path.join(folder_path, "netflix_sim_df.sav")
    
    netflix_cluster = load(open(netflix_cluster_path, 'rb'))
    netflix_sim_df = load(open(netflix_sim_df_path, 'rb'))
    
    return netflix_cluster, netflix_sim_df

# Provide movie recommendations
def provide_recommendation(netflix_cluster, netflix_sim_df, title):
    title_index = netflix_cluster.index[netflix_cluster['title'] == title][0]
    rec_index = list(netflix_sim_df.sort_values([title_index], ascending=False).iloc[1:11].index)       
    rec = [netflix_cluster.iloc[i]['title'] for i in rec_index]
    return rec

def main():
    st.title('Movie Recommender System')  # Web page title
    
    netflix_cluster, netflix_sim_df = load_data()  # Load data
    
    select_show = st.selectbox('Recommend Movies Like', netflix_cluster['title'].values, 
                               help="Select a movie to get recommendations")  # Dropdown of available Netflix titles
    
    if st.button('Recommend'):
        recommendations = provide_recommendation(netflix_cluster, netflix_sim_df, select_show)
        if recommendations:
            st.header("Recommendations for you:")
            for i, rec_movie in enumerate(recommendations, start=1):
                st.write(f"{i}. {rec_movie}")
        else:
            st.write("No recommendations found for the selected movie.")

if __name__ == "__main__":
    main()
