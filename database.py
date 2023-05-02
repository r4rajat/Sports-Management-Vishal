import mysql.connector

mydb = mysql.connector.connect(host="localhost", port="6603", user="root", password="t*U6RW8ex@*&Cgz",
                               database="sports_mgmt_db")

if mydb:
    print("Database Connected Successfully !")
else:
    print("Database Connection Failed")

c = mydb.cursor()


def create_table_sports():
    c.execute("create table if not exists sports(Sid int primary key, Sname varchar(30), Category varchar(30))")


def add_data_sports(Sid, Sname, Category):
    c.execute("insert into sports(Sid, Sname, Category) values(%s,%s,%s)", (Sid, Sname, Category))


def view_all_sports():
    c.execute("select * from sports")
    data = c.fetchall()
    return data


def view_only_sport_name():
    c.execute("select Sname from sports")
    data = c.fetchall()
    return data


def view_only_sport_id():
    c.execute("select Sid from sports")
    data = c.fetchall()
    return data


def get_sport_id(Sid):
    c.execute("select * from sports where Sid='{}'".format(Sid))
    data = c.fetchall()
    return data


def get_sport_name(Sname):
    c.execute("select * from sports where Sname='{}'".format(Sname))
    data = c.fetchall()
    return data


def edit_sport(new_sport_id, new_sport_name, new_category, Sid, Sname, Category):
    c.execute("UPDATE sports SET Sid=%s, Sname=%s, Category=%s  WHERE Sid=%s and Sname=%s and Category=%s",
              (new_sport_id, new_sport_name, new_category, Sid, Sname, Category))
    mydb.commit()
    c.execute("SELECT Sid from sports")
    data = c.fetchall()
    return data


def delete_sport_data(sport_to_delete):
    c.execute('delete from sports where Sid = "{}"'.format(sport_to_delete))
    mydb.commit()


def sql_query(query):
    c.execute("{}".format(query))
    data = c.fetchall()
    return data


# -----------------------------------------------------------COACH--------------------------------------------------

def create_table_coach():
    c.execute(
        "create table if not exists coach(Cid int primary key, Cname varchar(30), Ph_no varchar(30), Address varchar(50), Specialized_in varchar(30))")


def add_data_coach(Cid, Cname, Ph_no, Address, Specialized_in):
    c.execute("insert into coach(Cid, Cname, Ph_no, Address, Specialized_in) values(%s,%s,%s,%s,%s)",
              (Cid, Cname, Ph_no, Address, Specialized_in))


def view_all_coaches():
    c.execute("select * from coach")
    data = c.fetchall()
    return data


def view_only_coach():
    c.execute("select Cname from coach")
    data = c.fetchall()
    return data


def view_only_coach_id():
    c.execute("select Cid from coach")
    data = c.fetchall()
    return data


def get_coach_id(Cid):
    c.execute("select * from coach where Cid='{}'".format(Cid))
    data = c.fetchall()
    return data


def get_coach_name(Cname):
    c.execute("select * from coach where Cname='{}'".format(Cname))
    data = c.fetchall()
    return data


def edit_coach(new_coach_id, new_coach_name, new_coach_phno, new_coach_address, new_coach_specialization, Cid, Cname,
               Ph_no, Address, Specialized_in):
    c.execute(
        "UPDATE coach SET Cid=%s, Cname=%s, Ph_no=%s, Address=%s, Specialized_in=%s WHERE Cid=%s and Cname=%s and Ph_no=%s and Address=%s and Specialized_in=%s",
        (new_coach_id, new_coach_name, new_coach_phno, new_coach_address, new_coach_specialization, Cid, Cname, Ph_no,
         Address, Specialized_in))
    mydb.commit()
    c.execute("SELECT Cid from coach")
    data = c.fetchall()
    return data


def delete_coach_data(selected_coach):
    c.execute('delete from coach where Cid = "{}"'.format(selected_coach))
    mydb.commit()


# -----------------------------------------------------------LEAGUE--------------------------------------------------


def create_table_league():
    c.execute("create table if not exists league(Lid int primary key, Lname varchar(30))")


