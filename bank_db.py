import pickle
import sqlite3

class SqlBankDatabase():
    def __init__(self,filename):
        self.filename = filename
        self.database = {}
        self.read_database()
        


    def read_database(self):
        self.conn = sqlite3.connect(self.filename)
        self.cursor = self.conn.cursor()

    def write_database(self):
        self.conn.commit()


    def get_pin(self,acct_num):
        pass


    def get_name(self,acct_num):
        row = self.cursor.execute("SELECT fullname FROM BankDatabase WHERE acct = ?", (acct_num,))
        return self.cursor.fetchone()[0]


    def set_balance(self,acct_num,new_balance):
        self.cursor.execute("UPDATE BankDatabase SET balance = ? WHERE acct = ?", (new_balance,acct_num))
        self.write_database()

    def get_balance(self,acct_num):
        row = self.cursor.execute("SELECT balance FROM BankDatabase WHERE acct = ?",(acct_num,))
        return self.cursor.fetchone()[0]

    def validate_user(self,acct_num,pin):
        self.cursor.execute("SELECT acct,pin FROM BankDatabase WHERE acct = ? and pin = ?",(acct_num,pin))
        if self.cursor.fetchone() == None:
            return False
        else:
            return True
          


class PickleBankDatabase():
    def __init__(self,filename):
        self.filename = filename
        self.database = {}
        self.read_database()

    def read_database(self):
        infile = open(self.filename, 'rb')
        self.database = pickle.load(infile)
        infile.close()

    def write_database(self):
        outfile = open(self.filename, 'wb')
        pickle.dump(self.database,outfile)
        outfile.close()

    def get_pin(self,acct_num):
        return self.database[acct_num]['pin']

    def get_name(self,acct_num):
        return self.database[acct_num]['name']

    def set_balance(self,acct_num,new_balance):
        self.database[acct_num]['balance'] = new_balance
        self.write_database()

    def get_balance(self,acct_num):
        return self.database[acct_num]['balance'] 

    def validate_user(self,acct_num,pin):
        if acct_num in self.database and self.database[acct_num]['pin'] == pin:
            return True
        else:
            return False
