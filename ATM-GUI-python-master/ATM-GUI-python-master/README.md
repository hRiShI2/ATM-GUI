# ATM GUI using Python and bash scripts
The system saves users' data(name, password, balance) in a file named data.txt in a directory named with the account's ID. 
The text file DB.txt, in Database directory contains all accounts with their ID, name and account status.\
The system offers 5 services for the user:
- create new account
- withdraw cash
- check balance
- change password
- 4 payment services 
  
3 services for the admin
- delete account
- get account data
- search accounts using name
     
The system accepts only a password with a length four, and if the password is incorrect 3 times, 
the system locks the account and changes account status to locked.\
Maximum allowed value per transaction is 5000, and must be a multiple of 100.
