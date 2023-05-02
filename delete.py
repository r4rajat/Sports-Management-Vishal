import streamlit as st
import pandas as pd
from database import *


def delete_sport():
    all_sports = view_all_sports()
    df = pd.DataFrame(all_sports, columns=['Sports Id', 'Sports Name', 'Category'])
    with st.expander("Current data"):
        st.dataframe(df)

    list_of_sports = [i[0] for i in view_only_sport_id()]

    selected_sport = st.selectbox("Sport to delete", list_of_sports)
    st.warning("Do you want to delete sport {}?".format(selected_sport))
    if st.button("Delete selected sport"):
        delete_sport_data(selected_sport)
        st.success("Sport {} deleted successfully".format(selected_sport))
        after_delete = view_all_sports()
        df2 = pd.DataFrame(after_delete, columns=['Sid', 'Sname', 'Category'])
        with st.expander("After deleting the selected sport"):
            st.dataframe(df2)


def delete_coach():
    all_coaches = view_all_coaches()
    df = pd.DataFrame(all_coaches, columns=['Coach Id', 'Coach name', 'Phone no', 'Address', 'Specialization'])
    with st.expander("Current data"):
        st.dataframe(df)

    list_of_coaches = [i[0] for i in view_only_coach_id()]

    selected_coach = st.selectbox("Coach to delete", list_of_coaches)
    st.warning("Do you want to delete coach {}?".format(selected_coach))
    if st.button("Delete selected Coach"):
        delete_coach_data(selected_coach)
        st.success("Coach {} deleted successfully".format(selected_coach))
        after_delete = view_all_coaches()
        df2 = pd.DataFrame(after_delete, columns=['Coach Id', 'Coach name', 'Phone no', 'Address', 'Specialization'])
        with st.expander("After deleting the selected coach"):
            st.dataframe(df2)


def delete_league():
    all_leagues = view_all_leagues()
    df = pd.DataFrame(all_leagues, columns=['League Id', 'League name'])
    with st.expander("Current data"):
        st.dataframe(df)

    list_of_leagues = [i[0] for i in view_only_league_id()]

    selected_league = st.selectbox("League to delete", list_of_leagues)
    st.warning("Do you want to delete League {}?".format(selected_league))
    if st.button("Delete selected League"):
        delete_league_data(selected_league)
        st.success("League {} deleted successfully".format(selected_league))
        after_delete = view_all_leagues()
        df2 = pd.DataFrame(after_delete, columns=['League Id', 'League name'])
        with st.expander("After deleting the selected league"):
            st.dataframe(df2)


def delete_match():
    all_matches = view_all_matches()
    df = pd.DataFrame(all_matches, columns=['Match Id', 'Team1', 'Team2', 'Refree', 'Location', 'League Id'])
    with st.expander("Current data"):
        st.dataframe(df)

    list_of_matches = [i[0] for i in view_only_match_id()]

    selected_match = st.selectbox("Match to delete", list_of_matches)
    st.warning("Do you want to delete match {}?".format(selected_match))
    if st.button("Delete selected Match"):
        delete_match_data(selected_match)
        st.success("Match {} deleted successfully".format(selected_match))
        after_delete = view_all_matches()
        df2 = pd.DataFrame(after_delete, columns=['Match Id', 'Team1', 'Team2', 'Refree', 'Location', 'League Id'])
        with st.expander("After deleting the selected match"):
            st.dataframe(df2)


def delete_team():
    all_teams = view_all_teams()
    df = pd.DataFrame(all_teams,
                      columns=['Team Id', 'Team Name', 'Captain', 'No of players', 'Sports Id', 'Coach Id', 'Match Id',
                               'League Id'])
    with st.expander("Current data"):
        st.dataframe(df)

    list_of_teams = [i[0] for i in view_only_team_id()]

    selected_team = st.selectbox("Team to delete", list_of_teams)
    st.warning("Do you want to delete Team {}?".format(selected_team))
    if st.button("Delete selected Team"):
        delete_team_data(selected_team)
        st.success("Team {} deleted successfully".format(selected_team))
        after_delete = view_all_teams()
        df2 = pd.DataFrame(after_delete,
                           columns=['Team Id', 'Team Name', 'Captain', 'No of players', 'Sports Id', 'Coach Id',
                                    'Match Id', 'League Id'])
        with st.expander("After deleting the selected Team"):
            st.dataframe(df2)


def delete_player():
    all_players = view_all_players()
    df = pd.DataFrame(all_players,
                      columns=['Player Id', 'Firstname', 'Lastname', 'Date of birth', 'Age', 'Phone no', 'Address',
                               'Coach Id', 'Team Id'])
    with st.expander("Current data"):
        st.dataframe(df)

    list_of_players = [i[0] for i in view_only_player_id()]

    selected_player = st.selectbox("Player to delete", list_of_players)
    st.warning("Do you want to delete Player {}?".format(selected_player))
    if st.button("Delete selected Player"):
        delete_player_data(selected_player)
        st.success("Player {} deleted successfully".format(selected_player))
        after_delete = view_all_players()
        df2 = pd.DataFrame(after_delete,
                           columns=['Player Id', 'Firstname', 'Lastname', 'Date of birth', 'Age', 'Phone no', 'Address',
                                    'Coach Id', 'Team Id'])
        with st.expander("After deleting the selected Player"):
            st.dataframe(df2)
