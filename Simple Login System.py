#!/usr/bin/env python
# coding: utf-8

# ### Simple Login System
# #### Features include:
# ##### Store a username and password
# ##### Ask user to input both
# ##### check correctness
# ##### give max 3 attempts

# In[4]:


username = "olamidejoshua.1"
password = "joshua23"
attempts = 0
max_attempts = 3

while attempts < max_attempts:
    user_name = input("Enter the username: ")
    pass_word = input("Enter the password: ")

    attempts += 1

    if user_name == username and pass_word == password:
        print(f"Login successful! You successfully logged in with {attempts} attempts")
        break

    elif user_name != username and pass_word != password:
        print("Incorrect username and password")
        print(f"Attempts left: {max_attempts - attempts}")

    elif user_name != username:
        print("Incorrect username")
        print(f"Attempts left: {max_attempts - attempts}")

    else:
        print("Incorrect password")
        print(f"Attempts left: {max_attempts - attempts}")

else:
    print("Too many failed attempts. Access denied.")


# In[ ]:




