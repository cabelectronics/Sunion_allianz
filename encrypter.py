from cryptography import fernet
from cryptography.fernet import Fernet

pswd = 'Anze015p'
key = Fernet.generate_key()
print(key)
fernet = Fernet(key)
encPSWD = fernet.encrypt(pswd.encode())
print(encPSWD)
#encMessage = fernet.encrypt(message.encode())