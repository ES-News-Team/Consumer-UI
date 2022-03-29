# Consumer-UI
O objetivo desse projeto e oferecer um portal (front-end) para visualização de notícias.

# Tecnologia
Python 3.6 ou superior. Link para donwload e instalação: https://www.python.org/downloads/

Link para instalar pip: https://pip.pypa.io/en/stable/installation/

# Integrantes
Daniel de Souza Lima Junior  
Natalia Bíscaro  
Guilherme Garcia  

# Montando um Ambiente
Esses procedimentos devem ser feitos na raiz do projeto, e são exemplos em ambiente `Unix/Mac`.
1. Como criar [virtual environments](https://docs.python.org/3/library/venv.html)  
    ```
    python3 -m pip install virtualenv
    ```
2. Criando um ambiente virtual   
    ```
    python3 -m venv venv && source venv/bin/activate
    ```
3. Instalando dependências
    ```
    pip install -r requirements.txt
    ```
    As dependências usanda nesse projeto são:
    ```
    # dependências do flask
    click==8.1.0
    Flask==2.1.0
    itsdangerous==2.1.2
    Jinja2==3.1.1
    MarkupSafe==2.1.1
    Werkzeug==2.1.0

    # dependências do gunicorn
    gunicorn==20.1.0
    ```

# Desenvolvimento
```
python run.py
```

# Produção
```
gunicorn --bind 0.0.0.0:5000 "run:consumer_ui_service" --worker-class=gthread --threads=4 -w 4
```
