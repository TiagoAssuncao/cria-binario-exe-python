"# cria-binario-exe-python" 

Aplicação de criação de binários para uma plataforma Windows a partir de Scripts python na versão 3.6.

Com este código é possível transformar um script qualquer python na versão 3.6 para um binário de execução em uma plataforma
windows.
Neste, basta apenas indicar para a aplicação qual é o script que necessita ser transformado. Após isto, o exe estará pronto dentro
de uma pasta chamada build.

# Instalação 
Para instalar esta aplicação, é necessário instalar algumas depedências python que estão todas listadas no
arquivo requirements.txt. O gerenciar de pacotes python é o pip. Desta forma, basta apenas utilizar o instalador
do pip passando as depedências necessárias. Este irá acessar o repositório remotoda pypi, onde todos os pacotes estão
armazenados, baixá-los e instalá-los.

```bash
pip3 install -r requirements.txt
```

# Usando a aplicação
O uso da aplicação pode ser divido em dois passos. O primeiro se trata da configuração dos procedimentos. A segunda diz respeito
à chamada do sistema para criar o executável. Estas serão explicadas nas próximas sessões.


### Configuração do Processo

Para configurarmos a aplicação, são necessários dois passos básicos: 
1. Colocar o script que desejamos compilar no mesmo diretório deste projeto, exatamente no mesmo nível do arquivo setup.py
2. Alterar os parâmetros do arquivo config.ini, passando as opções que desejamos. 

O primeiro passo, referente a ter o script na mesma pasta do arquivo setup.py pode ser resolvido apenas saltando o arquivo
neste diretório ou simplesmente o copiando.

Já o segundo passo consistem em entrar no  arquivo e alterar as opções de acordo com o desejado. O arquivo config.ini possui
quatro opções que podem ser parametrizadas. Além dessas opções, serão apresentados os seus respectivos significados. 

1.  Script: nome do script que será alvo da transformação
2.  Version: número da versão do script, que será refletida no executável
3.  Description: descrição do script
4.  Autor: autor da aplicação para

Um exemplo de configuração do arquivo config.ini está a seguir:

```ini
[Info]
  Script: armazena.py
  Version: 1.0.1
  Description: Script python para fins criptograficos
  Autor: Rael
```