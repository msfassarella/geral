import numpy as np
import pickle
import argparse
import time
import paho.mqtt.client as mqtt


parser = argparse.ArgumentParser(description='Codigo de update do arquivo pickle')
parser.add_argument('func',type=str,help='escolha a funcionalidade a ser usada')
parser.add_argument('principal',type=str,help='nome do arquivo pickle principal ou nome do usuario a ser apagado',default='nada')
parser.add_argument('secundario',type=str,help='nome do arquivo pickle 2 que serah adicionado no arquivo principal',default='nada')
args = parser.parse_args()


# se chamar func no cmd voce pode escolhe entre as funcoes abaixo ao escolhelas deve passar os parametros necessarios de cada funcao para que a execucao ocorra da forma certa


broker_address="mqtt.de.vix.br"
#broker_address="iot.eclipse.org" #use external broker
client = mqtt.Client("AtualizouPickle") #create new instance
client.connect(broker_address) #connect to broker

# updateVersao
# Atualiza o arquivo de versionamento do arquivo pickle
# 
def updateVersao(nomearquivo):
    with open(nomearquivo, 'r+') as file:
        versaostr = file.readline()
        numversao = versaostr.split(':')[1]
        numversaoatualizado = round(float(numversao) + 0.1, 1)
        versaostr = versaostr.replace(numversao, str(numversaoatualizado))
        file.seek(0)
        file.write(versaostr)
        file.truncate()


def update(datadst,datasrc):
    try:
        data = pickle.loads(open(datadst , "rb").read())
        data2 = pickle.loads(open(datasrc , "rb").read())
    except:
        print('arquivo nao encontrado')
    for k in range(1):
        data = np.append(data,data2)
        data = dict(data)
    print(data)
    with open(datadst + "2", 'wb') as file:
        pickle.dump(data, file)
    updateVersao('doc')
    client.publish("almoxerife/estoque/rsync", "ON")


# Apaga um usuario do arquivo pickle
def apagaUsuario(datadst,nome):
    try:
        data = pickle.loads(open(datadst , "rb").read())
    except:
        print('Arquivo nao encontrado')
        return 0 


    nomes = data['names']
    arraycodificado = data['encodings']

    #cria novas listas sem os dados do nome a ser deletado    
    arraycodificadonovo = []
    nomesnovo = []
    for cnt in range(len(nomes)):
        if nome in nomes[cnt]:
            #print("Remover nome e array")
            pass
        else:
            #print("Manter nome e dados do usuario")
            arraycodificadonovo.append(arraycodificado[cnt])
            nomesnovo.append(nomes[cnt])


    #dicionario novo
    dicnovo =  {'encodings': arraycodificadonovo, 'names': nomesnovo}

    #salva no arquivo
    with open(datadst, 'wb') as file:
        pickle.dump(dicnovo, file)

    return dicnovo


# Retorna uma lista nao ordenada com os nomes que estao no dicionario do arquivo pickle
# Esperado que o arquivo tenha o seguinte formato: {'encodings': array de encondings, 'names': array de nomes}
def listar(datadst, nada):
    data = pickle.loads(open(datadst , "rb").read())
    nomes = data['names']
    usuarios = list(set(nomes))
    print (usuarios)
    return usuarios


def getdicionarioaoperacoes():
    return {'update':update, 'apagarUsuario': apagaUsuario, 'listar': listar}

#execucao
dicfuncoes = getdicionarioaoperacoes()
funcao = dicfuncoes[args.func]
funcao(args.principal, args.secundario)

'''
if args.func == 'update':
    update(args.data,args.data2,args.arq)
    
 
    

elif args.func == 'apagar':
    print(apagaUsuario(args.data,args.nome,args.arq))

elif args.func == 'listar':
    print(listar(args.data))
'''