def add_data_league(Lid, Lname):
    c.execute("insert into league(Lid, Lname) values(%s,%s)", (Lid, Lname))


def view_all_leagues():
    c.execute("select * from league")
    data = c.fetchall()
    return data


def view_only_league():
    c.execute("select Lname from league")
    data = c.fetchall()
    return data


def view_only_league_id():
    c.execute("select Lid from league")
    data = c.fetchall()
    return data


def get_league_id(Lid):
    c.execute("select * from league where Lid='{}'".format(Lid))
    data = c.fetchall()
    return data


def get_league(Lname):
    c.execute("select * from league where Lname='{}'".format(Lname))
    data = c.fetchall()
    return data


def edit_league(new_league_id, new_league_name, Lid, Lname):
    c.execute("UPDATE league SET Lid=%s, Lname=%s  WHERE Lid=%s and Lname=%s",
              (new_league_id, new_league_name, Lid, Lname))
    mydb.commit()
    c.execute("SELECT Lid from league")
    data = c.fetchall()
    return data


def delete_league_data(selected_league):
    c.execute('delete from league where Lid = "{}"'.format(selected_league))
    mydb.commit()


# -----------------------------------------------------------MATCHES--------------------------------------------------

def create_table_matches():
    c.execute(
        "create table if not exists matches(Mid int primary key, Team1 varchar(30), Team2 varchar(30), Refree varchar(30), Location varchar(30), Lid int, FOREIGN KEY (Lid) REFERENCES league(Lid) ON DELETE CASCADE)")


def add_data_matches(Mid, Team1, Team2, Refree, Location, Lid):
    c.execute("insert into matches(Mid, Team1, Team2, Refree, Location, Lid) values(%s,%s,%s,%s,%s,%s)",
              (Mid, Team1, Team2, Refree, Location, Lid))


def view_all_matches():
    c.execute("select * from matches")
    data = c.fetchall()
    return data


def view_only_match_id():
    c.execute("select Mid from matches")
    data = c.fetchall()
    return data


def get_match_id(Mid):
    c.execute("select * from matches where Mid='{}'".format(Mid))
    data = c.fetchall()
    return data


def edit_match(new_match_id, new_team1, new_team2, new_refree, new_location, new_lid, Mid, Team1, Team2, Refree,
               Location, Lid):
    c.execute(
        "UPDATE matches SET Mid=%s, Team1=%s, Team2=%s, Refree=%s, Location=%s, Lid=%s  WHERE Mid=%s and Team1=%s and Team2=%s and Refree=%s and Location=%s and Lid=%s",
        (new_match_id, new_team1, new_team2, new_refree, new_location, new_lid, Mid, Team1, Team2, Refree, Location,
         Lid))
    mydb.commit()
    c.execute("SELECT Mid from matches")
    data = c.fetchall()
    return data


def delete_match_data(selected_match):
    c.execute('delete from matches where Mid = "{}"'.format(selected_match))
    mydb.commit()


# -----------------------------------------------------------TEAMS--------------------------------------------------

def create_table_teams():
    c.execute(
        "create table if not exists teams(Tid int primary key, Tname varchar(30), Captain varchar(30), No_of_players int, Sid int, Cid int, Mid int, Lid int, FOREIGN KEY (Sid) REFERENCES sports(Sid) ON DELETE CASCADE, FOREIGN KEY (Cid) REFERENCES coach(Cid) ON DELETE CASCADE, FOREIGN KEY (Mid) REFERENCES matches(Mid) ON DELETE CASCADE, FOREIGN KEY (Lid) REFERENCES league(Lid) ON DELETE CASCADE)")


def add_data_teams(Tid, Tname, Captain, No_of_players, Sid, Cid, Mid, Lid):
    c.execute(
        "insert into teams(Tid, Tname, Captain, No_of_players, Sid, Cid, Mid, Lid) values(%s,%s,%s,%s,%s,%s,%s,%s)",
        (Tid, Tname, Captain, No_of_players, Sid, Cid, Mid, Lid))


