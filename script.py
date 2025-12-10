#Importação da Biblioteca Requirida
import qrcode

# Variável onde será armazenada a URL:
url = input("Enter the URL: ").strip()

# Caminho de Destino do QRCODE ( Ajuste conforme seu sistema operacional )
file_path = "Seu caminho de destino no seu computador onde será salvo o seu QRCODE"

# Inicialização do Gerador QR Code
qr = qrcode.QRCode()

# Adição dos Dados
qr.add_data(url)

# Geração da Imagem do QR Code
img = qr.make_image()

# Salvamento do Arquivo
img.save(file_path)

# Mensagem de Confirmação
print("QR Code was generated!")