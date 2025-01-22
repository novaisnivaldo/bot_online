from telethon import TelegramClient, sync, events
from time import sleep
import requests
from senhas import api_hash,api_id

sessao = 'Repassagem Mensagem'

def main():
        print ('Monitoriamento iniciado...')
        client = TelegramClient (sessao, api_id, api_hash)
        tabela_size = 100
        tabela_bot = []
        @client.on(events.NewMessage(chats = [1002356837091]))
        async def enviar_mensagem(event):
            msg_orig = event.raw_text
            linhas = msg_orig.strip().split('\n')
            linhas_filtradas = [linhas[0], linhas[1], linhas[2], linhas[3], linhas[4]]
            mensagem_filtrada = '\n'.join(linhas_filtradas)

            def remove_linhas_com_palavras(msg_orig, palavras):
                linhas = msg_orig.splitlines()
                linhas_excluidas = [
                    linha for linha in linhas
                    if not any(palavra.lower() in linha.lower() for palavra in palavras)
                ]
                return "\n".join(linhas_excluidas)
            texto = msg_orig
            palavras = ["robô", "Bug","green365","Estatísticas"]
            texto_filtrado = remove_linhas_com_palavras(texto, palavras)

            def processar_mensagem(msg_orig):
                 if "Relatório Diário" in msg_orig:
                      return texto_filtrado
                 else:
                      return mensagem_filtrada
            msg_replace = processar_mensagem(msg_orig)
            msg_send = msg_replace.replace("📈", "🎮 ").replace("🕓","⏰ ").replace("🅿️", "⚽️ ").replace("🥇","🏆 ").replace("🏆Tip:","Resultado:")
            msg_copy = await client.send_message(-1002481733456,msg_send)
            id_msg_copy = msg_copy.id
            id_msg_orig = event.message.id
            if len(tabela_bot) >= tabela_size:
                tabela_bot.pop(0)
            tabela_bot.append([id_msg_orig,id_msg_copy])

        @client.on(events.MessageEdited(chats = [1002356837091]))
        async def enviar_mensagem(event):
            msg_editada = event.raw_text
            linhas = msg_editada.strip().split('\n')
            linhas_filtradas = [linhas[0], linhas[1], linhas[2], linhas[3], linhas[4], linhas[5], linhas[1], linhas[27]]
            msg_filtrada = '\n'.join(linhas_filtradas)
            msg_replace = msg_filtrada.replace("📈", "🎮 ").replace("🕓","⏰ ").replace("🅿️", "⚽️ ").replace("🥇","🏆 ").replace("🏆Tip:","Resultado:")
            msg_alt = event.message.id
            for i in range(len(tabela_bot)):
                if msg_alt == tabela_bot[i][0]:
                    msg_edit = tabela_bot[i][1]
                    break
            await client.edit_message(-1002481733456,msg_edit,msg_replace)

        client.start()
        client.run_until_disconnected()
main()
