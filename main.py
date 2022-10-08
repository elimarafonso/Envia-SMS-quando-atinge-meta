import pandas as pd
import os
from twilio.rest import Client

account_sid = 'AC71837a387a88b1a61cc4565dc06a61f6'
auth_token = '3d5cd402a89834c66a1e5cffa05c8bbf'
client = Client(account_sid, auth_token)


lista_meses = ['janeiro', 'fevereiro', 'março', 'maio', 'junho']


for mes in lista_meses:
    tabela_vendas = pd.read_excel(f'{mes}.xlsx')

    if(tabela_vendas['Vendas'] > 40000).any():
        vendedor = tabela_vendas.loc[tabela_vendas['Vendas'] > 40000, 'Vendedor'].values[0]
        vendas = tabela_vendas.loc[tabela_vendas['Vendas'] > 40000, 'Vendas'].values[0]
        print(f'No mês {mes} alguém bateu a meta. Vendedor: {vendedor}  e Vendas: {vendas}')


        message = client.messages.create(
            body=f'{vendedor} BATEU A META  DE {mes}!!',
            from_='+13253960349',
            to='+5533998029799'
        )
        print(message.sid)
