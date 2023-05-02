import streamlit as st
import pandas as pd
from database import *


def update_sport():
    result = view_all_sports()
    df = pd.DataFrame(result, columns=["Sports Id", "Sports name", "Category"])
    with st.expander("Current Sports"):
        st.dataframe(df)

    list_of_sports_id = [i[0] for i in view_only_sport_id()]

    selected_sports = st.selectbox("Sport to edit", list_of_sports_id)
    selected_result = get_sport_id(selected_sports)
    if selected_result:
        Sid = selected_result[0][0]
        Sname = selected_result[0][1]
        Category = selected_result[0][2]

        col1, col2 = st.columns(2)
        with col1:
            new_sport_id = st.text_input("Sports Id", Sid)
            new_sport_name = st.text_input("Sports Name", Sname)

        with col2:
            new_category = st.selectbox("Category", ["Men", "Women"])

        if st.button("Update Sports"):
            edit_sport(new_sport_id, new_sport_name, new_category, Sid, Sname, Category)
            st.success("Successfully updated values of tuple")
            st.success("Old values -----> Sports Id = {}, Sports Name = {}, Category = {}".format(selected_result[0][0],
                                                                                                  selected_result[0][1],
                                                                                                  selected_result[0][
                                                                                                      2]))
            st.success(
                "Updated -----> Sports Id = {}, Sports Name = {}, Category = {}".format(new_sport_id, new_sport_name,
                                                                                        new_category))

    result2 = view_all_sports()
    df2 = pd.DataFrame(result2, columns=["Sports Id", "Sports name", "Category"])
    with st.expander("Sports table after Updating"):
        st.dataframe(df2)


def update_coach():
    result = view_all_coaches()
    df = pd.DataFrame(result, columns=["Coach Id", "Coach Name", "Phone no", "Address", "Specialization"])
    with st.expander("Current Coaches"):
        st.dataframe(df)

    list_of_coach_id = [i[0] for i in view_only_coach_id()]

    selected_coaches = st.selectbox("Coach to edit", list_of_coach_id)
    selected_result = get_coach_id(selected_coaches)
    if selected_result:
        Cid = selected_result[0][0]
        Cname = selected_result[0][1]
        Ph_no = selected_result[0][2]
        Address = selected_result[0][3]
        Specialized_in = selected_result[0][4]

        col1, col2 = st.columns(2)
        with col1:
            new_coach_id = st.text_input("Coach Id", Cid)
            new_coach_name = st.text_input("Coach Name", Cname)
            new_coach_phno = st.text_input("Phone Number", Ph_no)

        with col2:
            new_coach_address = st.text_area("Address", Address)
            new_coach_specialization = st.text_input("Specialization", Specialized_in)

        if st.button("Update Coach"):
            edit_coach(new_coach_id, new_coach_name, new_coach_phno, new_coach_address, new_coach_specialization, Cid,
                       Cname, Ph_no, Address, Specialized_in)
            st.success("Successfully updated values of tuple")
            st.success(
                "Old values -----> Coach Id = {}, Coach Name = {}, Phone no = {}, Address = {}, Specialized_in = {}".format(
                    selected_result[0][0], selected_result[0][1], selected_result[0][2], selected_result[0][3],
                    selected_result[0][4]))
            st.success(
                "Updated values -----> Coach Id = {}, Coach Name = {}, Phone no = {}, Address = {}, Specialized_in = {}".format(
                    new_coach_id, new_coach_name, new_coach_phno, new_coach_address, new_coach_specialization))

    result2 = view_all_coaches()
    df2 = pd.DataFrame(result2, columns=["Coach Id", "Coach Name", "Phone no", "Address", "Specialization"])
    with st.expander("Coach table after Updating"):
        st.dataframe(df2)


