INSTRUÇÕES GERAIS

1 - O script a ser executado é denominado de 'scriptdefinitivo.py'.
2 - Os arquivos a serem processados ('data_one.csv' e 'data_two.csv') pelo script estão na pasta 'Origem'.
3 - A pasta 'Destino' deve receber o arquivo 'data_json.json' quando os arquivos da pasta 'Origem' forem devidamente lidos e apagados (comentar a linha 'os.unlink(archive)' do script para que os arquivos não sejam apagados).
4 - Os arquivos 'data_one.csv' e 'data_two.csv' também estão na raiz da pasta para serem copiados para a pasta 'Origem' caso o script já tenha sido executado uma vez e os arquivos tenham sido apagados da pasta 'Origem' e deseje-se executar o script novamente.
5 - O documento 'Protocolo Netflow.pdf' na raiz da pasta corresponde a segunda atividade (descrição sobre o Protocolo NetFlow).