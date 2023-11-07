
BAD_PASSWORDS = ['password', 'letmein', 'sesame', 'hello', 'justinbieber']
Newpassword = input("Please enter your new password:")[:12]

if Newpassword in BAD_PASSWORDS:
    print("Error you may not use this password")
else: CheckPass = input("Please re-enter your new password:")

if len(Newpassword) > 12:
    print("Password too long")

if Newpassword == 'CheckPass':
    print("Password set")

elif Newpassword != 'Checkpass':
    print("Error 404")