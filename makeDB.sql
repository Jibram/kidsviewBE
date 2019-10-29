/* Assuming you wrote "sqlite3 KVDB.db"... */
CREATE DATABASE KVDB;

CREATE TABLE patients(
    patientID   INTEGER PRIMARY KEY,
    patientName TEXT NOT NULL,
    parentName  TEXT NOT NULL,
    phoneNumber INTEGER NOT NULL,
    meData      TEXT,
    aeData      INTEGER
);

CREATE TABLE users(
    userID  TEXT NOT NULL,
    pword   TEXT NOT NULL,
    allowed INTEGER,
    PRIMARY KEY(userID, pword)
)