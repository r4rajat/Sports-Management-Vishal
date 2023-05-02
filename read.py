import streamlit as st
import pandas as pd
from database import *


def read_sports():
    result = view_all_sports()
    df = pd.DataFrame(result, columns=["Sports Id", "Sports name", "Category"])
    with st.expander("View all Sports"):
        st.dataframe(df)


def read_coach():
    result = view_all_coaches()
    df = pd.DataFrame(result, columns=["Coach Id", "Coach Name", "Phone no", "Address", "Specialization"])
    with st.expander("View all Coaches"):
        st.dataframe(df)


def read_leagues():
    result = view_all_leagues()
    df = pd.DataFrame(result, columns=["League Id", "League name"])
    with st.expander("View all Leagues"):
        st.dataframe(df)


def read_matches():
    result = view_all_matches()
    df = pd.DataFrame(result, columns=["Match Id", "Team1", "Team2", "Refree", "Location", "League Id"])
    with st.expander("View all Matches"):
        st.dataframe(df)


def read_teams():
    result = view_all_teams()
    df = pd.DataFrame(result,
                      columns=["Team Id", "Team Name", "Captain", "No of players", "Sports Id", "Coach Id", "Match Id",
                               "League Id"])
    with st.expander("View all Teams"):
        st.dataframe(df)


def read_players():
    result = view_all_players()
    df = pd.DataFrame(result,
                      columns=["Player Id", "Firstname", "Lastname", "Date of birth", "Age", "Phone no", "Address",
                               "Coach Id", "Team Id"])
    with st.expander("View all Players"):
        st.dataframe(df)
