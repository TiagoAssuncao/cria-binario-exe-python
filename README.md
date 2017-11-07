# Cria Binário exe - Python3.6

Aplicação de criação de binários para plataforma Windows utilizando Scripts python na versão 3.6.

Com este código é possível transformar um script qualquer python na versão 3.6 para um binário de execução em uma plataforma
windows.
Neste, basta apenas indicar para a aplicação qual é o script que necessita ser transformado. Após isto, o exe estará pronto dentro
de uma pasta chamada build.

![Python](https://www.iped.com.br/img/cursos/60190.jpg)
## Instalação 
Para instalar esta aplicação, é necessário instalar algumas depedências python que estão todas listadas no
arquivo requirements.txt. O gerenciar de pacotes python é o pip. Desta forma, basta apenas utilizar o instalador
do pip passando as depedências necessárias. Este irá acessar o repositório remoto da pypi, onde todos os pacotes python estão armazenados, baixá-los e instalá-los.  
```bash
pip3 install -r requirements.txt
```

## Usando a aplicação
O uso da aplicação pode ser divido em dois passos. O primeiro se trata da configuração dos procedimentos. A segunda diz respeito
à chamada do sistema para criar o executável. Estas serão explicadas nas próximas sessões.


### Configuração do Processo

Para configurarmos a aplicação, são necessários dois passos básicos: 
1. Colocar o script que desejamos compilar no mesmo diretório deste projeto, exatamente no mesmo nível do arquivo setup.py
2. Alterar os parâmetros do arquivo config.ini, passando as opções que desejamos. 

O primeiro passo, referente a ter o script na mesma pasta do arquivo setup.py pode ser resolvido apenas salvando o arquivo
neste diretório ou simplesmente o copiando.

Já o segundo passo consiste em entrar no  arquivo e alterar as opções de acordo com o desejado. O arquivo config.ini possui
quatro opções que podem ser parametrizadas.

1.  Script: nome do script que será alvo da transformação
2.  Version: número da versão do script, que será refletida no executável
3.  Description: descrição do script
4.  Autor: autor da aplicação criada

Um exemplo de configuração do arquivo config.ini está a seguir:

```ini
[Info]
  Script: armazena.py
  Version: 1.0.1
  Description: Script python para fins criptograficos
  Autor: Rael
```

### Criando o Executável
Agora que o arquivo de configuração está pronto, podemos então iniciar o processo de criação do executável.
Toda vez que este comando for executado, uma pasta build será criada. Dentro tela, terá uma pasta contendo
todos os pacotes necessários da aplicação. Além disso, existirá um executável exe com o exato nome que foi passado
para o script no arquivo de configuração. 

É recomendado apagar a pasta build ao criá-la novamente, caso já exista.

![setup](https://www.visualstudio.com/wp-content/uploads/2016/06/python-1-562x309@2x-op.png)
De toda maneira, tomada essas precauções, para a criação do binário é necessário rodar o seguinte comando:

`
python3 setup.py build
`

Este irá criar o executável ou mostrar uma mensagem na tela caso haja algum erro da compilação do arquivo.

## Limitações da Aplicação
Esta aplicação se limita nos seguintes pontos:

1. Caso haja algum erro no script em tempo de execução, este deve ser tratado pelo programador que o executou.
Todos os erros existentes não serão apresentados ao usuário em tempo de execução. O programa irá apenas ser encerrado.
Desta maneira, todo script deve ser testado e avaliado antes de ser transformado em executável. O programador
deverá tomar todos os devidos cuidados com a aplicação para que esta não se encerre enquanto o usuário a estiver utilizando.

2. Esta aplicação transforma apenas scripts de um único arquivo em um executável. Esta não irá operar corretamente com uso
de módulos, projetos e aplicações como Flask, Django, DRF e derivados.

3. Esta aplicação opera utilizando a linguagem de programação Python 3.6. Outras versões e outras linguagens não são
aceitas ou não funcionarão corretamente como o esperado.
