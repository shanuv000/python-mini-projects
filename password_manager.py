from cryptography.fernet import Fernet
# colors
def inputs(inputs, color_code = 32):
     return input(f"\033[{color_code}m{inputs}\033[0m")

def prints(text,color_code = 35):
    return print(f"\033[{color_code}m{text}\033[0m")

'''
def write_key():
    key =Fernet.generate_key()
    with open('key.key','wb') as key_file:
        key_file.write(key)
'''
def load_key():
    file= open("key.key",'rb')
    key = file.read()
    file.close()
    return key
master_pwd = inputs("What is the master password? ",36)
key = load_key() + master_pwd.encode()
fer = Fernet(key)

def view():
    with open('password.txt','r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user , passw = data.split('|')
            print('User:',user,'Password:',fer.decrypt(passw.encode()).decode())
            
def add():
    name = inputs("Account name: ",31)
    pwd = inputs("password: ",31)

    with open('password.txt','a') as f:
        f.write(name+"|"+fer.encrypt(pwd.encode()).decode() + "\n")
        
while True:
    mode = inputs("Would you like to add a new passeord or view the existing ones (view, add)?, press q to quit ").lower()
    if mode == 'q':
        break
    
    if mode == 'view':
        view()
    elif mode=='add':
        add()
    else: 
        print("Invalid mode")
        continue