import os
import json
import glob
import time

from multiprocessing import Process

def organize_data(directory_archive) :

    remove_pipe = list()
    remove_keys = list()
    only_keys = list()
    main_output = list()
    secondary_output = dict()
    
    arch = open(directory_archive, 'r')
    remove_slashn = [name.strip() for name in arch.readlines()] #Lista em que cada posição se refere a uma linha do arquivo lido e sem o '\n' no final.

    for lines in remove_slashn :
        remove_pipe.append(lines.split('|')) #Lista cujos elementos são os mesmos da lista 'remove_slashn', com a exceção de que os pipes são removidos.

    for lines in remove_pipe[1:] : 
        remove_keys.append(lines) #Lista sem a linha que contem as chaves - primeira linha.

    for lines_one in range(len(remove_keys)):
        only_keys = remove_pipe[0]

        for lines_two in range(len(remove_keys[lines_one])) :
            secondary_output[only_keys[lines_two]] = remove_keys[lines_one][lines_two] #Dicionário
            
        main_output.append(secondary_output.copy()) #Lista final contendo os dicionarios criados no passo anterior.

    arch.close()

    return main_output
    
def write_json(txt_data) :
    
    if os.path.isfile('Destino/data_json.json') : 

        #Se o arquivo existe, ele é aberto e concatenam-se os dados antigos e os atuais e reescreve o arquivo.
        open_arch = open('Destino/data_json.json', 'r+') 
        read = open_arch.read()
        data_txt = json.loads(read)
        concatenated_data = json.dumps(txt_data + data_txt, indent = 2)
        open_arch.seek(0) #Escrever a partir do inicio, para não precisar apagar o arquivo toda vez.
        open_arch.write(concatenated_data)
       
    else :
        #Se o arquivo não existe, abre-se um arquivo e escreve-se os dados atuais nele.
        open_arch = open('Destino/data_json.json', 'w+')
        data_json = json.dumps(txt_data, indent = 2)
        open_arch.write(data_json)

if __name__ == '__main__' :

    #Processo principal a ser executado, que despacha tarefas para o subprocesso.
    while True :
 
        archives = sorted(glob.glob('Origem/*.csv'), reverse = True)

        if archives :
            for archive in archives :
                txt_data = organize_data(archive)
                write_json(txt_data)
                subprocess = Process(target = organize_data, args = (archive,)) #Subprocesso a ser executado, que executa as tarefas.  
                subprocess.start()
                subprocess.join()
                os.unlink(archive)

                print('Os dados foram devidamente processados.')
                print('\n')

        else :
            print("Não existem mais dados a serem processados.")
            print('\n')

        time.sleep(2)
