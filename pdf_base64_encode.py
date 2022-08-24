import base64

try:
    with open("file.pdf", "rb") as pdf_file:
        file = open("base64.txt", "w+")
        file.write(base64.b64encode(pdf_file.read()).decode())
        file.close()
        print("-> Os dados foram gerados e salvos em base64.txt")
except Exception as error:
    print("-> Ocorreu um problema! Certifique-se que o arquivo foi adicionado corretamente.")
