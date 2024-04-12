import secrets
import string as s
from secrets import SystemRandom as sr
 
random = secrets.SystemRandom() 

# print(s.ascii_letters, s.digits, s.punctuation)

senha_forte = "".join(random.choices(s.ascii_letters + s.digits + s.punctuation, k=12))

print(senha_forte)