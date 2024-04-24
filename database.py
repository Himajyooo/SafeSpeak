import mysql.connector

def create_connection():
    #Used to connect Python with MySQL
    con = mysql.connector.connect(\
          host = "localhost",\
          user = "root",
          password = "")
    cur = con.cursor()
    strSQL = "show databases"
    cur.execute(strSQL)
    r = cur.fetchall()
    if ("safespeak",) in r:
        pass
    else:  #Till here
        strSQL = "create database safespeak;"
        cur.execute(strSQL)
    strSQL = "select database();"
    cur.execute(strSQL)
    r = cur.fetchall()
    if r in ("safespeak",):
        pass
    else:
        strSQL = "use safespeak;"
        cur.execute(strSQL)
    strSQL = "show tables;"
    cur.execute(strSQL)
    r = cur.fetchall()
    if ("login",) in r:
        pass
    else:
        strSQL = "create table login("\
                "userid int(5) primary key auto_increment ,username varchar(20) not null,"\
                "pass varchar(20) not null,email varchar(20) not null);"
        cur.execute(strSQL)
        strSQL="insert into login values(001,'user','password','user@email.com');"
        cur.execute(strSQL)
        con.commit()
    if ("toxic",) in r:
        pass
    else:
        strSQL = "create table toxic("\
                "toxic_id int auto_increment primary key, "\
                "userid  int(5),comment_desc text, "\
                "discussion_id int(5),username varchar(20) not null,"\
                "FOREIGN KEY (discussion_id) REFERENCES discussion(discussion_id),"\
                "FOREIGN KEY (userid) REFERENCES login(userid));"
        cur.execute(strSQL)
        con.commit()
    if ("discussion",) in r:
        pass
    else:
        strSQL = "create table discussion("\
                "discussion_id int(5) primary key auto_increment,d_name varchar(20) not null);"
        cur.execute(strSQL)
        strSQL="insert into discussion (d_name) values('discussion1'),('discussion2'),('discussion3');"
        cur.execute(strSQL)
        con.commit()    
    if ("comment",) in r:
        pass
    else:
        strSQL = "create table comment("\
                "comment_id int auto_increment primary key, "\
                "userid  int(5),comment_desc text, "\
                "discussion_id int(5),"\
                "FOREIGN KEY (discussion_id) REFERENCES discussion(discussion_id),"\
                "FOREIGN KEY (userid) REFERENCES login(userid));"
        cur.execute(strSQL)
        con.commit()
    return con, cur