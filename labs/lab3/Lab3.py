import sqlite3

conn = sqlite3.connect('test.db')

print "Opened database successfully";

conn.execute('''CREATE TABLE Player
        (ID         INTEGER PRIMARY KEY NOT NULL,
        Name        NOT NULL,
        Team        CHAR(3),
        Position    CHAR(2),
        Age         INTEGER,
        GP          INTEGER,
        MPG         INTEGER,
        FTA         INTEGER,
        FTPerc      FLOAT(3),
        TwoPA       INTEGER,
        TwoPPerc    FLOAT(3),
        ThreePA     INTEGER,
        ThreePPerc  FLOAT(3),
        TSPerc      FLOAT(3),
        PPG         FLOAT(3),
        RPG         FLOAT(3),
        TRBPerc     FLOAT(3),
        APG         FLOAT(3),
        ASTPerc     FLOAT(3),
        SPG         FLOAT(3),
        BPG         FLOAT(3),
        VI          FLOAT(1));''')

print "Player Table created successfully";

conn.execute('''CREATE TABLE Team
        (TeamName       PRIMARY KEY NOT NULL,
        Conference      CHAR(4),
        Division        VARCHAR(10),
        GP              INTEGER,
        PPG             FLOAT(1),
        OPPG            FLOAT(1),
        PDIF            FLOAT(1),
        PACE            FLOAT(1),
        OEFF            FLOAT(1),
        DEFF            FLOAT(1),
        EDIF            FLOAT(1),
        SoS             FLOAT(2),
        SAR             FLOAT(2),
        CONS            FLOAT(1),
        A4F             FLOAT(3),
        Win             INTEGER,
        Loss            INTEGER,
        WinPerc         FLOAT(3),
        PWinPerc        FLOAT(3),
        EWinPerc        FLOAT(3),
        ACH             FLOAT(3));''')

print "Team table created successfully";

conn.close()
