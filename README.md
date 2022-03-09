# Portfólio

- **Autor:** Gustavo Pereira Lemes Molina
- **Apelido:** TM
- **Contato:** **tm.dev.io@gmail.com**

## Estrutura de arquivos

```
portfólio
├─ doc
|  ├─ wireframe.pdf
├─ src
|  ├─ static
|  |  ├─ css
|  |  |  └─ arquivos (.css)
|  |  ├─ img
|  |  |  └─ imagens (.png)
|  |  ├─ js
|  |  |  └─ main.js  
|  ├─ templates
|  |  └─ arquivos (.html)
|  └─ app.py
├─ .gitignore
├─ README.md
└─ requirements.txt
 ```
### Descrição das pastas
 > **Pasta doc:** possui o wireframe do projeto

 > **Pasta src:** possui o código fonte do projeto, arquivos .css, .html, .js e .py


## Frameworks e plugins usados
- **[Tailwindcss:](https://tailwindcss.com/)** Framework utilizada para a estilização e auxílio na responsividade

- **[Flickity:](https://flickity.metafizzy.co/)** Plugin utilizado para fazer o slider de cards encontrado na seção 'Minhas habilidades' 


## Como rodar a aplicação

Tendo a ferramenta Git e o Python instalados em seu computador:
- Abra o Prompt de Comando no caminho de um novo diretório e copie o seguinte comando para clonar o nosso repositório:

```
git clone https://github.com/TheMachineDev/portfolio.git
```
- Dentro da pasta root do projeto, crie um Ambiente Virtual com o seguite comando:
```
python3 -m venv venv
```
ou caso tenha o python3 já instalado
```
python -m venv venv
```
(Obs.: caso você utilize um sistema operacional diferente do Windows, verifique comandos alternativos neste [Link](https://docs.python.org/pt-br/3/library/venv.html) .)
- Isso criará o diretório  ```venv```. Agora ative o Ambiente Virtual com o comando:
```
venv\Scripts\activate
```
- Você deverá ver o ambiente virtual ativado antes do caminho do seu diretório, assim:
``` (venv) C:\...```
- Agora instale as dependências do projeto:
``` 
pip install -r requirements.txt
```
- Agora certifique-se que está no diretório ```src``` e para executar a aplicação, execute o comando:
```
flask run
```
- A aplicação estará rodando na url indicada pelo prompt de comando.
