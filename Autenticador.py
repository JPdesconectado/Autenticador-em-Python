from Usuario import Usuarios
import os, hashlib

def defineidentifier():
    vdd = True
    while (vdd):
        identifier = input("Digite o nome de usuário:\n")
        user = Usuarios()
        users = user.selectAllUsers()
        i = 0
        for usuarios in users:
                if usuarios[1] == identifier: 
                    i = 1
                    print("nome de usuário em uso.\n")
                    break
                else:
                    continue
        if (i == 0):
            vdd = False        
    return identifier

def registerUser():
        identifier = defineidentifier()
        user = Usuarios()
        user.usuario = identifier
        password = input("Digite a senha:\n")
        sal = os.urandom(32)
        passhash = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), sal, 100000)

        user.passhash = passhash
        user.sal = sal
        print(user.insertUser())


def verifyIdentifier():
    identifier = input("Digite o nome de usuário:\n")
    user = Usuarios()
    users = user.selectAllUsers()
    for usuarios in users:
            if usuarios[1] == identifier: 
                verifyPassword(identifier)
                break
    else:
        print("Usuário não cadastrado.")

def verifyPassword(identifier):
    password = input("Digite a senha:\n")
    user = Usuarios()
    user.selectUser(identifier)
    sal = user.sal
    passhash = user.passhash
    new_hash = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), sal, 100000)
    if (passhash == new_hash):
        print("\n\n\n------------- Usuário Logado com Sucesso! -------------")

    else:
        print("Erro no Login.")
        
while True:
    print("----------- Menu Fabuloso -----------")
    print("[1] Identificação")
    print("[2] Verificação")
    choice = input("Opção:")
    choice = int(choice)
    if (choice == 1):
        registerUser()
    elif (choice == 2):
        verifyIdentifier()