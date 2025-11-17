import re
import random
import time
from datetime import datetime

import smtplib
from email.mime.text import MIMEText
from datetime import date
import socket
import subprocess
import sys

def check_internet_connection():
    try:
        socket.create_connection(('8.8.8.8', 53), timeout=5)
        return True
    except OSError:
        return False
num = 10
while(num == 10):
    if check_internet_connection():
        def install_mysql_connector():
            try:
                import mysql.connector
            except ImportError:
                print('mysql-connector-python is not installed. Installing now...')
                print()
                subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'mysql-connector-python'])
                print('mysql-connector-python installed successfully')
                print()
        install_mysql_connector()
        num = 15
    else:
        print('No internet connection. please connect to the internet and wait let your code run')
        print()
        time.sleep(10)

import mysql.connector


def connect_to_server(host1, user1, password1):
    mydb = mysql.connector.connect(
        host=host1,
        user=user1,
        password=password1

    )
    return mydb


def connect_to_database(host1, user1, password1, database1):
    mydb = mysql.connector.connect(
        host=host1,
        user=user1,
        password=password1,
        database=database1
    )
    return mydb


def execute_query(mydb, query):
    cursor = mydb.cursor()
    cursor.execute(query)
    mydb.commit()


def execute_query2(mydb, query, p):
    cursor = mydb.cursor()
    cursor.execute(query, p)
    mydb.commit()


def read_query(mydb, query):
    mycusor = mydb.cursor()
    mycusor.execute(query)
    result = mycusor.fetchall()
    return result


def read_query2(mydb, query):
    mycusor = mydb.cursor()
    mycusor.execute(query)
    result = mycusor.fetchone()
    return result





def create_database(cursor):
    cursor.execute(f'CREATE DATABASE IF NOT EXISTS bankdatabase  ')


def create_table(cursor):
    cursor.execute(f'USE bankdatabase')
    user_details = """CREATE TABLE IF NOT EXISTS user_details(
       account_id INT NOT NULL AUTO_INCREMENT,
       firstname VARCHAR (100) NOT NULL,
       surname VARCHAR (100) NOT NULL,
       username VARCHAR (100) NULL,
       password VARCHAR (100) NULL,
       pin INT NULL,
       phonenumber VARCHAR (20)NULL ,
       bvn VARCHAR(20) NULL,
       balance INT NULL,
       accountnumber VARCHAR(20) NULL,
       email TEXT NOT NULL,
       PRIMARY KEY (account_id));

       """
    cursor.execute(user_details)


connection_database = connect_to_server('localhost', 'root', '')
cursor = connection_database.cursor()
create_database(cursor)
connection = connect_to_database('localhost', 'root', '', 'bankdatabase')
cursor_table = connection.cursor()

create_table(cursor_table)


