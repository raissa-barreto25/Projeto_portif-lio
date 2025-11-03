import datetime
import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# Se modificar esses escopos, delete o arquivo token.json.
SCOPES = ["https://www.googleapis.com/auth/calendar.readonly"]

def main():
    """Mostra como se autenticar e listar os próximos eventos do Google Calendar."""
    creds = None
    # O arquivo token.json armazena os tokens de acesso e atualização do usuário,
    # e é criado automaticamente na primeira vez que o fluxo de autorização é concluído.
    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)
    
    # Se não houver credenciais válidas disponíveis, o usuário é autenticado.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                "credentials.json", SCOPES
            )
            creds = flow.run_local_server(port=0)
        # Salva as credenciais para a próxima execução
        with open("token.json", "w") as token:
            token.write(creds.to_json())

    try:
        service = build("calendar", "v3", credentials=creds)

        # Chama a API do Google Calendar
        now = datetime.datetime.now(datetime.UTC).isoformat() + "Z"  # RFC3339 format
        print("Obtendo os próximos 10 eventos...")
        events_result = (
            service.events()
            .list(
                calendarId="primary",
                timeMin=now,
                maxResults=10,
                singleEvents=True,
                orderBy="startTime",
            )
            .execute()
        )
        events = events_result.get("items", [])

        if not events:
            print("Nenhum evento futuro encontrado.")
            return

        # Imprime os eventos
        for event in events:
            start = event["start"].get("dateTime", event["start"].get("date"))
            print(f"{start} - {event['summary']}")

    except HttpError as error:
        print(f"Ocorreu um erro na API: {error}")


if __name__ == "__main__":
    main()
# Use o código com cuidado.

# Como executar no VS Code:
# Salve o arquivo credentials.json (baixado do Google Cloud Console) na mesma pasta que agenda_script.py.
# Abra o terminal integrado no VS Code (atalho Ctrl + ').
# Execute o script:
# bash
# python agenda_script.py