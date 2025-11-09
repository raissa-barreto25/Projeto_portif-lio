from __future__ import print_function
import datetime
import os.path
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

SCOPES = ['https://www.googleapis.com/auth/calendar']

def conectar_google_calendar():
    creds = None
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    service = build('calendar', 'v3', credentials=creds)
    return service


def registrar_pedido(nome_cliente, sabor, data_entrega, observacoes=""):
    service = conectar_google_calendar()

    # 🗓️ Converte a data e calcula diferença
    hoje = datetime.date.today()
    data_entrega_date = datetime.datetime.strptime(data_entrega, "%Y-%m-%d").date()
    diferenca = (data_entrega_date - hoje).days

    # 🚫 Regra 1: Pedido com pelo menos 2 dias de antecedência
    if diferenca < 2:
        print("❌ O agendamento deve ser feito com pelo menos 2 dias de antecedência.")
        return

    # 🚫 Regra 2: Bloquear certos dias (exemplo: domingo e feriados)
    dias_bloqueados = [
        datetime.date(2025, 12, 25),  # Natal
        datetime.date(2025, 1, 1),    # Ano Novo
    ]
    if data_entrega_date.weekday() == 6 or data_entrega_date in dias_bloqueados:
        print("🚫 Esse dia não está disponível para agendamento.")
        return

    # 📊 Regra 3: Limite de pedidos por dia
    eventos_existentes = service.events().list(
        calendarId='primary',
        timeMin=f"{data_entrega}T00:00:00-03:00",
        timeMax=f"{data_entrega}T23:59:59-03:00",
        singleEvents=True
    ).execute()

    limite_diario = 3  # máximo de pedidos por dia
    if len(eventos_existentes.get('items', [])) >= limite_diario:
        print("⚠️ Limite diário de pedidos atingido para essa data.")
        return

    # ✅ Cria o evento
    evento = {
        'summary': f'Pedido de {nome_cliente} - {sabor}',
        'description': observacoes,
        'start': {
            'dateTime': f'{data_entrega}T09:00:00',
            'timeZone': 'America/Sao_Paulo',
        },
        'end': {
            'dateTime': f'{data_entrega}T10:00:00',
            'timeZone': 'America/Sao_Paulo',
        },
    }

    event = service.events().insert(calendarId='primary', body=evento).execute()
    print(f"✅ Pedido registrado com sucesso: {event.get('htmlLink')}")


# 💡 Exemplo de uso
registrar_pedido(
    nome_cliente="Maria Clara",
    sabor="Red Velvet",
    data_entrega="2025-11-08",  # teste alterando a data
    observacoes="Retirar na loja às 15h"
)