class Banking_Application:
    def __init__(self, username):
        self.username = username
        self.d = True
        print('please enter your gmail address and gmail app password below for the automatic gmail sender')
        self.email1 = input("Enter your Gmail address to receive transaction receipts: ")
        self.password1 = input("Enter your Gmail App Password: ")
    def input_int(self,prompt):
        while True:
            try:
                value = int(input(prompt))
                print()
                return value
            except ValueError:
                print('invalid input! please you can only enter an integer.')
                print()
    def create_account(self):
        self.first_name = input('please enter your first name: ')
        print()
        self.surname = input('please enter your surname: ')
        print()
        self.balance = 0
        print()

        username_check = """SELECT username FROM user_details; """
        connection = connect_to_database('localhost', 'root', '', 'bankdatabase')
        result = read_query(connection, username_check)
        self.d = True
        while (self.d == True):
            self.username = input('please enter a username: ')
            print()
            if (self.username,) in result:
                print('this username already exist please use another username')
                print()
            else:

                self.d = False
        print('please your password must contain letters and words')
        print()
        self.d = True
        while (self.d == True):
            self.password = input('please enter your password here: ')
            print()
            pattern = re.compile(r'^(?=.*[A-Za-z])(?=.*\d).+$')
            if pattern.match(self.password):
                pass
                self.d = False
            else:
                print('please your password must contain letter and numbers')
                print()
        self.d = True
        while (self.d == True):
            self.pin = input('please enter your 4 digit pin you will like to use: ')
            print()

            if not self.pin.isdigit():
                print('pin must contain only digits. please enter a valid number.')
                print()
            elif len(str(self.pin)) != 4:
                print('please your pin can only be 4 digits')
                print()
            else:
                loop_no = 4
                while (loop_no == 4):
                    self.pin2 = input('please reenter your pin to confirm ')
                    print()
                    if not self.pin2.isdigit():
                        print('pin must contain only digits. please enter a valid number.')
                        print()

                    elif (self.pin == self.pin2):
                        print('pin match')
                        print()
                        self.d = False
                        loop_no = 6

                    else:
                        print(
                            'your confirm pin is not correct pins do not match and your pin might not be up to 4 digits')
                        print()
        self.d = True
        while (self.d == True):
            self.phone_number = input('pls enter your phone number: ')
            print()

            if not self.phone_number.isdigit():
                print('phone number must contain only digits. please enter a valid number.')
                print()
            elif (len(str(self.phone_number))) != 11:
                print(self.phone_number)
                print()
                print('phone number can only be 11 digits')
                print()
            else:
                pass
                self.d = False
        self.d = True
        while (self.d == True):
            print('please do you have a bvn 1. yes 2. no ')
            print()
            user_choice = self.input_int('please enter your choice hear: ')
            if (user_choice == 1):
                ff = 5
                while (ff == 5):
                    self.bvn = input('please input your bvn hear: ')
                    print()

                    if not self.bvn.isdigit():
                        print('bvn must contain only digits. please enter a valid number.')
                        print()
                    elif (len(str(self.bvn))) != 10:
                        print('bvn can only be 10 digits')
                        print()

                        self.d = True
                    else:
                        bvn_to_store = self.bvn
                        pass
                        self.d = False
                        ff = 7
            elif (user_choice == 2):
                self.bvn_number = ''.join(str(random.randint(1, 9)) for i in range(10))
                bvn_to_store = self.bvn_number
                print()
                print(f'your new bvn number is {self.bvn_number} save it')
                print()
                self.d = False
            else:
                print('incorrect option selected \n try again')
                print()
        self.d = True
        useremail_check = """SELECT email FROM user_details; """
        connection = connect_to_database('localhost', 'root', '', 'bankdatabase')
        result = read_query(connection, useremail_check)
        while (self.d == True):
            print('please enter your gmail correctly and plus check before pressing enter')
            print()
            self.email = input('please enter your email: ')
            print()
            if ((self.email,) not in result):
                pg = True
                while (pg == True):
                    if ("@" in self.email and " " not in self.email and "." in self.email[
                                                                               self.email.index("@") + 1:] and len(
                            self.email[self.email.index("@") + 1:].split(".")[0]) > 0):

                        # '@' in self.email and self.email.count('@') == 1
                        pg = False
                        self.d = False

                    else:
                        print(
                            'invalid email! please enter a valid email with no spaces and a domain (e.g., user@example.com).')
                        print()
                        pg = False
            else:
                print('email already rested with an account use another')
                print()

        self.account_number = ''.join(str(random.randint(1, 9)) for i in range(10))
        print()
        
        def account_creation_confirmation():
            current_datetime = datetime.now()
            current_date = current_datetime.strftime('%Y-%m-%d')
            current_time = current_datetime.strftime('%H:%M')

            message = f"""
                  Dear {self.first_name} {self.surname},

                  Congratulations! Your account has been successfully created with BANKING BUDDY.

                  Account Details:
                  ------------------------------------------
                  Account Name: {self.first_name} {self.surname}
                  Account Number: {self.account_number}
                  Date ACCOUNT Created: {current_date},{current_time}
                  ------------------------------------------

                  Thank you for choosing BANKING BUDDY.
                  Best regards,
                  The BANKING BUDDY Team

                  This is an automated message. Please do not reply.
                  ----------------------------------------------
                  """
            return message  # Return the formatted string

        message = account_creation_confirmation()
        msg = MIMEText(message)
        msg['Subject'] = 'ACCOUNT CREATED SUCCESSFULLY'
        msg['From'] = self.email1
        msg['To'] = self.email

        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            # server.starttls()
            
            server.login(self.email1, self.password1)

            server.send_message(msg)
        # Print the result
        print(
            f'your account has been successfully registered \n this your new account number please save it thanks for using david bank {self.account_number}')
        print()
        print('the details has been sent to your email you can check it out')
        print()

        first_insertion = (
            f"""INSERT INTO user_details(firstname,surname,balance,username,password,pin,phonenumber,accountnumber,bvn,email) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);""")

        p = (self.first_name, self.surname, self.balance, self.username, self.password, self.pin, self.phone_number,
             self.account_number, bvn_to_store, self.email)
        execute_query2(connection, first_insertion, p)



    def add_money(self):
        print('good day ')
        print()

        amount = self.input_int('please enter the amount you want to add: ')
        print()

        update_user_balance = f"""  UPDATE user_details SET balance = balance + {amount}  WHERE username = '{self.username}' ; """
        execute_query(connection, update_user_balance)
        balance_details = f"""  SELECT balance FROM user_details WHERE username = '{self.username}' ; """
        display_amount = read_query2(connection, balance_details)
        for i in display_amount:
            pass
        first_name_details = f"""  SELECT firstname FROM user_details WHERE username = '{self.username}' ; """
        display_first_name = read_query2(connection, first_name_details)
        for y in display_first_name:
            pass
        surn_name_details = f"""  SELECT surname FROM user_details WHERE username = '{self.username}' ; """
        display_surn_name = read_query2(connection, surn_name_details)
        for x in display_surn_name:
            pass

        def account_add_money_verified():
            current_datetime = datetime.now()
            current_date = current_datetime.strftime('%Y-%m-%d')
            current_time = current_datetime.strftime('%H:%M')


            message = f"""
                Dear {y} {x},

                You have successfully added money to your account.

                Details:
                ------------------------------------------
                Amount Added: #{amount}
                Balance: #{i}
                Date MONEY WAS ADDED TO ACCOUNT: {current_date},{current_time}
                ------------------------------------------

                Thank you for choosing BANKING BUDDY.
                Best regards,
                The BANKING BUDDY Team

                This is an automated message. Please do not reply.
                ----------------------------------------------
                """
            return message

        email_details = f"""  SELECT email FROM user_details WHERE username = '{self.username}' ; """
        display_email = read_query2(connection, email_details)
        for n in display_email:
            pass


        message = account_add_money_verified()
        msg = MIMEText(message)
        msg['Subject'] = 'Money Added Details'
        msg['From'] = self.email1
        msg['To'] = n

        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            # server.starttls()
            server.login(self.email1, self.password1)
            server.send_message(msg)

        print(f'the sum of {amount} has b een added to your account your balance is {i}')
        print()
        print('the details of money added to your account has been sent to your email you can check it out')
        print()


    def transfer_money(self):
        print('good day ')
        print()
        num3 = 10
        while (num3 == 10):

            account_details = """SELECT  accountnumber FROM user_details;"""
            account_run = read_query(connection, account_details)
            print('please you can only transfer money to accounts that registered to banking buddy')
            print()
            acccount_no = self.input_int('please enter the account number hear you will like to transfer money to: ')
            print()
            account_numbers = [str(acc[0]) for acc in account_run]

            if (str(acccount_no, )) in account_numbers:
                name_details = f"""SELECT firstname FROM user_details WHERE accountnumber = '{acccount_no}';"""
                result_name = read_query2(connection, name_details)
                for i in result_name:
                    print(f'owner of account firstname: {i}')
                    print()
                surname_details = f"""SELECT surname FROM user_details WHERE accountnumber = '{acccount_no}';"""
                result_surname = read_query2(connection, surname_details)
                for q in result_surname:
                    print(f'owner of account surname: {q}')
                    print()
                print(
                    '1. select 1 if this  the person you want to transfer money to \n 2. select 2 if this not the person you want to transfer money to')
                print()
                user_choice = self.input_int('please enter your choice hear: ')
                print()
                if (user_choice == 1):
                    num = 10
                    while (num == 10):
                        balance_details = f"""SELECT balance FROM user_details WHERE username = '{self.username}';"""
                        result7 = read_query2(connection, balance_details)
                        for p in result7:
                            pass

                        print(f'your balance is: {p} ')
                        print()
                        # print('do you wish to add money \n 1. yes \n 2. no')

                        nu = 10
                        while (nu == 10):
                            print('do you wish to add money \n 1. yes \n 2. no')
                            print()
                            userchoice3 = self.input_int('your choice hear: ')
                            print()
                            if (userchoice3 == 1):

                                self.add_money()
                                num3 = 15
                                num = 14
                                num2 = 15
                                p2 = 18

                            elif (userchoice3 == 2):
                                amount = self.input_int('please enter the amount you will like to transfer: ')
                                print()
                                num4 = 10
                                balance_details2 = f"""SELECT balance FROM user_details WHERE username = '{self.username}';"""
                                result72 = read_query2(connection, balance_details2)
                                for m in result72:
                                    pass

                                #print(f'your balance is: {m} ')
                                #print()
                                if amount < m:
                                    while (num4 == 10):
                                        pin = self.input_int('please enter your 4 digit pin  to make the transaction: ')
                                        print()
                                        pin_details = f"""SELECT pin FROM user_details WHERE username = '{self.username}';"""
                                        result9 = read_query2(connection, pin_details)
                                        if (pin,) == result9:
                                            print('pin correct')
                                            add_money_to_user_account = f"""UPDATE user_details SET balance = balance + {amount} WHERE accountnumber = '{acccount_no}';"""
                                            result5 = execute_query(connection, add_money_to_user_account)
                                            minus_money_to_user_account = f"""UPDATE user_details SET balance = balance - {amount} WHERE username = '{self.username}';"""
                                            result6 = execute_query(connection, minus_money_to_user_account)
                                            balance_details2 = f"""SELECT balance FROM user_details WHERE username = '{self.username}';"""
                                            result8 = read_query2(connection, balance_details2)
                                            for y in result8:
                                                pass
                                            first_name_details = f"""  SELECT firstname FROM user_details WHERE username = '{self.username}' ; """
                                            display_first_name = read_query2(connection, first_name_details)
                                            for b in display_first_name:
                                                pass
                                            surn_name_details = f"""  SELECT surname FROM user_details WHERE username = '{self.username}' ; """
                                            display_surn_name = read_query2(connection, surn_name_details)
                                            for x in display_surn_name:
                                                pass

                                            def account_transfer_verified():
                                                current_datetime = datetime.now()
                                                current_date = current_datetime.strftime('%Y-%m-%d')
                                                current_time = current_datetime.strftime('%H:%M')
                                                message = f"""
                                                            Dear {b} {x},

                                                            Your transfer of #{amount} was successful.

                                                            Details of the transaction are as follows:
                                                            ------------------------------------------
                                                            Amount Transferred : #{amount}
                                                            Account Number: {acccount_no}
                                                            Balance: {y}
                                                            Date OF TRANSACTION: {current_date},{current_time}
                                                            ------------------------------------------

                                                            Thank you for choosing BANKING BUDDY.
                                                            Best regards,
                                                            The BANKING BUDDY Team

                                                            This is an automated message. Please do not reply.
                                                            ----------------------------------------------
                                                            """
                                                return message

                                            email_details = f"""  SELECT email FROM user_details WHERE username = '{self.username}' ; """
                                            display_email = read_query2(connection, email_details)
                                            for n in display_email:
                                                pass
                                            message = account_transfer_verified()
                                            msg = MIMEText(message)
                                            msg['Subject'] = 'Transaction Details'
                                            msg['From'] = self.email1
                                            msg['To'] = n

                                            with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
                                                # server.starttls()
                                                server.login(self.email1,
                                                             self.password1)
                                                server.send_message(msg)
                                            print(
                                                f' you have successfully transfered the money to  this account {acccount_no} your balance is: {y} ')
                                            print()
                                            print('the details of your transaction has  been sent to your email you can check it out')
                                            print()

                                            num3 = 15
                                            num = 14
                                            num4 = 17
                                            num2 = 15
                                            p2 = 18
                                            nu = 13
                                            break

                                        else:

                                            print('wrong pin try again')
                                            print()
                                else:
                                    print('insufficent funds ')
                                    print()
                                    print('do you wish to try again \n 1. yes \n 2. no')
                                    print()
                                    user_choice2 = self.input_int('please enter your choice hear: ')
                                    print()
                                    if (user_choice2 == 1):
                                        continue
                                    elif (user_choice2 == 2):
                                        print('ok thanks for using our bank')
                                        print()
                                        num3 = 15
                                        num = 14
                                        num4 = 14
                                        num2 = 15
                                        p2 = 14
                                        break
                            else:
                                print('wrong input')
                                print()






                elif (user_choice == 2):

                    num3 = 10
                    print('try entering the account number again')
                    print()
                else:
                    print('you picked a wrong choice enter the account number again')
                    print()
                    num3 = 10


            else:
                print('please this account number  is not registered to our bank')
                print()

    def buy_airtime_or_buy_databundle(self):
        x = 0
        current_function = None
        current_network = None
        print('good day ')
        print()

        def buy_airtime():
            # nonlocal person_username
            phone_no = self.input_int('pls enter the phone number here: ')
            print()

            balance_details = f"""SELECT balance FROM user_details WHERE username = '{self.username}';"""
            result = read_query2(connection, balance_details)
            for m in result:
                pass

            print(f'your balance is: {m} ')
            print()
            bool1 = True
            while (bool1 == True):
                amount = self.input_int('please enter the amount here: ')
                print()
                if amount < m:
                    num = 10
                    while (num == 10):
                        pin_input = self.input_int('please enter your pin hear: ')
                        print()
                        fetch_pin = f"""SELECT pin FROM user_details WHERE username = '{self.username}';"""
                        result_obtained = read_query2(connection, fetch_pin)
                        if ((pin_input,) == result_obtained):
                            minus_money_from_user_account = f"""UPDATE user_details SET balance = balance - {amount} WHERE username = '{self.username}';"""
                            result2 = execute_query(connection, minus_money_from_user_account)
                            balance_details = f"""SELECT balance FROM user_details WHERE username = '{self.username}';"""
                            result3 = read_query2(connection, balance_details)
                            for y in result3:
                                pass
                            first_name_details = f"""  SELECT firstname FROM user_details WHERE username = '{self.username}' ; """
                            display_first_name = read_query2(connection, first_name_details)
                            for b in display_first_name:
                                pass
                            surn_name_details = f"""  SELECT surname FROM user_details WHERE username = '{self.username}' ; """
                            display_surn_name = read_query2(connection, surn_name_details)
                            for x in display_surn_name:
                                pass

                            def account_airtime_verified():
                                current_datetime = datetime.now()
                                current_date = current_datetime.strftime('%Y-%m-%d')
                                current_time = current_datetime.strftime('%H:%M')
                                return f"""
                                        Dear {b} {x},

                                        Thank you for using our service.

                                        We are pleased to inform you that your recent purchase of airtime was successful. Below are the details of your transaction:

                                        Transaction Details:
                                        ------------------------------------------
                                        Type of Purchase: AIRTIME
                                        Amount: #{amount}
                                        Phone Number: {phone_no}
                                        Balance: {y}
                                        Date of purchase: {current_date},{current_time}
                                        ------------------------------------------

                                        Thank you for choosing BANKING BUDDY.
                                        Best regards,
                                        The BANKING BUDDY Team

                                        This is an automated message. Please do not reply.
                                        ----------------------------------------------
                                        """

                            email_details = f"""  SELECT email FROM user_details WHERE username = '{self.username}' ; """
                            display_email = read_query2(connection, email_details)
                            for n in display_email:
                                pass
                            message = account_airtime_verified()
                            msg = MIMEText(message)
                            msg['Subject'] = 'Airtime purchase  Details'
                            msg['From'] = self.email1
                            msg['To'] = n

                            with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
                                # server.starttls()
                                server.login(self.email1,
                                             self.password1)
                                server.send_message(msg)
                            print(
                                f'you have successfully purchased airtime for this phone number {phone_no} from  your account your balance is {y} \n thanks for using our services')
                            print()
                            print('the details of your purchase of your airtime has  been sent to your email you can check it out')
                            print()
                            bool1 = False
                            num = 15
                            break
                        else:
                            print('incorect pin')
                            print()



                else:
                    print('insufficent funds')
                    print()
                    print('1. select 1 if you wish to try again\n2. select 2 you dont wish to buy airtime again')
                    print()
                    user_choice = self.input_int('please enter your choice hear: ')
                    print()
                    bool2 = True
                    while (bool2 == True):
                        if (user_choice == 1):
                            pass
                            bool2 = False
                        elif (user_choice == 2):
                            print('thanks for using this bank ')
                            print()
                            bool2 = False
                            bool1 = False
                            break

        def AUTO_or_one_off():
            nonlocal x
            #  nonlocal person_username
            nonlocal current_function
            nonlocal phone_number
            nonlocal current_network
            print('1. AUTO-RENEW \n 2.  ONE-OFF \n 3. back')
            print()
            bool1 = True
            while (bool1 == True):
                user_choice = self.input_int('please enter your choice hear: ')
                print()
                if (user_choice == 1 or user_choice == 2):
                    num = 10
                    while (num == 10):
                        pin_input = self.input_int('please enter your pin hear: ')
                        print()
                        fetch_pin = f"""SELECT pin FROM user_details WHERE username = '{self.username}';"""
                        result_obtained = read_query2(connection, fetch_pin)
                        if ((pin_input,) == result_obtained):
                            minus_money_from_user_account = f"""UPDATE user_details SET balance = balance - {x} WHERE username = '{self.username}';"""
                            result2 = execute_query(connection, minus_money_from_user_account)
                            first_name_details = f"""  SELECT firstname FROM user_details WHERE username = '{self.username}' ; """
                            display_first_name = read_query2(connection, first_name_details)
                            for b in display_first_name:
                                pass
                            surn_name_details = f"""  SELECT surname FROM user_details WHERE username = '{self.username}' ; """
                            display_surn_name = read_query2(connection, surn_name_details)
                            for a in display_surn_name:
                                pass

                            def account_data_verified():
                                current_datetime = datetime.now()
                                current_date = current_datetime.strftime('%Y-%m-%d')
                                current_time = current_datetime.strftime('%H:%M')
                                return f"""
                                        Dear {b} {a},

                                        Thank you for using our service.

                                        We are pleased to inform you that your recent purchase of a data bundle was successful. Below are the details of your transaction:

                                        Transaction Details:
                                        ------------------------------------------
                                        Type of Purchase: Data Bundle
                                        Amount: #{x}
                                        Phone Number: {phone_number}
                                        Date of purchase: {current_date},{current_time}
                                        ------------------------------------------

                                        Thank you for choosing BANKING BUDDY.
                                        Best regards,
                                        The BANKING BUDDY Team

                                        This is an automated message. Please do not reply.
                                        ----------------------------------------------
                                        """

                            email_details = f"""  SELECT email FROM user_details WHERE username = '{self.username}' ; """
                            display_email = read_query2(connection, email_details)
                            for n in display_email:
                                pass
                            message = account_data_verified()
                            msg = MIMEText(message)
                            msg['Subject'] = 'data bundle purchase Details'
                            msg['From'] = self.email1
                            msg['To'] = n

                            with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:

                                server.login(self.email1, self.password1)
                                server.send_message(msg)
                            print(
                                f'you have successfully purchased an airtime of {x} for this number {phone_number} \n thanks for using our service')
                            print()
                            print('the details of your purchase of your airtime has  been sent to your email you can check it out')
                            print()

                            bool1 = False
                            num = 15
                            break
                        else:
                            print('incorrect pin entered')
                            print()
                elif (user_choice == 3):
                    if (current_function == 'social_plan'):
                        social_plan()
                        bool1 = False
                    elif (current_function == 'mtn_network'):
                        mtn_network()
                        bool1 = False
                    elif (current_function == 'glo_network'):
                        glo_network()
                        bool1 = False
                    elif (current_function == 'airtel_network'):
                        airtel_network()
                        bool1 = False



                else:
                    print('wrong input')
                    print()

        def social_plan():
            nonlocal x
            # nonlocal person_username
            nonlocal current_function
            nonlocal current_network
            current_function = 'social_plan'
            balance_details = f"""SELECT balance FROM user_details WHERE username = '{self.username}';"""
            result = read_query2(connection, balance_details)
            for m in result:
                pass

            bool1 = True
            while (bool1 == True):
                print(
                    """1. #25 FOR 25MB(WHATSAPP ONLY, 1 DAY) \n 2. #25 FOR 25MB(FACEBOOK ONLY,1 DAY) \n 3. #25 FOR 25MB(AYOBA ONLY, 1 DAY) \n 4. #50 FOR 200MB (TIKTOK ONLY, 1 DAY) \n 5. #50 FOR 50MB (WHATSAPP ONLY, 7 DAYS) \n 6. #50 FOR 50MB (AYOBA ONLY, 1 DAY) \n 7. #50 FOR 150MB (ALL SOCIAL MEDIAS, 1 DAY) \n 8. #50 FOR 200MB (TIKTOK ONLY, 1 DAY) \n 99. next \n 0. back """)
                print()
                user_choice = self.input_int('please enter your choice hear: ')
                print()
                if (user_choice == 1 or user_choice == 2 or user_choice == 3):
                    x = 25
                    if x < m:
                        AUTO_or_one_off()
                        bool1 = False
                        break
                    else:
                        print('insuffficent funds')
                        print()
                elif (user_choice == 4 or user_choice == 5 or user_choice == 6 or user_choice == 7 or user_choice == 8):
                    x = 50
                    if x < m:
                        AUTO_or_one_off()
                        bool1 = False
                        break
                    else:
                        print('insufficent funds')
                        print()
                elif (user_choice == 99):
                    bool2 = True
                    while (bool2 == True):
                        print(
                            """9. #100 FOR 350MB (ALL SOCIAL MEDIAS, 7 DAYS) \n 10. #150 FOR 150MB (WHATSAPP ONLY, 30 DAYS) \n 11. #150 FOR 150MB (FACEBOOK ONLY, 30 DAYS) \n 12. #150 FOR 150MB (AYOBA ONLY, 30 DAYS) \n 13. #250 FOR 1GB (ALL SOCIAL MEDIAS, 30 DAYS) \n 14. #350 FOR 2GB (TIKTOK ONLY, 7 DAYS)  \n 0. back""")
                        print()
                        user_choice2 = self.input_int('please enter your choice hear: ')
                        print()
                        if (user_choice2 == 9):
                            x = 100
                            if x < m:
                                AUTO_or_one_off()
                                bool2 = False
                                bool1 = False

                                break
                            else:
                                print('insufficent funds')
                                print()
                        elif (user_choice2 == 10 or user_choice2 == 11 or user_choice2 == 12):
                            x = 150
                            if x < m:
                                AUTO_or_one_off()
                                bool2 = False
                                bool1 = False

                                break
                            else:
                                print('insufficent funds')
                                print()
                        elif (user_choice2 == 13):
                            x = 250
                            if x < m:
                                AUTO_or_one_off()
                                bool2 = False
                                bool1 = False
                                break
                            else:
                                print('insufficent funds')
                                print()
                        elif (user_choice2 == 14):
                            x = 350
                            if x < m:
                                AUTO_or_one_off()
                                bool2 = False
                                bool1 = False
                                break
                            else:
                                print('insufficent funds')
                                print()
                        elif (user_choice2 == 0):
                            bool2 = False

                            bool1 = True
                        else:
                            print('wrong input')
                            print()
                elif (user_choice == 0):
                    if (current_network == 'mtn_network'):
                        mtn_network()
                        bool1 = False
                        break
                    elif (current_network == 'glo_network'):
                        glo_network()
                        bool1 = False
                        break
                    elif (current_network == 'airtel_network'):
                        airtel_network()
                        bool1 = False
                        break
                else:
                    print('wrong input entered')

                    print()

        def mtn_network():
            nonlocal x
            # nonlocal person_username
            nonlocal current_function
            nonlocal current_network
            current_function = 'mtn_network'
            current_network = 'mtn_network'
            balance_details = f"""SELECT balance FROM user_details WHERE username = '{self.username}';"""
            result = read_query2(connection, balance_details)
            for m in result:
                pass

            print(f'your balance is: {m} ')
            print()
            bool1 = True
            while (bool1 == True):
                print(
                    """1. daily plan \n 2. weekly plan \n 3. monthly plan \n 4. 2-3 month plan \n 5. social media plan """)
                print()
                user_choice1 = self.input_int('please enter your choice hear: ')
                print()

                if (user_choice1 == 1):
                    bool2 = True
                    while (bool2 == True):
                        print(
                            """1. #50 FOR 40MB (1 DAY) \n 2. #100 FOR 100MB (1 DAY) \n 3. #200 FOR 250MB (3 DAYS) \n 4. #350 FOR 1GB (1 DAY) \n 5. #800 FOR 3GB (2 DAYS) \n 6. #600 FOR 2.5GB (2 DAYS) \n 7. #400 FOR 1.5GB (1 DAYS) \n 0. back""")
                        print()
                        user_choice2 = self.input_int('please enter your choice hear: ')
                        print()
                        if (user_choice2 == 1):
                            x = 50
                            if x < m:
                                AUTO_or_one_off()
                                bool2 = False
                                bool1 = False
                                break
                            else:
                                print('insufficent funds')
                                print()
                        elif (user_choice2 == 2):
                            x = 100
                            if x < m:
                                AUTO_or_one_off()
                                bool2 = False
                                bool1 = False
                                break
                            else:
                                print('insufficent funds')
                                print()
                        elif (user_choice2 == 3):
                            x = 200
                            if x < m:

                                AUTO_or_one_off()
                                bool2 = False
                                bool1 = False
                                break
                            else:
                                print('insufficent funds')
                                print()

                        elif (user_choice2 == 4):
                            x = 350
                            if x < m:
                                AUTO_or_one_off()
                                bool2 = False
                                bool1 = False
                                break
                            else:
                                print('insufficent funds')
                                print()
                        elif (user_choice2 == 5):
                            x = 800
                            if x < m:
                                AUTO_or_one_off()
                                bool2 = False
                                bool1 = False
                                break
                            else:
                                print('insufficent funds')
                                print()
                        elif (user_choice2 == 6):
                            x = 600
                            if x < m:
                                AUTO_or_one_off()
                                bool2 = False
                                bool1 = False
                                break
                            else:
                                print('insufficent funds')
                                print()
                        elif (user_choice2 == 7):
                            x = 400
                            if x < m:
                                AUTO_or_one_off()
                                bool2 = False
                                bool1 = False
                                break
                            else:
                                print('insufficent funds')
                                print()
                        elif (user_choice2 == 0):
                            bool2 = False
                            bool1 = True
                        else:
                            print('wrong input')
                            print()


                elif (user_choice1 == 2):
                    bool3 = True
                    while (bool3 == True):
                        print(
                            """1. #350 FOR 350MB (7 DAYS) \n 2. #500 FOR 600MB (7 DAYS) \n 3. #500 FOR 750MB + 500 (14 DAYS) \n 4. #600 FOR 1GB (7 DAYS) \n 5. #2,000 FOR 7GB (7 DAYS) \n 6. #1,000 FOR 1.5GB (7 DAYS) \n 7. #1,500 FOR 5GB (7 DAYS) \n 0. back""")
                        print()
                        user_choice3 = self.input_int('please enter your choice hear: ')
                        print()
                        if (user_choice3 == 1):
                            x = 350
                            if x < m:
                                AUTO_or_one_off()
                                bool3 = False
                                bool1 = False
                                break
                            else:
                                print('insufficent funds')
                                print()
                        elif (user_choice3 == 2):
                            x = 500
                            if x < m:
                                AUTO_or_one_off()
                                bool3 = False
                                bool1 = False
                                break
                            else:
                                print('insufficent funds')
                                print()
                        elif (user_choice3 == 3):
                            x = 500
                            if x < m:
                                AUTO_or_one_off()
                                bool3 = False
                                bool1 = False
                                break
                            else:
                                print('insufficent funds')
                                print()

                        elif (user_choice3 == 4):
                            x = 600
                            if x < m:
                                AUTO_or_one_off()
                                bool3 = False
                                bool1 = False
                                break
                            else:
                                print('insufficent funds')
                                print()
                        elif (user_choice3 == 5):
                            x = 2000
                            if x < m:
                                AUTO_or_one_off()
                                bool3 = False
                                bool1 = False
                                break
                            else:
                                print('insufficent funds')
                                print()
                        elif (user_choice3 == 6):
                            x = 1000
                            if x < m:
                                AUTO_or_one_off()
                                bool3 = False
                                bool1 = False
                                break
                            else:
                                print('insufficent funds')
                                print()
                        elif (user_choice3 == 7):
                            x = 1500
                            if x < m:

                                AUTO_or_one_off()
                                bool3 = False
                                bool1 = False
                                break
                            else:
                                print('insufficent funds')
                                print()
                        elif (user_choice3 == 0):
                            bool3 = False
                            bool1 = True
                        else:
                            print('wrong input')
                            print()

                elif (user_choice1 == 3):
                    bool4 = True
                    while (bool4 == True):
                        print(
                            """1. #1000 FOR 1.2GB( 30 DAYS) \n 2. #1200 FOR 1.5GB(30 DAYS) \n 3. #`1600 FOR 3GB(30 DAYS) \n 4. #2000 FOR 4GB (30 DAYS) \n 5. #1500 FOR 5GB (30 DAYS) \n 6. #3000 FOR 8GB (30 DAYS) \n 7. #3500 FOR 150MB (30 DAYS) \n 8. #4000 FOR 12GB (30 DAYS) \n 99. next \n 0. back """)
                        print()
                        user_choice4 = self.input_int('please enter your choice hear: ')
                        print()
                        if (user_choice4 == 1):
                            x = 1000
                            if x < m:

                                AUTO_or_one_off()
                                bool4 = False
                                bool1 = False

                                break
                            else:
                                print('insuffficent funds')
                                print()
                        elif (user_choice4 == 2):
                            x = 1200
                            if x < m:

                                AUTO_or_one_off()
                                bool4 = False
                                bool1 = False
                                break
                            else:
                                print('insufficent funds')
                                print()
                        elif (user_choice4 == 3):
                            x = 1600
                            if x < m:

                                AUTO_or_one_off()
                                bool4 = False
                                bool1 = False
                                break
                            else:
                                print('insufficent funds')
                                print()
                        elif (user_choice4 == 4):
                            x = 2000
                            if x < m:

                                AUTO_or_one_off()
                                bool4 = False
                                bool1 = False
                                break
                            else:
                                print('insufficent funds')
                                print()
                        elif (user_choice4 == 5):
                            x = 1500
                            if x < m:

                                AUTO_or_one_off()
                                bool4 = False
                                bool1 = False
                                break
                            else:
                                print('insufficent funds')
                                print()
                        elif (user_choice4 == 6):
                            x = 3000
                            if x < m:

                                AUTO_or_one_off()
                                bool4 = False
                                bool1 = False
                                break
                            else:
                                print('insufficent funds')
                                print()
                        elif (user_choice4 == 7):
                            x = 3500
                            if x < m:

                                AUTO_or_one_off()
                                bool4 = False
                                bool1 = False
                                break
                            else:
                                print('insufficent funds')
                                print()
                        elif (user_choice4 == 8):
                            x = 4000
                            if x < m:

                                AUTO_or_one_off()
                                bool4 = False
                                bool1 = False
                                break
                            else:
                                print('insufficent funds')
                                print()
                        elif (user_choice4 == 99):
                            bool5 = True
                            while (bool5 == True):
                                print(
                                    """9. #5,500 FOR 20GB (30 DAYS) \n 10. #6,500 FOR 25GB (30 DAYS) \n 11. #11,000 FOR 40GB (30 DAYS) \n 12. #16,000 FOR 75GB (30 DAYS) \n 13. #22,000 FOR 120GB (30 DAYS) \n 0. back""")
                                print()
                                user_choice5 = self.input_int('please enter your choice hear: ')
                                print()
                                if (user_choice5 == 9):
                                    x = 5500
                                    if x < m:

                                        AUTO_or_one_off()
                                        bool5 = False
                                        bool4 = False
                                        bool1 = False

                                        break
                                    else:
                                        print('insufficent funds')
                                        print()
                                elif (user_choice5 == 10):
                                    x = 6500
                                    if x < m:

                                        AUTO_or_one_off()
                                        bool5 = False
                                        bool4 = False
                                        bool1 = False

                                        break
                                    else:
                                        print('insufficent funds')
                                        print()
                                elif (user_choice5 == 11):
                                    x = 11000
                                    if x < m:

                                        AUTO_or_one_off()
                                        bool5 = False
                                        bool4 = False
                                        bool1 = False
                                        break
                                    else:
                                        print('insufficent funds')
                                        print()
                                elif (user_choice5 == 12):
                                    x = 16000
                                    if x < m:

                                        AUTO_or_one_off()
                                        bool5 = False
                                        bool4 = False
                                        bool1 = False
                                        break
                                    else:
                                        print('insufficent funds')
                                        print()
                                elif (user_choice5 == 13):
                                    x = 22000
                                    if x < m:

                                        AUTO_or_one_off()
                                        bool5 = False
                                        bool4 = False
                                        bool1 = False
                                        break
                                    else:
                                        print('insufficent funds')
                                        print()

                                elif (user_choice5 == 0):
                                    bool5 = False
                                    bool4 = True
                                    bool1 = False
                                else:
                                    print('wrong input')
                                    print()
                        elif (user_choice4 == 0):
                            bool4 = False
                            bool1 = True

                        else:
                            print('wrong input')
                            print()


                elif (user_choice1 == 4):
                    bool6 = True
                    while (bool6 == True):
                        print(
                            """1. #20,000 FOR 100GB( 60 DAYS)\n 2. #30,000 FOR 160GB(60 DAYS)\n 3. #`50,000 FOR 400GB(90 DAYS) \n 4. #75,000 FOR 600GB (90 DAYS) \n 0. back """)
                        print()
                        user_choice6 = self.input_int('please enter your choice hear: ')
                        print()
                        if (user_choice6 == 1):
                            x = 20000
                            if x < m:

                                AUTO_or_one_off()
                                bool6 = False
                                bool1 = False

                                break
                            else:
                                print('insuffficent funds')
                                print()
                        elif (user_choice6 == 2):
                            x = 30000
                            if x < m:

                                AUTO_or_one_off()
                                bool6 = False
                                bool1 = False
                                break
                            else:
                                print('insufficent funds')
                                print()
                        elif (user_choice6 == 3):
                            x = 50000
                            if x < m:

                                AUTO_or_one_off()
                                bool6 = False
                                bool1 = False
                                break
                            else:
                                print('insufficent funds')
                                print()
                        elif (user_choice6 == 4):
                            x = 75000
                            if x < m:

                                AUTO_or_one_off()
                                bool6 = False
                                bool1 = False
                                break
                            else:
                                print('insufficent funds')
                                print()
                        elif (user_choice6 == 0):
                            bool6 = False
                            bool1 = True
                        else:
                            print('wrong input')
                            print()
                elif (user_choice1 == 5):
                    social_plan()
                    bool1 = False
                else:
                    print('wrong input entered')
                    print()

        def glo_network():
            nonlocal x
            # nonlocal person_username
            nonlocal current_function
            nonlocal current_network
            current_function = 'glo_network'
            current_network = 'glo_network'
            balance_details = f"""SELECT balance FROM user_details WHERE username = '{self.username}';"""
            result = read_query2(connection, balance_details)
            for m in result:
                pass

            print(f'your balance is: {m} ')
            print('   ')
            bool1 = True
            while (bool1 == True):
                print(
                    """1. mini plan  \n 2. monthly plan \n 3. nigh and weekend plan \n 4. social media plan """)
                print()
                user_choice1 = self.input_int('please enter your choice hear')
                print()
                if (user_choice1 == 1):
                    bool2 = True
                    while (bool2 == True):
                        print(
                            """1. #100 FOR 150MB (1 DAY INCL 35MB NITE) \n 2. #200 FOR 350MB (2 DAYS INCL 110MB) \n 3. #500 FOR 1.8GB (14DAYS INCL 1GB NITE) \n 4. #50 FOR 50MB (1 DAY INCL 5MB NITE)  0. back""")
                        print()
                        user_choice2 = self.input_int('please enter your choice hear: ')
                        print()
                        if (user_choice2 == 1):
                            x = 100
                            if x < m:

                                AUTO_or_one_off()
                                bool2 = False
                                bool1 = False
                                break
                            else:
                                print('insufficent funds')
                                print()
                        elif (user_choice2 == 2):
                            x = 200
                            if x < m:

                                AUTO_or_one_off()
                                bool2 = False
                                bool1 = False
                                break
                            else:
                                print('insufficent funds')
                                print()
                        elif (user_choice2 == 3):
                            x = 500
                            if x < m:

                                AUTO_or_one_off()
                                bool2 = False
                                bool1 = False
                                break
                            else:
                                print('insufficent funds')
                                print()

                        elif (user_choice2 == 4):
                            x = 50
                            if x < m:

                                AUTO_or_one_off()
                                bool2 = False
                                bool1 = False
                                break
                            else:
                                print('insufficent funds')
                                print()
                        elif (user_choice2 == 0):
                            bool2 = False
                            bool1 = True
                        else:
                            print('wrong input')
                            print()
                elif (user_choice1 == 2):
                    bool3 = True
                    while (bool3 == True):
                        print(
                            """1. #1000 FOR 3.9GB( 30 DAYS INCL 12GN NITE) \n 2. #1500 FOR 7.5GB(30 DAYS INCL 4GB NITE) \n 3. #`2000 FOR 9.2GB(30 DAYS INCL 4GB NITE) \n 4. #2500 FOR 10.8GB (30 DAYS INCL 4GB NITE) \n 5. #3000 FOR 14GB (30 DAYS INCL 4GB NITE) \n 6. #4000 FOR 18GB (30 DAYS INCL NITE) \n 7. #5000 FOR 24GB (30 DAYS INCL 4GB NITE) \n 8. #8000 FOR 29.5GB (30 DAYS INCL 4GB NITE) \n 99. next \n 0. back """)
                        print()
                        user_choice3 = self.input_int('please enter your choice hear: ')
                        print()
                        if (user_choice3 == 1):
                            x = 1000
                            if x < m:
                                AUTO_or_one_off()
                                bool3 = False
                                bool1 = False

                                break
                            else:
                                print('insuffficent funds')
                                print()
                        elif (user_choice3 == 2):
                            x = 1500
                            if x < m:

                                AUTO_or_one_off()
                                bool3 = False
                                bool1 = False
                                break
                            else:
                                print('insufficent funds')
                                print()
                        elif (user_choice3 == 3):
                            x = 2000
                            if x < m:

                                AUTO_or_one_off()
                                bool3 = False
                                bool1 = False
                                break
                            else:
                                print('insufficent funds')
                                print()
                        elif (user_choice3 == 4):
                            x = 2500
                            if x < m:

                                AUTO_or_one_off()
                                bool3 = False
                                bool1 = False
                                break
                            else:
                                print('insufficent funds')
                                print()
                        elif (user_choice3 == 5):
                            x = 3000
                            if x < m:

                                AUTO_or_one_off()
                                bool3 = False
                                bool1 = False
                                break
                            else:
                                print('insufficent funds')
                                print()
                        elif (user_choice3 == 6):
                            x = 4000
                            if x < m:

                                AUTO_or_one_off()
                                bool3 = False
                                bool1 = False
                                break
                            else:
                                print('insufficent funds')
                                print()
                        elif (user_choice3 == 7):
                            x = 5000
                            if x < m:

                                AUTO_or_one_off()
                                bool3 = False
                                bool1 = False
                                break
                            else:
                                print('insufficent funds')
                                print()
                        elif (user_choice3 == 8):
                            x = 8000
                            if x < m:

                                AUTO_or_one_off()
                                bool3 = False
                                bool1 = False
                                break
                            else:
                                print('insufficent funds')
                                print()
                        elif (user_choice3 == 99):
                            bool4 = True
                            while (bool4 == True):
                                print(
                                    """9. #10,000 FOR 50GB (30 DAYS INCL 4GB NITE) \n 10. #15,000 FOR 93GB (30 DAYS INCL 7GB NITE) \n 11. #18,000 FOR 119GB (30 DAYS INCL 10GB NITE) \n 12. #20,000 FOR 138GB (30 DAYS INCL 12GB NITE) \n 0. back""")
                                print()
                                user_choice4 = self.input_int('please enter your choice hear: ')
                                print()
                                if (user_choice4 == 9):
                                    x = 10000
                                    if x < m:

                                        AUTO_or_one_off()

                                        bool4 = False
                                        bool3 = False
                                        bool1 = False

                                        break
                                    else:
                                        print('insufficent funds')
                                        print()
                                elif (user_choice4 == 10):
                                    x = 15000
                                    if x < m:

                                        AUTO_or_one_off()
                                        bool4 = False
                                        bool3 = False
                                        bool1 = False

                                        break
                                    else:
                                        print('insufficent funds')
                                        print()
                                elif (user_choice4 == 11):
                                    x = 18000
                                    if x < m:

                                        AUTO_or_one_off()
                                        bool4 = False
                                        bool3 = False
                                        bool1 = False
                                        break
                                    else:
                                        print('insufficent funds')
                                        print()

                                elif (user_choice4 == 12):
                                    x = 20000
                                    if x < m:

                                        AUTO_or_one_off()
                                        bool4 = False
                                        bool3 = False
                                        bool1 = False
                                        break
                                    else:
                                        print('insufficent funds')
                                        print()


                                elif (user_choice4 == 0):
                                    bool3 = True
                                    bool4 = False
                                    bool1 = False
                                else:
                                    print('wrong input')
                                    print()
                        elif (user_choice3 == 0):
                            bool3 = False
                            bool1 = True

                        else:
                            print('wrong input')
                            print()
                elif (user_choice1 == 3):
                    bool5 = True
                    while (bool5 == True):
                        print(
                            """1. #25 FOR 250MB( 1 DAY 12AM-05AM) \n 2. #50 FOR 500MB(1 DAY 12AM-05AM) \n 3. #100 FOR 1GB(5 DAYS 12AM-05AM) \n 4. #200 FOR 1.25GB (30 DAYS INCL 4GB NITE) \n 5. #500 FOR 3GB (2 DAYS SAT-SUN)  \n 0. back """)
                        print()
                        user_choice5 = self.input_int('please enter your choice hear: ')
                        print()
                        if (user_choice5 == 1):
                            x = 25
                            if x < m:

                                AUTO_or_one_off()
                                bool5 = False
                                bool1 = False

                                break
                            else:
                                print('insuffficent funds')
                                print()

                        elif (user_choice5 == 2):
                            x = 50
                            if x < m:

                                AUTO_or_one_off()
                                bool5 = False
                                bool1 = False
                                break
                            else:
                                print('insufficent funds')
                                print()
                        elif (user_choice5 == 3):
                            x = 100
                            if x < m:

                                AUTO_or_one_off()
                                bool5 = False
                                bool1 = False
                                break
                            else:
                                print('insufficent funds')
                                print()

                        elif (user_choice5 == 4):
                            x = 200
                            if x < m:

                                AUTO_or_one_off()
                                bool5 = False
                                bool1 = False
                                break
                            else:
                                print('insufficent funds')
                                print()
                        elif (user_choice5 == 5):
                            x = 3000
                            if x < m:

                                AUTO_or_one_off()
                                bool5 = False
                                bool1 = False
                                break
                            else:
                                print('insufficent funds')
                                print()
                        elif (user_choice5 == 0):
                            bool5 = False
                            bool1 = True
                elif (user_choice1 == 4):
                    social_plan()
                    bool1 = False
                else:
                    print('wrong input entered')
                    print()

        def airtel_network():
            nonlocal x
            #  nonlocal person_username
            nonlocal current_function
            nonlocal current_network
            current_function = 'airtel_network'
            current_network = 'airtel_network'
            balance_details = f"""SELECT balance FROM user_details WHERE username = '{self.username}';"""
            result = read_query2(connection, balance_details)
            for m in result:
                pass

            print(f'your balance is: {m} ')
            bool1 = True
            while (bool1 == True):
                print("""1. daily plan  \n 2. monthly plan \n 3. social media plan """)
                print()
                user_choice1 = self.input_int('please enter your choice hear')
                print()
                if (user_choice1 == 1):
                    bool2 = True
                    while (bool2 == True):
                        print(
                            """1. #50 FOR 50MB (1 DAY) \n 2. #100 FOR 100MB (1 DAY) \n 3. #150 FOR 200MB (1DAY) \n 4. #200 FOR 650MB (1 DAY ) \n 5. #300 FOR 1GB (1 DAY ) \n 6. #500 FOR 2GB (3 DAYS ) \n 7. #1,500 FOR 7GB (7 DAYS ) \n 0. back""")
                        print()
                        user_choice2 = self.input_int('please enter your choice hear: ')
                        print()
                        if (user_choice2 == 1):
                            x = 50
                            if x < m:

                                AUTO_or_one_off()
                                bool2 = False
                                bool1 = False
                                break
                            else:
                                print('insufficent funds')
                                print()
                        elif (user_choice2 == 2):
                            x = 100
                            if x < m:

                                AUTO_or_one_off()
                                bool2 = False
                                bool1 = False
                                break
                            else:
                                print('insufficent funds')
                                print()
                        elif (user_choice2 == 3):
                            x = 150
                            if x < m:

                                AUTO_or_one_off()
                                bool2 = False
                                bool1 = False
                                break
                            else:
                                print('insufficent funds')
                                print()

                        elif (user_choice2 == 4):
                            x = 200
                            if x < m:

                                AUTO_or_one_off()
                                bool2 = False
                                bool1 = False
                                break
                            else:
                                print('insufficent funds')
                                print()
                        elif (user_choice2 == 5):
                            x = 300
                            if x < m:

                                AUTO_or_one_off()
                                bool2 = False
                                bool1 = False
                                break
                            else:
                                print('insufficent funds')
                                print()
                        elif (user_choice2 == 6):
                            x = 500
                            if x < m:

                                AUTO_or_one_off()
                                bool2 = False
                                bool1 = False
                                break
                            else:
                                print('insufficent funds')
                                print()
                        elif (user_choice2 == 7):
                            x = 1500
                            if x < m:

                                AUTO_or_one_off()
                                bool2 = False
                                bool1 = False
                                break
                            else:
                                print('insufficent funds')
                                print()

                        elif (user_choice2 == 0):
                            bool2 = False
                            bool1 = True
                        else:
                            print('wrong input')
                            print()
                elif (user_choice1 == 2):
                    bool3 = True
                    while (bool3 == True):
                        print(
                            """1. #1000 FOR 4GB (30 DAYS) \n 2. #1200 FOR 6.2GB (30 DAYS) \n 3. #2000 FOR 9.5GB (30 DAYS) \n 4. #2500 FOR 11GB (30 DAYS ) \n 5. #3000 FOR 15GB (30 DAYS ) \n 6. #4000 FOR 18.5GB (30 DAYS ) \n 7. #5000 FOR 22GB (30 DAYS ) \n 8. #20,000 FOR 125GB (30 DAYS ) 0. back""")
                        print()
                        user_choice3 = self.input_int('please enter your choice hear: ')
                        print()
                        if (user_choice3 == 1):
                            x = 1000
                            if x < m:

                                AUTO_or_one_off()
                                bool3 = False
                                bool1 = False
                                break
                            else:
                                print('insufficent funds')
                                print()
                        elif (user_choice3 == 2):
                            x = 1200
                            if x < m:

                                AUTO_or_one_off()
                                bool3 = False
                                bool1 = False
                                break
                            else:
                                print('insufficent funds')
                                print()
                        elif (user_choice3 == 3):
                            x = 2000
                            if x < m:

                                AUTO_or_one_off()
                                bool3 = False
                                bool1 = False
                                break
                            else:
                                print('insufficent funds')
                                print()

                        elif (user_choice3 == 4):
                            x = 2500
                            if x < m:
                                AUTO_or_one_off()
                                bool3 = False
                                bool1 = False
                                break
                            else:
                                print('insufficent funds')
                                print()
                        elif (user_choice3 == 5):
                            x = 3000
                            if x < m:
                                AUTO_or_one_off()
                                bool3 = False
                                bool1 = False
                                break
                            else:
                                print('insufficent funds')
                                print()
                        elif (user_choice3 == 6):
                            x = 4000
                            if x < m:

                                AUTO_or_one_off()
                                bool3 = False
                                bool1 = False
                                break
                            else:
                                print('insufficent funds')
                                print()
                        elif (user_choice3 == 7):
                            x = 5000
                            if x < m:

                                AUTO_or_one_off()
                                bool3 = False
                                bool1 = False
                                break
                            else:
                                print('insufficent funds')
                                print()
                        elif (user_choice3 == 8):
                            x = 20000
                            if x < m:

                                AUTO_or_one_off()
                                bool3 = False
                                bool1 = False
                                break
                            else:
                                print('insufficent funds')
                                print()

                        elif (user_choice3 == 0):
                            bool3 = False
                            bool1 = True
                        else:
                            print('wrong input')
                            print()
                elif (user_choice1 == 3):
                    social_plan()
                    bool1 = False
                else:
                    print('wrong input entered')
                    print()

        num3 = 10
        while (num3 == 10):
            print('1. BUY AIRTIME \n 2. PURCHASE DATA_ BUNDLE')
            print()
            user_choice1 = self.input_int('please enter your choice here: ')
            print()
            if (user_choice1 == 1):
                buy_airtime()
                num3 = 15
                num2 = 15
                num = 16
            elif (user_choice1 == 2):
                print('pls enter the phone number you will like to purchase data for below')
                print()
                phone_number = self.input_int('pls enter the phone number here: ')
                print()
                print('PLEASE SELECT THE NETWORK \n 1. MTN NETWORK \n 2. GLO_NETWORK \n 3. AIRTEL_NETWORK \n 4. 9 MOBILE NETWORK ')

                print()
                num4 = 10
                while (num4 == 10):
                    user_choice2 = self.input_int('please enter your choice here: ')
                    print()

                    if (user_choice2 == 1):
                        mtn_network()
                        num4 = 15
                        num3 = 15
                        num2 = 15
                        num = 16
                    elif (user_choice2 == 2):
                        glo_network()
                        num4 = 15
                        num3 = 15
                        num2 = 15
                        num = 16
                    elif (user_choice2 == 3):
                        airtel_network()
                        num4 = 15
                        num3 = 15
                        num2 = 15
                        num = 16
                    elif (user_choice2 == 4):
                        airtel_network()
                        num4 = 15
                        num3 = 15
                        num2 = 15
                        num = 16
                    else:
                        print('wrong input entered')
                        print()

            else:
                print('wrong input entered')
                print()

    def check_balance(self):
        get_user_balance = f"""SELECT balance FROM user_details WHERE username = '{self.username}'; """
        obtained_balance = read_query2(connection, get_user_balance)
        for i in obtained_balance:
            pass
        print(f'your account balance is {i}')
        print()

    def change_details(self):
        print('good day')
        print()
        print('select any of the credencails you will like to change')
        print()

        bool1 = True
        while (bool1 == True):
            print('1.PASSWORD \n 2. PIN \n 3.EMAIL \n 4. phone number ')
            print()
            user_choice1 = self.input_int('please enter your choice hear: ')
            print()
            if (user_choice1 == 1):
                bool2 = True
                while (bool2 == True):
                    print('please your password must contain words and numbers for security purpose')
                    print()
                    password_to_change = input(' please enter the password you will like to change:  ')
                    print()
                    pattern = re.compile(r'^(?=.*[A-Za-z])(?=.*\d).+$')
                    if pattern.match(password_to_change):
                        password_details4 = f"""  SELECT password FROM user_details WHERE username = '{self.username}' ; """
                        result4 = read_query2(connection, password_details4)
                        bool25 = True
                        while (bool25 == True):
                            if ((password_to_change,) != result4):
                                bool23 = True
                                while (bool23 == True):
                                    password_confirm = (input('please reenter your password to confirm:  '))
                                    print()
                                    if (password_to_change == password_confirm):
                                        print('password match')
                                        print()
                                        change_password = f"""UPDATE user_details SET password = '{password_to_change}' WHERE username = '{self.username}';"""
                                        execute_command = execute_query(connection, change_password)
                                        print('your password has been changed successfully thanks for using banking buddy')
                                        print()
                                        bool23 = False
                                        bool25 = False
                                        bool2 = False
                                        bool1 = False
                                        num2 = 16
                                        num = 13
                                        break
                                    else:
                                        print('password incorrect')
                                        print()
                            else:
                                print('you cant use your prevoius password for security reason')
                                print()
                                bool25 = False

                                bool2 = True

                    else:
                        print('please your password must contain letter and numbers')
                        print()
            elif (user_choice1 == 2):
                bool3 = True
                while (bool3 == True):
                    pin = input('please enter the 4 digit pin you will like to change: ')
                    print()
                    if len(str(pin)) != 4:
                        print('please your pin can only be 4 digits')
                        print()
                    elif not pin.isdigit():
                        print('pin must contain only digits. please enter a valid number.')
                        print()
                    else:
                        bool4 = True
                        while (bool4 == True):
                            pin2 = input('please reenter your pin to confirm:  ')
                            print()
                            if (pin == pin2):
                                print('pin match')

                                print()
                                change_pin = f"""UPDATE user_details SET pin = {pin2} WHERE username = '{self.username}';"""
                                execute_command_pin = execute_query(connection, change_pin)
                                print('your pin has been changed successfully thanks for using banking buddy')
                                print()
                                bool4 = False
                                bool3 = False
                                bool1 = False
                                num2 = 14
                                num = 13
                                break
                            elif not pin2.isdigit():
                                print('pin must contain only digits. please enter a valid number.')
                                print()
                            else:
                                print(
                                    'your confirm pin is not correct pins do not match and your pin might not be up to 4 digits')
                                print()
            elif (user_choice1 == 3):
                user_email = input('please enter the email you will like to change hear: ')
                print()
                update_email = f"""UPDATE user_details SET email = '{user_email}' WHERE username = '{self.username}';"""
                execute_command_email = execute_query(connection, update_email)
                print('your email has been changed successfully thanks for using banking buddy')
                print()
                bool1 = False
                num2 = 13
                num = 13
                break
            elif (user_choice1 == 4):
                bool5 = True
                while (bool5 == True):
                    phone_number = input('pls enter the  phone number you like to change to: ')
                    print()
                    if (len(str(phone_number))) != 11:
                        print('phone number can only be 10 digits')
                        print()
                    elif not phone_number.isdigit():
                        print('phone number  must contain only digits. please enter a valid number.')
                        print()

                    else:
                        update_phone_number = f"""UPDATE user_details SET phonenumber = '{phone_number}' WHERE username = '{self.username}';"""
                        execute_command_email = execute_query(connection, update_phone_number)
                        print('your phone number has been changed successfully thanks for using banking buddy')
                        print()

                        bool1 = False
                        num2 = 13
                        bool5 = False
                        num = 13
                        break
            else:
                print('wrong input inputed')
                print()


