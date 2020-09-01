import os
import mysql.connector
from dotenv import load_dotenv


class DB(object):
    def __init__(self, db): # db = 'db-main' or 'db-sub'
        load_dotenv(os.path.dirname(os.path.realpath(__file__)) + '/../.env')
        self.load_var(db)
        self.connect()
        self.create_tables()
        self.close()

    def load_var(self, db):
        self.db_name = db
        if self.db_name == 'db_main':
            self.db_pswd = 'MYSQL_MAIN_PSWD'
            self.db_port = 'MYSQL_MAIN_PORT'
            self.db_ip = 'MYSQL_MAIN_IP'
        elif self.db_name == 'db_sub':
            self.db_pswd = 'MYSQL_SUB_PSWD'
            self.db_port = 'MYSQL_SUB_PORT'
            self.db_ip = 'MYSQL_SUB_IP'
        else:
            print('No DB matched, exit...')
            exit()

    def connect(self, address='localhost'):
        self.conn = mysql.connector.connect(host=address,
                                    user='root',
                                    port=os.getenv(self.db_port),
                                    password=os.getenv(self.db_pswd),
                                    use_pure=True)
        self.cursor = self.conn.cursor(buffered=True)

    def create_tables(self):
        if self.db_name == 'db_main':
            self.connect()
            self.cursor.execute("CREATE DATABASE IF NOT EXISTS " + self.db_name)
            self.cursor.execute("USE " + self.db_name)
            self.cursor.execute("CREATE TABLE IF NOT EXISTS location( \
                                    postcode VARCHAR(8), \
                                    name VARCHAR(64), \
                                    PRIMARY KEY (postcode) \
                                    )")
            self.cursor.execute("CREATE TABLE IF NOT EXISTS people( \
                                    person_id INT NOT NULL AUTO_INCREMENT UNIQUE, \
                                    name VARCHAR(64), \
                                    phone VARCHAR(16), \
                                    age SMALLINT, \
                                    address VARCHAR(256) NOT NULL, \
                                    location VARCHAR(8), \
                                    test_result ENUM('Positive', 'Negative', 'None') NOT NULL, \
                                    encryption_keys VARCHAR(512), \
                                    FOREIGN KEY (location) REFERENCES location(postcode), \
                                    PRIMARY KEY (person_id) \
                                    )")
            self.cursor.execute("CREATE TABLE IF NOT EXISTS contact( \
                                    idx INT NOT NULL AUTO_INCREMENT, \
                                    person_id1 INT NOT NULL, \
                                    person_id2 INT NOT NULL, \
                                    FOREIGN KEY (person_id1) REFERENCES people(person_id), \
                                    FOREIGN KEY (person_id2) REFERENCES people(person_id), \
                                    PRIMARY KEY (idx) \
                                    )")
            self.cursor.execute("CREATE TABLE IF NOT EXISTS stay_home_record( \
                                    idx INT NOT NULL AUTO_INCREMENT, \
                                    name VARCHAR(64), \
                                    phone VARCHAR(16), \
                                    start_time DATETIME, \
                                    end_time DATETIME, \
                                    address VARCHAR(256) NOT NULL, \
                                    location VARCHAR(8), \
                                    images VARCHAR(1024), \
                                    videos VARCHAR(1024), \
                                    documents VARCHAR(1024), \
                                    FOREIGN KEY (location) REFERENCES location(postcode), \
                                    PRIMARY KEY (idx) \
                                    )")
            self.cursor.execute("CREATE TABLE IF NOT EXISTS admin( \
                                    idx INT NOT NULL AUTO_INCREMENT, \
                                    name VARCHAR(64), \
                                    phone VARCHAR(16), \
                                    encryption_keys VARCHAR(2048), \
                                    PRIMARY KEY (idx) \
                                    )")
            self.cursor.execute("CREATE TABLE IF NOT EXISTS researcher( \
                                    idx INT NOT NULL AUTO_INCREMENT, \
                                    name VARCHAR(64), \
                                    phone VARCHAR(16), \
                                    encryption_keys VARCHAR(2048), \
                                    PRIMARY KEY (idx) \
                                    )")
        
        elif self.db_name == 'db_sub':
            self.connect()
            self.cursor.execute("CREATE DATABASE IF NOT EXISTS " + self.db_name)
            self.cursor.execute("USE " + self.db_name)
            # self.cursor.execute("CREATE TABLE IF NOT EXISTS location( \
            #                         postcode VARCHAR(8), \
            #                         name VARCHAR(64), \
            #                         PRIMARY KEY (postcode) \
            #                         )")
            # self.cursor.execute("CREATE TABLE IF NOT EXISTS people( \
            #                         person_id INT NOT NULL AUTO_INCREMENT UNIQUE, \
            #                         name VARCHAR(64), \
            #                         phone VARCHAR(16), \
            #                         age SMALLINT, \
            #                         address VARCHAR(256) NOT NULL, \
            #                         location VARCHAR(8), \
            #                         test_result ENUM('Positive', 'Negative', 'None') NOT NULL, \
            #                         encryption_keys VARCHAR(512), \
            #                         FOREIGN KEY (location) REFERENCES location(postcode), \
            #                         PRIMARY KEY (person_id) \
            #                         )")
            
        else:
            print('No DB matched, exit...')
            exit()

    def close(self):
        self.conn.commit()
        self.cursor.close()
        self.conn.close()

db = DB('db_main')
