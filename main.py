import pywhatkit
import time
import pyautogui
from datetime import datetime

# Número de destino e mensagem formal desejada
destino_numero = '+55 85 9985-8662'
mensagem = (
    'Olá! Meu nome é Rafael de Jesus. Estou realizando testes com um ChatBotWpp 100% automatizado criado com Python e OpenAI. '
    'Seu número foi escolhido para participar. '
    'Fique à vontade para me seguir no Instagram @rafaeldeje. '
    'Agradeço pela compreensão e participação!'
)

# Tempo de espera para abrir o WhatsApp Web (20 segundos)
time.sleep(20)

# Posicione o cursor no campo de entrada da mensagem no WhatsApp Web (ajuste conforme necessário)
pyautogui.click(x=500, y=500)  # Substitua pelas coordenadas corretas

# Aguarde um breve momento antes de iniciar a digitação
time.sleep(2)

# Simula a digitação da mensagem letra por letra com um pequeno intervalo
pyautogui.write(mensagem, interval=0.1)

# Aguarde um tempo antes de enviar (15 segundos)
time.sleep(15)

# Enviar mensagem
pywhatkit.sendwhatmsg(destino_numero, mensagem, datetime.now().hour, datetime.now().minute + 2)

# Aguarde um tempo após o envio (15 segundos)
time.sleep(15)

# Fechar a janela com Ctrl + W
pyautogui.hotkey('ctrl', 'w')