saved_username = None
bank_obj = Banking_Application(saved_username)


# bank_obj.create_account()
# bank_obj.buy_airtime_or_buy_databundle()
# bank_obj.add_money()
# bank_obj.change_details()
# bank_obj.transfer_money()
# bank_obj.check_balance()


def input_int2(prompt):
    while True:
        try:
            value = int(input(prompt))
            print()
            return value
        except ValueError:
            print('invalid input! please you can only enter an integer.')
            print()


bool_main = True
while (bool_main == True):
    if check_internet_connection():
        bool1 = True
        while (bool1 == True):
            print('welcome to BANKING BUDDY')
            print()

            print('please make sure your device is connected to the internet before procceding')
            print()
            print('please read before inputing choice')
            print()
            print('1.SIGN UP(CREATE AN ACCOUNT) \n 2.SIGN IN')
            print()
            user_choice1 = input_int2('please enter your chioce hear: ')
            print()
            if (user_choice1 == 1):
                bank_obj.create_account()

            elif (user_choice1 == 2):
                bool2 = True
                while (bool2 == True):
                    username1 = input('please enter your username: ')
                    print()
                    password = input('please enter your password here: ')
                    print()
                    get_username = """SELECT username FROM user_details; """
                    display_username = read_query(connection, get_username)
                    get_password = """SELECT password FROM user_details;"""
                    display_password = read_query(connection, get_password)
                    if (username1,) in display_username and (password,) in display_password:
                        bool23 = True
                        while (bool23 == True):
                            bool3 = True
                            while (bool3 == True):
                                bank_obj.username = username1
                                print(
                                    '1.ADD MONEY \n 2.TRANSFER MONEY \n 3.BUY AIRTIME OR DATA BUNDLE \n 4.CHECK BALANCE \n 5.CHANGE DETAILS ')
                                print()
                                userchoice2 = input_int2('please enter your choice hear: ')
                                print()
                                if (userchoice2 == 1):
                                    bank_obj.add_money()
                                    bool3 = False
                                    bool2 = False
                                    bool1 = False
                                    bool23 = False
                                    bool_main = False
                                    break
                                elif (userchoice2 == 2):
                                    bank_obj.transfer_money()
                                    bool3 = False
                                    bool2 = False
                                    bool1 = False
                                    bool23 = False
                                    bool_main = False
                                    break
                                elif (userchoice2 == 3):
                                    bank_obj.buy_airtime_or_buy_databundle()
                                    bool3 = False
                                    bool2 = False
                                    bool1 = False
                                    bool23 = False
                                    bool_main = False
                                    break
                                elif (userchoice2 == 4):
                                    bank_obj.check_balance()
                                    bool3 = False
                                    bool2 = False
                                    bool1 = False
                                    bool23 = False
                                    bool_main = False
                                    break
                                elif (userchoice2 == 5):
                                    bank_obj.change_details()
                                    bool3 = False
                                    bool2 = False
                                    bool1 = False
                                    bool23 = False
                                    bool_main = False
                                    break
                                else:
                                    print('wrong input entered')
                                    print()

                            bool4 = True
                            while (bool4 == True):
                                print('Do you which to perform another operation\n1.yes\n2.no')
                                print()
                                userchoice3 = input_int2('please enter your choice hear: ')
                                print()
                                if (userchoice3 == 1):
                                    pass
                                    bool4 = False
                                    bool23 = True

                                elif (userchoice3 == 2):
                                    bool4 = False
                                    bool3 = False
                                    bool2 = False
                                    bool1 = False
                                    bool23 = False
                                    break
                                else:
                                    print('wrong input entered')
                                    print()



                    else:
                        print('your username or password entered is incorrect')
                        print()
                        bool4 = True
                        while (bool4 == True):
                            print('1.TO TRY AGAIN\n2.FORGOTTEN CREDEDENTIALS')
                            print()
                            userchoice4 = input_int2('please enter your choice hear: ')
                            print()
                            if (userchoice4 == 1):
                                bool2 = True
                                bool4 = False
                            elif (userchoice4 == 2):
                                print('please plus check your email while entering')
                                print()
                                bool5 = True
                                while (bool5 == True):

                                    user_email = input('please enter your email here: ')
                                    print()
                                    get_useremail = """SELECT email FROM user_details; """
                                    display_useremail = read_query(connection, get_useremail)
                                    if (user_email,) in display_useremail:
                                        print('please enter your gmail address and gmail app password below for the automatic gmail sender')
                                        email12 = input("Enter your Gmail address to receive transaction receipts: ")
                                        password12 = input("Enter your Gmail App Password: ")
                                        code = ''.join(str(random.randint(0, 9)) for i in range(4))
                                        msg = MIMEText(f'your verification code is {code}')
                                        msg['Subject'] = 'verification code'
                                        msg['From'] = email12
                                        msg['To'] = user_email

                                        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
                                            # server.starttls()
                                            server.login(email12,password12)
                                            server.send_message(msg)
                                        print('a 4 digit code as been sent to your email please input it below')
                                        print()
                                        bool6 = True
                                        while (bool6 == True):

                                            pin_entering = int(input('enter the 4 digit here: '))
                                            print()
                                            if (int(code) == pin_entering):
                                                get_username = f"""SELECT username FROM user_details WHERE email = '{user_email}' ; """
                                                display_useremail = read_query2(connection, get_username)
                                                get_userpassword = f"""SELECT password FROM user_details WHERE email = '{user_email}' ; """
                                                display_userpassword = read_query2(connection, get_userpassword)
                                                for j in display_useremail:
                                                    pass
                                                for p in display_userpassword:
                                                    pass
                                                print(f'your username is: {j}\nyour password is:{p}')
                                                print()
                                                print('re try entering your credentials')
                                                print()
                                                bool6 = False
                                                bool5 = False
                                                bool4 = False
                                                bool3 = False
                                                bool2 = True

                                            else:
                                                print('wrong code inputed')
                                                print()


                                    else:
                                        print('please this email is invalid')
                                        print()
                            else:
                                print('wrong input entered')
                                print()
            else:
                print('wrong input entered')
                print()

    else:
        print('No internet connection. please connect to the internet and wait let your code run')
        print()
        time.sleep(10)