def update_league():
    result = view_all_leagues()
    df = pd.DataFrame(result, columns=["League Id", "League name"])
    with st.expander("Current Leagues"):
        st.dataframe(df)

    list_of_league_id = [i[0] for i in view_only_league_id()]

    selected_league = st.selectbox("League to edit", list_of_league_id)
    selected_result = get_league_id(selected_league)
    if selected_result:
        Lid = selected_result[0][0]
        Lname = selected_result[0][1]

        col1, col2 = st.columns(2)
        with col1:
            new_league_id = st.text_input("League Id", Lid)

        with col2:
            new_league_name = st.text_input("League Name", Lname)

        if st.button("Update League"):
            edit_league(new_league_id, new_league_name, Lid, Lname)
            st.success("Successfully updated values of tuple")
            st.success("Old values -----> League Id = {}, League Name = {}".format(selected_result[0][0],
                                                                                   selected_result[0][1]))
            st.success("Updated -----> League Id = {}, League Name = {}".format(new_league_id, new_league_name))

    result2 = view_all_leagues()
    df2 = pd.DataFrame(result2, columns=["League Id", "League name"])
    with st.expander("League table after Updating"):
        st.dataframe(df2)


def update_matches():
    result = view_all_matches()
    df = pd.DataFrame(result, columns=["Match Id", "Team1", "Team2", "Refree", "Location", "League Id"])
    with st.expander("Current Matches"):
        st.dataframe(df)

    list_of_match_id = [i[0] for i in view_only_match_id()]

    selected_match = st.selectbox("Match to edit", list_of_match_id)
    selected_result = get_match_id(selected_match)
    if selected_result:
        Mid = selected_result[0][0]
        Team1 = selected_result[0][1]
        Team2 = selected_result[0][2]
        Refree = selected_result[0][3]
        Location = selected_result[0][4]
        Lid = selected_result[0][5]

        col1, col2 = st.columns(2)
        with col1:
            new_match_id = st.text_input("Match Id", Mid)
            new_team1 = st.text_input("Team1", Team1)
            new_team2 = st.text_input("Team2", Team2)

        with col2:
            new_refree = st.text_input("Refree", Refree)
            new_location = st.text_input("Location", Location)
            new_lid = st.text_input("League Id", Lid)

        if st.button("Update Match"):
            edit_match(new_match_id, new_team1, new_team2, new_refree, new_location, new_lid, Mid, Team1, Team2, Refree,
                       Location, Lid)
            st.success("Successfully updated values of tuple")
            st.success(
                "Old values -----> Match Id = {}, Team1 = {}, Team2 = {}, Refree = {}, Location = {}, League Id = {}".format(
                    selected_result[0][0], selected_result[0][1], selected_result[0][2], selected_result[0][3],
                    selected_result[0][4], selected_result[0][5]))
            st.success(
                "Updated values -----> Match Id = {}, Team1 = {}, Team2 = {}, Refree = {}, Location = {}, League Id  = {}".format(
                    new_match_id, new_team1, new_team2, new_refree, new_location, new_lid))

    result2 = view_all_matches()
    df2 = pd.DataFrame(result2, columns=["Match Id", "Team1", "Team2", "Refree", "Location", "League Id"])
    with st.expander("Match table after Updating"):
        st.dataframe(df2)


def update_teams():
    result = view_all_teams()
    df = pd.DataFrame(result,
                      columns=["Team Id", "Team Name", "Captain", "No of players", "Sports Id", "Coach Id", "Match Id",
                               "League Id"])
    with st.expander("Current Teams"):
        st.dataframe(df)

    list_of_team_id = [i[0] for i in view_only_team_id()]

    selected_teams = st.selectbox("Team to edit", list_of_team_id)
    selected_result = get_team_id(selected_teams)
    if selected_result:
        Tid = selected_result[0][0]
        Tname = selected_result[0][1]
        Captain = selected_result[0][2]
        No_of_players = selected_result[0][3]
        Sid = selected_result[0][4]
        Cid = selected_result[0][5]
        Mid = selected_result[0][6]
        Lid = selected_result[0][7]

        col1, col2 = st.columns(2)
        with col1:
            new_Tid = st.text_input("Team Id", Tid)
            new_Tname = st.text_input("Team Name", Tname)
            new_captain = st.text_input("Capatain", Captain)
            new_no_of_players = st.text_input("No of players", No_of_players)

        with col2:
            new_sid = st.text_input("Sports Id", Sid)
            new_cid = st.text_input("Coach Id", Cid)
            new_mid = st.text_input("Match Id", Mid)
            new_lid = st.text_input("League Id", Lid)

        if st.button("Update Teams"):
            edit_team(new_Tid, new_Tname, new_captain, new_no_of_players, new_sid, new_cid, new_mid, new_lid, Tid,
                      Tname, Captain, No_of_players, Sid, Cid, Mid, Lid)
            st.success("Successfully updated values of tuple")
            st.success(
                "Old values -----> Team Id = {}, Team Name = {}, Captain = {}, No of players = {}, Sports Id = {}, Coach Id = {}, Match Id = {}, League Id = {}".format(
                    selected_result[0][0], selected_result[0][1], selected_result[0][2], selected_result[0][3],
                    selected_result[0][4], selected_result[0][5], selected_result[0][6], selected_result[0][7]))
            st.success(
                "Updated -----> Team Id = {}, Team Name = {}, Captain = {}, No of players = {}, Sports Id = {}, Coach Id = {}, Match Id = {}, League Id = {}".format(
                    new_Tid, new_Tname, new_captain, new_no_of_players, new_sid, new_cid, new_mid, new_lid))

    result2 = view_all_teams()
    df2 = pd.DataFrame(result2,
                       columns=["Team Id", "Team Name", "Captain", "No of players", "Sports Id", "Coach Id", "Match Id",
                                "League Id"])
    with st.expander("Teams table after Updating"):
        st.dataframe(df2)


