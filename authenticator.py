import hashlib

username = input('Digite seu username:')
password = input('Digite sua senha:')

#definindo variaveis para converter os dados em hash
hash1 = hashlib.sha256(b"Kryp10N1938").hexdigest()
hash2 = hashlib.sha256(b"k@ne1939FInGer").hexdigest()
hash3 = hashlib.sha256(b"F@lK1936bEnG@1@").hexdigest()



if password == hash1 and username == "kent":
    print('Logado com sucesso!')

elif password == hash2 and username == "wayne":
    print('Logado com sucesso!')

elif password == hash3 and username == "walker": 
    print('Logado com sucesso!')

else:
    print('Usuário/senha inválidos!')

###########


usuarios = []

usuario = {

    "name": "Clark Kent",

    "username": "kent",

    "password": "Kryp10N1938"

}

usuarios.append(usuario)

usuario = {

    "name": "Bruce Wayne",

    "username": "wayne",

    "password": "k@ne1939FInGer"
}

usuarios.append(usuario)

usuario = {

    "name": "Christopher Walker",

    "username": "walker",

    "password": "F@lK1936bEnG@1@"

}

usuarios.append(usuario)

rm = input('Digite seu rm no terminal:')
print (rm)
