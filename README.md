# QR-Generator

QR-Generator é um projeto feito em Python para geração de QR codes com mais facilidade e menos dependências de ferramentas on-line para realização da mesma tarefa.

## Instalação

Use o gerenciador de pacotes [pip](https://pip.pypa.io/en/stable/) para instalar as dependências da aplicação presentes no arquivo ```requirements.txt```.

```bash
pip install -r requirements.txt
```

Se preferir, você pode criar um ambiente virtual ```venv``` para instalação das dependências do projeto, com o seguinte comando:

```bash
python -m venv venv

#após a criação da pasta venv

# no windows
.\venv\Scripts\actvate

# no Linux
source ./venv/bin/activate
```

## Uso

### Captura de tela do código 
<div align="center">
<img src="main_py.png" alt="Screenshot" width="500" height="550">
</div>

Para utilizar a aplicação, foi criada a função ```generate_qrcode(data, back_color, front_color, file_name)```, ela recebe alguns parâmetros:

- ```data```: dado que será inserido como informação do QR code;
- ```back_color```: aqui será passada uma tupla, com o código RGB da cor de fundo da imagem do qr-code gerada;
- ```front_color```: aqui será passada uma tupla, com o código RGB da cor do QR code gerado;
- ```file_name```: aqui será passado o nome do arquivo do QR code gerado.

Depois de alterar essas informações, utilize o comando abaixo para iniciar o arquivo ```main.py```:

```bash
python main.py
```

### Resultado após execução do projeto 
<div align="center">
<img src="qrcode.png" alt="Screenshot" width="200" height="200">
</div>

## Contribuições

Pull requests são bem-vindos. Para mudanças importantes, abra um chamado primeiro
para discutir o que você gostaria de mudar.


## Licença

[MIT](https://choosealicense.com/licenses/mit/)