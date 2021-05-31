email = input("Enter your email: "). strip() # get input from the user, strip function removes extra space on both sides
username = email[: email.index('@')] # variable will store names that occur before @
domain = email[email.index('@') + 1:]
print (f"Your username is {username} and domain is {domain}") # format text  It enables you to concatenate parts of a string at desired intervals through point data format.


email = input("Enter email: ").strip()
username = email[: email.index('a')]
domain = email[email.index('@') +1:]

print(f"username = {username} and your domain = {domain}")


email = input("Enter email: ").strip()
username = email[: email.index('a')]
domain = email[email.index('@') +1:]

print(f"username = {username}\ndomain = {domain}")
