import json
from datetime import datetime
from pathlib import Path

import streamlit as st

ARQUIVO_MENSAGENS = Path(__file__).with_name("mensagens.json")
LOGO = Path(__file__).with_name("logo.svg")

st.set_page_config(
    page_title="Chatte",
    page_icon=str(LOGO),
    layout="wide",
)


def carregar_mensagens():
    """Carrega as mensagens salvas; retorna uma lista vazia se não houver arquivo válido."""
    if not ARQUIVO_MENSAGENS.exists():
        return []

    try:
        with ARQUIVO_MENSAGENS.open("r", encoding="utf-8") as arquivo:
            dados = json.load(arquivo)
        return dados if isinstance(dados, list) else []
    except (json.JSONDecodeError, OSError):
        return []


def salvar_mensagens(mensagens):
    """Grava a lista de mensagens no arquivo JSON."""
    with ARQUIVO_MENSAGENS.open("w", encoding="utf-8") as arquivo:
        json.dump(mensagens, arquivo, indent=4, ensure_ascii=False)


def adicionar_mensagem(username, mensagem):
    """Cria e salva uma mensagem no início do histórico."""
    mensagens = carregar_mensagens()
    horario = datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
    mensagens.insert(0, {
        "time": horario,
        "username": username,
        "mensagem": mensagem,
    })
    salvar_mensagens(mensagens)


logo_col, titulo_col = st.columns([0.5, 8], gap="small", vertical_alignment="center")
with logo_col:
    st.image(str(LOGO), width=64)
with titulo_col:
    st.title("Chatte")

st.caption("Uma conversa simples, feita por você.")

username = st.sidebar.text_input(
    "Seu nome no chat",
    key="username",
    value="Anônimo",
    max_chars=20,
).strip()


@st.fragment(run_every=3)
def renderizar_chat():
    mensagens = carregar_mensagens()
    with st.container(border=True, height=500):
        for msg in mensagens:
            st.write(f"{msg['time']} — {msg['username']}: {msg['mensagem']}")


renderizar_chat()

entrada_mensagem = st.chat_input("Escreva uma mensagem...", max_chars=500)
if entrada_mensagem and entrada_mensagem.strip():
    adicionar_mensagem(username or "Anônimo", entrada_mensagem.strip())
    st.rerun()
