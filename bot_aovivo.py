from telethon import TelegramClient, sync, events
from time import sleep
import requests
from senhas import api_hash,api_id

sessao = 'Repassagem Mensagem'

def main():
        print ('Monitoriamento iniciado...')
        client = TelegramClient (sessao, api_id, api_hash)
        @client.on(events.NewMessage(chats = [4506407899]))
        async def enviar_mensagem(event):
            # Mensagem original
            mensagem = event.raw_text
            # Dividir a mensagem em linhas
            linhas = mensagem.strip().split('\n')
            # Selecionar as linhas desejadas (1, 3, 4 e 5)
            linhas_filtradas = [linhas[0], linhas[2], linhas[3], linhas[4], linhas[5]]
            # Juntar as linhas filtradas de volta em uma string
            mensagem_filtrada = '\n'.join(linhas_filtradas)
            print(mensagem_filtrada)
            #print(mensagem)
            #print(event.raw_text)
            await client.send_message(-1002481733456,mensagem_filtrada)
        client.start()
        client.run_until_disconnected()
main()