#! python3
#passw_locker.py -> An insecure password locker program
import sys
import pyperclip

PASSWORDS = {'email': 'F7minlBDDuvMJuxESSKHFhTxFtjVB6',
             'blog': 'VmALvQyKAxiVH5G8v01if1MLZF3sdt',
             'luggage': '12345'}
#first cmd argument will be account name
#since it's mandatory, display message to user so they remember to add it

if len(sys.argv) < 2:
    #first item in list is script name, second is first arg -> len=2
    print("Usage: python passw_locker.py [account] - copy account password")
    sys.exit()

account = sys.argv[1]
if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print('Password for ' + account + ' copied to clipboard')
else:
    print('There is no account named ' + account)