def update_players():
    result = view_all_players()
    df = pd.DataFrame(result,
                      columns=["Player Id", "Firstname", "Lastname", "Date of birth", "Age", "Phone no", "Address",
                               "Coach Id", "Team Id"])
    with st.expander("Current Players"):
        st.dataframe(df)

    list_of_player_id = [i[0] for i in view_only_player_id()]

    selected_player = st.selectbox("Player to edit", list_of_player_id)
    selected_result = get_player_id(selected_player)
    if selected_result:
        Pid = selected_result[0][0]
        Fname = selected_result[0][1]
        Lname = selected_result[0][2]
        Dob = selected_result[0][3]
        Age = selected_result[0][4]
        Ph_no = selected_result[0][5]
        Address = selected_result[0][6]
        Cid = selected_result[0][7]
        Tid = selected_result[0][8]

        col1, col2 = st.columns(2)
        with col1:
            new_Pid = st.text_input("Player Id", Pid)
            new_Fname = st.text_input("Firstname", Fname)
            new_Lname = st.text_input("Lastname", Lname)
            new_Dob = st.text_input("Date of birth", Dob)
            new_Age = st.text_input("Ages", Age)

        with col2:
            new_Ph_no = st.text_input("Phone no", Ph_no)
            new_Address = st.text_input("Address", Address)
            new_cid = st.text_input("Coach Id", Cid)
            new_tid = st.text_input("Team Id", Tid)

        if st.button("Update Player"):
            edit_player(new_Pid, new_Fname, new_Lname, new_Dob, new_Age, new_Ph_no, new_Address, new_cid, new_tid, Pid,
                        Fname, Lname, Dob, Age, Ph_no, Address, Cid, Tid)
            st.success("Successfully updated values of tuple")
            st.success(
                "Old values -----> Player Id = {}, Firstname = {}, Lastname = {}, Date of birth = {}, Age = {}, Phone no = {}, Address = {}, Coach Id = {}, Team Id = {}".format(
                    selected_result[0][0], selected_result[0][1], selected_result[0][2], selected_result[0][3],
                    selected_result[0][4], selected_result[0][5], selected_result[0][6], selected_result[0][7],
                    selected_result[0][8]))
            st.success(
                "Updated -----> Player Id = {}, Firstname = {}, Lastname = {}, Date of birth = {}, Age = {}, Phone no = {}, Address = {}, Coach Id = {}, Team Id = {}".format(
                    new_Pid, new_Fname, new_Lname, new_Dob, new_Age, new_Ph_no, new_Address, new_cid, new_tid))

    result2 = view_all_players()
    df2 = pd.DataFrame(result2,
                       columns=["Player Id", "Firstname", "Lastname", "Date of birth", "Age", "Phone no", "Address",
                                "Coach Id", "Team Id"])
    with st.expander("Players table after Updating"):
        st.dataframe(df2)
