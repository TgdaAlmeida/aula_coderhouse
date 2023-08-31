import pandas as pd
import requests
from datetime import datetime
from plyer import notification


#url = 'https://brasilapi.com.br/api/banks/v1' #bancos ok
#url = 'https://brasilapi.com.br/api#tag/TAXAS/ibge/uf/v1' #capitais erro 404
url = 'https://brasilapi.com.br/api/cvm/corretoras/v1' #corretoras ok



def Alerta(nivel, base, etapa):
    base = base
    etapa = etapa
    data_atual = datetime.now()
    data_formatada = data_atual.strftime('%d/%m/%d')
    mensagem = (f'Falha no carregamento da base {base} na etapa {etapa} em {data_formatada}')
    titulo = nivel
    notification.notify(title=titulo, message=mensagem, timeout=10)

while True:
    response = requests.get(url)
    response_code = response.status_code
    break
if response_code == 200:
    data_json = response.json()
    #df = pd.DataFrame(data_json)
    print('Requisição Completa')
elif response_code >= 400 and response_code < 500:
    nivel = 'ATENÇÃO: Erro Grave'
    Alerta(nivel = nivel, base='Data_Bank',etapa='Extração')
elif response_code >=500 and response_code < 600:
    nivel = 'ATENÇÃO: Erro Médio'
    Alerta(nivel = nivel, base='Data_Bank',etapa='Extração')
else:
    print('Erro Desconhecido')

df = pd.DataFrame(data_json)

print(df.head())