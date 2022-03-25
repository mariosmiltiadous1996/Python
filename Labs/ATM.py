import getpass
from random import *
import random

def cls():
    print '\n' * 100
    
def welcome_message():
    global flag, count
    print '============================================================'
    print "======================[Password Entry]======================"
    print '============================================================'
    print
    name = random.choice(passwords.keys())
    Pass = passwords[name]
    print 'Hello %s!' % name
    print
    tries = 3
    while tries > 1:
        password = input('Please enter your 4-digit password: ')
        if password == Pass:
            tries = 0
            cls()
            options()
            break
        else:
            tries -= 1
            cls()
            msg = raw_input('\nThe password you entered is incorect. \nYou have %s more tries. \n\nTry again?[Y/N]: ' % tries)
            if msg == 'N' or msg == 'n':
                tries = 0
                break
            cls()
            print '============================================================'
            print "======================[Password Entry]======================"
            print '============================================================'
            print
    '''while tries > 0:
        password = input('Please enter your 4-digit password: ')
        tries -= 1
        for i in range(len(passwords)):
            if password in passwords.values():
                tries = 0
                cls()
                options()
                break
            else:
                print
                msg = raw_input('The password you entered is incorect. You have %s more tries. Try again?[Y/N]: ' % tries)
                if msg == 'N' or msg == 'n':
                    tries = 0
                    break
                print'''

def closure():
    global flag_3, amount, sum_50, sum_20
    cls()
    if flag_3:
        with open('atm.txt', 'a') as fl:
            fl.write('==============================================================')
            fl.write("\n======================[Transaction Info]======================")
            fl.write('\n==============================================================')
            fl.write('\n')
            fl.write('\nAmount: %s Euros' % amount)
            fl.write('\nNumber of 50s Euros: %s' % sum_50)
            fl.write('\nNumber of 20s Euros: %s' % sum_20)
            fl.write('\n\n\n')
            fl.write('-------------------------------------------------------------------------')
            fl.write('\n\n\n')
    print 'Thank you for using our sercives and we hope our services will be in your preferences. Have a good day!'

def options():
    global flag
    while flag:
        cls()
        print '================================================================================'
        print "======================[Welcome to STiXzoOR's Advanced ATM]======================"
        print '================================================================================'
        print
        print '1. Withdraw Money'
        print '2. View Your Current Balance'
        print '3. Exit'
        print
        option = input('How can i help you with? Please choose an option[1-3]: ')
        if option == 1:
            option_1()
        if option == 2:
            option_2()
        if option == 3:
            option_3()
    closure()

def option_1():
    global flag, amount
    cls()
    print '============================================================'
    print "======================[Withdraw Money]======================"
    print '============================================================'
    print
    print 'You can only withdraw from 20 to 600 Euros.'
    print 'You will recieve the money in 50s and 20s only.'
    print '------------------------------------------------'
    print
    amount = input('Please enter the amount: ')
    if (amount % 10 == 0) and (20 <= amount <= 600):
        calc_money(amount)
    else:
        print 'Wrong amount!!'
    msg = raw_input('Do you want to use our services again?[Y/N]: ')
    if msg == 'N' or msg == 'n':
        flag = False

def option_2():
    global flag, balance, new_balance, count
    cls()
    print '============================================================'
    print "======================[Widthraw Money]======================"
    print '============================================================'
    print
    print 'Your current balance is: %s Euros' % balance
    print
    msg = raw_input('Do you want to use our services again?[Y/N]: ')
    if msg == 'N' or msg == 'n':
        flag = False

def option_3():
    global flag
    flag = False

def calc_money(amount):
    global flag_3, balance, new_balance, sum_20, sum_50, count
    flag_2 = True
    sum_20 = 0
    sum_50 = 0
    if (amount < balance):
        if amount % 50 == 0:
            sum_50 = amount / 50
        else:
            remainder = amount % 50
            sum_20 = remainder / 20
            if remainder == 30:
                if amount != 30:
                    sum_50 = (amount/50)-1
                    sum_20 +=3
                else:
                    cls()
                    print "You can't widthraw that value choose a different one."
                    flag_2 = False
            elif remainder == 10:
                sum_50 = (amount/50)-1
                sum_20 +=3
            else:
                sum_50 = amount / 50
        if flag_2:
            flag_3 = True
            balance = balance - amount
            cls()
            print '=============================================================='
            print "======================[Transaction Info]======================"
            print '=============================================================='
            print
            print 'Amount:', amount, 'Euros'
            print 'Number of 50s Euros:', sum_50
            print 'Number of 20s Euros:', sum_20
            print
            closure()
            flag_3 = False
    else:
       cls()
       print "Your balance remainder doesn't fit for this transaction. Please choose a different one."
       print

passwords = {
    'Andreas Christou': 1234
    }

amount = None
sum_20 = None
sum_50 = None
balance = randint(10,3500)
new_balance = None
count = 0
flag = True
flag_3 = None

welcome_message()
