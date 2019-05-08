import string
import random


# Generating name functions
# You can create different surnames to increase the variety of usernames.
def generatingName():
    firstName = ["Kimmy", "Rose", "Apple", "Sophie", "Mary", "Susan", "Vicky", "Ann", "Josie", "Joyce", "Diana", "Isabel", "Natalie", "Kate", "Helen", "Wendy", "Grace", "Julie", "Kelly", "Sammy", "Emily"]

    surName = ["Chan", "Lee", "Wong", "Ho",
		"Cheung", "Li", "Tam", "Lau",
		"Tse", "Ma", "Kwan", "Yip"]
        
    return ''.join(random.choice(firstName) + ' '  + random.choice(surName))


# Generating a username
def username(size = 6, chars  = string.ascii_lowercase + random.choice(['$', '_'])):
    return ''.join(random.choice(chars) for _ in range(size))


# Generating a Email
def generatingEmail() :
    return ''.join(username() + '@seznam.cz')
