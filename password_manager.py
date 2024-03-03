def inputs(inputs, color_code = 32):
     return input(f"\033[{color_code}m{inputs}\033[0m")

def prints(text,color_code = 35):
    return print(f"\033[{color_code}m{text}\033[0m")

master_pwd = inputs("What is the master password? ",36)

def view():
    with open('password.txt','r') as f:
        for line in f.readlines():
            prints(line.rstrip())
            # print(f.read())
            
def add():
    name = inputs("Account name: ",33)
    pwd = inputs("password: ",33)

    with open('password.txt','a') as f:
        f.write(name+"|"+pwd + "\n")
        
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