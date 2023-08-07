# Chamar os pacotes necessários para atribuição.

from plyer import notification
from datetime import datetime

# Criação da função.

def alerta(nivel, base, etapa):

    # Criação das variáveis de hora e mensagem.

    hora_alerta = str(datetime.now())
    danger = f'Falha no carregamento da base de {base} na etapa {etapa}.\n {hora_alerta}'

    # Usei a condicional (if, elif e else) para determinar a entrada do nível de alerta.

    if nivel == 1:
        titulo ='DANGER...Alerta Baixo'
    elif nivel == 2:
        titulo = 'DANGER...Alerta Médio'
    elif nivel == 3:
        titulo = 'DANGER...Alerta Alto'
    else:
        print(f'Indisponibilida de Nível {nivel}')

    # notification.notify para criar/configurar a os quesitos do alerta.

    notification.notify(
            title=titulo,
            message=danger,
            app_name='alerta',
            timeout=10)
    
# Produção.        

alerta(nivel = 1, base = 'CLIENTES', etapa = 'EXTRAÇÃO')

alerta(nivel = 2, base = 'CLIENTES', etapa = 'EXTRAÇÃO')

alerta( nivel = 3, base = 'CLIENTES', etapa = 'EXTRAÇÃO')