def view_all_teams():
    c.execute("select * from teams")
    data = c.fetchall()
    return data


def view_only_team():
    c.execute("select Tname from teams")
    data = c.fetchall()
    return data


def view_only_team_id():
    c.execute("select Tid from teams")
    data = c.fetchall()
    return data


def get_team_id(Tid):
    c.execute("select * from teams where Tid='{}'".format(Tid))
    data = c.fetchall()
    return data


def get_team(Tname):
    c.execute("select * from teams where Tname='{}'".format(Tname))
    data = c.fetchall()
    return data


def edit_team(new_Tid, new_Tname, new_captain, new_no_of_players, new_sid, new_cid, new_mid, new_lid, Tid, Tname,
              Captain, No_of_players, Sid, Cid, Mid, Lid):
    c.execute(
        "UPDATE teams SET Tid=%s, Tname=%s, Captain=%s, No_of_players=%s, Sid=%s, Cid=%s, Mid=%s, Lid=%s WHERE Tid=%s and Tname=%s and Captain=%s and No_of_players=%s and Sid=%s and Cid=%s and Mid=%s and Lid=%s",
        (new_Tid, new_Tname, new_captain, new_no_of_players, new_sid, new_cid, new_mid, new_lid, Tid, Tname, Captain,
         No_of_players, Sid, Cid, Mid, Lid))
    mydb.commit()
    c.execute("SELECT Tid from teams")
    data = c.fetchall()
    return data


def delete_team_data(selected_team):
    c.execute('delete from teams where Tid = "{}"'.format(selected_team))
    mydb.commit()


# -----------------------------------------------------------PLAYERS-------------------------------------------------

def create_table_players():
    c.execute(
        "create table if not exists players(Pid int primary key, Fname varchar(30), Lname varchar(30), Dob date, Age int, Ph_no varchar(30), Address varchar(50), Cid int, Tid int, FOREIGN KEY (Cid) REFERENCES coach(Cid) ON DELETE CASCADE, FOREIGN KEY (Tid) REFERENCES teams(Tid)ON DELETE CASCADE)")


def add_data_players(Pid, Fname, Lname, Dob, Age, Ph_no, Address, Cid, Tid):
    c.execute(
        "insert into players(Pid, Fname, Lname, Dob, Age, Ph_no, Address, Cid, Tid) values(%s,%s,%s,%s,%s,%s,%s,%s,%s)",
        (Pid, Fname, Lname, Dob, Age, Ph_no, Address, Cid, Tid))


def view_all_players():
    c.execute("select * from players")
    data = c.fetchall()
    return data


def view_only_player():
    c.execute("select Sname from players")
    data = c.fetchall()
    return data


def view_only_player_id():
    c.execute("select Pid from players")
    data = c.fetchall()
    return data


def get_player_id(Pid):
    c.execute("select * from players where Pid='{}'".format(Pid))
    data = c.fetchall()
    return data


def get_player(Fname):
    c.execute("select * from players where Fname='{}'".format(Fname))
    data = c.fetchall()
    return data


def edit_player(new_Pid, new_Fname, new_Lname, new_Dob, new_Age, new_Ph_no, new_Address, new_cid, new_tid, Pid, Fname,
                Lname, Dob, Age, Ph_no, Address, Cid, Tid):
    c.execute(
        "UPDATE players SET Pid=%s, Fname=%s, Lname=%s, Dob=%s, Age=%s, Ph_no=%s, Address=%s, Cid=%s, Tid=%s WHERE Pid=%s and Fname=%s and Lname=%s and Dob=%s and Age=%s and Ph_no=%s and Address=%s and Cid=%s and Tid=%s",
        (new_Pid, new_Fname, new_Lname, new_Dob, new_Age, new_Ph_no, new_Address, new_cid, new_tid, Pid, Fname, Lname,
         Dob, Age, Ph_no, Address, Cid, Tid))
    mydb.commit()
    c.execute("SELECT Pid from players")
    data = c.fetchall()
    return data


def delete_player_data(selected_player):
    c.execute('delete from players where Pid = "{}"'.format(selected_player))
    mydb.commit()
