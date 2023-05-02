import streamlit as st
from database import *
from create import *
from read import *
from update import *
from delete import *


def main():
    st.image("https://www.educationportal.mp.gov.in/ApplicantRegistration/Image/banners.png")
    st.markdown("<h1 style='text-align:center';>Sports Management Database System</h1>", unsafe_allow_html=True)

    table = ["Sports", "Coach", "League", "Match", "Teams", "Players"]
    choice = st.sidebar.selectbox("Table", table)

    if choice == "Sports":
        st.subheader("Sports Table")
        crud = ["Create", "Read", "Update", "Delete"]
        choice = st.sidebar.selectbox("Operations", crud)

        create_table_sports()
        if choice == "Create":
            st.subheader("Add Sports")
            create_sports()

        elif choice == "Read":
            st.subheader("View Sports")
            read_sports()

        elif choice == "Update":
            st.subheader("Edit/Update Sports")
            update_sport()

        else:
            st.subheader("Delete Sports")
            delete_sport()

    if choice == "Coach":
        st.subheader("Coach Table")
        crud = ["Create", "Read", "Update", "Delete"]
        choice = st.sidebar.selectbox("Operations", crud)

        create_table_coach()
        if choice == "Create":
            st.subheader("Add Coach")
            create_coach()

        elif choice == "Read":
            st.subheader("View Coach")
            read_coach()

        elif choice == "Update":
            st.subheader("Edit/Update Coach")
            update_coach()

        else:
            st.subheader("Delete Coach")
            delete_coach()

    if choice == "League":
        st.subheader("League Table")
        crud = ["Create", "Read", "Update", "Delete"]
        choice = st.sidebar.selectbox("Operations", crud)

        create_table_league()
        if choice == "Create":
            st.subheader("Add League")
            create_league()

        elif choice == "Read":
            st.subheader("View League")
            read_leagues()

        elif choice == "Update":
            st.subheader("Edit/Update League")
            update_league()

        else:
            st.subheader("Delete League")
            delete_league()

    if choice == "Match":
        st.subheader("Match Table")
        crud = ["Create", "Read", "Update", "Delete"]
        choice = st.sidebar.selectbox("Operations", crud)

        create_table_matches()
        if choice == "Create":
            st.subheader("Add Match")
            create_matches()

        elif choice == "Read":
            st.subheader("View Match")
            read_matches()

        elif choice == "Update":
            st.subheader("Edit/Update Match")
            update_matches()

        else:
            st.subheader("Delete Match")
            delete_match()

    if choice == "Teams":
        st.subheader("Teams Table")
        crud = ["Create", "Read", "Update", "Delete"]
        choice = st.sidebar.selectbox("Operations", crud)

        create_table_teams()
        if choice == "Create":
            st.subheader("Add Team")
            create_teams()

        elif choice == "Read":
            st.subheader("View Team")
            read_teams()

        elif choice == "Update":
            st.subheader("Edit/Update Team")
            update_teams()

        else:
            st.subheader("Delete Team")
            delete_team()

    if choice == "Players":
        st.subheader("Players Table")
        crud = ["Create", "Read", "Update", "Delete"]
        choice = st.sidebar.selectbox("Operations", crud)

        create_table_players()
        if choice == "Create":
            st.subheader("Add Players")
            create_players()

        elif choice == "Read":
            st.subheader("View Players")
            read_players()

        elif choice == "Update":
            st.subheader("Edit/Update Players")
            update_players()

        else:
            st.subheader("Delete Players")
            delete_player()

    st.sidebar.write("")
    st.sidebar.write("")
    st.sidebar.write("")
    st.sidebar.write("")
    st.sidebar.write("")
    st.sidebar.write("")
    st.sidebar.write("")
    st.sidebar.write("")
    st.sidebar.write("")
    st.sidebar.write("")
    st.sidebar.write("Done by:")
    st.sidebar.write("Vishal Chouhan")
    st.sidebar.write("Roll No. 97")
    st.sidebar.write("PRN 1062201930")
    st.sidebar.write("TYBBA-CA")


if __name__ == '__main__':
    main()

