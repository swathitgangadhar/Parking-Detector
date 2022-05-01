#!/usr/bin/env python

import park
import mysql.connector
import configparser

# Establishing a connection between the ultrasonic sensor and the db management system
def connection():
    cfg = configparser.ConfigParser()
    cfg.read("/home/pi/Desktop/Pycode/parking_detector.ini")
    assert "MySQL" in cfg, "Missing credentials for MySQL"      #Check the necessary credintials needed
    connect = mysql.connector.connect(host=cfg["MySQL"]["host"],
                                      user=cfg["MySQL"]["username"],
                                      passwd=cfg["MySQL"]["password"], database=cfg["MySQL"]["db"])
    return connect

# To collect the data from the ultrasonic sensor and record it on the db table
def data_input(con):
    avail = park.availability

    cursor = con.cursor(buffered=True)
    query = "INSERT INTO parking_detector(date, time, availability) VALUES (CURRENT_DATE(),CURRENT_TIME(), %s)"
    cursor.execute(query, (int(avail)))
    con.commit()
    cursor.close()
    con.close()

if __name__ == "__main__":
    data_input(connection())