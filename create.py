import datetime

import streamlit as st
from database import *


def create_sports():
    col1, col2 = st.columns(2)
    with col1:
        Sid = st.text_input("Sports Id")
        Sname = st.text_input("Sports Name")

    with col2:
        Category = st.selectbox("Category", ["Men", "Women"])

    if st.button("Add Sport"):
        add_data_sports(Sid, Sname, Category)
        st.success("successfully added Sport: {}".format(Sname))


def create_coach():
    col1, col2 = st.columns(2)
    with col1:
        Cid = st.text_input("Coach Id")
        Cname = st.text_input("Coach Name")
        Ph_no = st.text_input("Phone Number")

    with col2:
        Address = st.text_area("Address")
        Specialized_in = st.text_input("Specialization")

    if st.button("Add Coach"):
        add_data_coach(Cid, Cname, Ph_no, Address, Specialized_in)
        st.success("successfully added Coach: {}".format(Cname))


def create_league():
    col1, col2 = st.columns(2)
    with col1:
        Lid = st.text_input("League Id")

    with col2:
        Lname = st.text_input("League Name")

    if st.button("Add League"):
        add_data_league(Lid, Lname)
        st.success("successfully added League: {}".format(Lname))


def create_matches():
    col1, col2 = st.columns(2)
    with col1:
        Mid = st.text_input("Match Id")
        Team1 = st.text_input("Team 1")
        Team2 = st.text_input("Team 2")

    with col2:
        Refree = st.text_input("Refree")
        Location = st.text_input("Location")
        Lid = st.text_input("League Id")

    if st.button("Add Match"):
        add_data_matches(Mid, Team1, Team2, Refree, Location, Lid)
        st.success("successfully added Match with id: {}".format(Mid))


def create_teams():
    col1, col2 = st.columns(2)
    with col1:
        Tid = st.text_input("Team Id")
        Tname = st.text_input("Team Name")
        Captain = st.text_input("Captain")
        No_of_players = st.text_input("Number of players")

    with col2:
        Sid = st.text_input("Sports Id")
        Cid = st.text_input("Coach Id")
        Mid = st.text_input("Match Id")
        Lid = st.text_input("League Id")

    if st.button("Add Teams"):
        add_data_teams(Tid, Tname, Captain, No_of_players, Sid, Cid, Mid, Lid)
        st.success("successfully added Team: {}".format(Tname))


def create_players():
    col1, col2 = st.columns(2)
    with col1:
        Pid = st.text_input("Player Id")
        Fname = st.text_input("Firstname")
        Lname = st.text_input("Lastname")
        Dob = st.date_input(label="Date of birth", min_value=datetime.date(1990, 1, 1), max_value=datetime.datetime.now())
        Age = st.text_input("Age")

    with col2:
        Ph_no = st.text_input("Phone Number")
        Address = st.text_area("Address")
        Cid = st.text_input("Coach Id")
        Tid = st.text_input("Team Id")

    if st.button("Add Teams"):
        add_data_players(Pid, Fname, Lname, Dob, Age, Ph_no, Address, Cid, Tid)
        st.success("successfully added Player: {} {}".format(Fname, Lname))
