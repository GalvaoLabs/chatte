# Chatte 💬

Um chat simples feito com Python e Streamlit. Cada pessoa pode escolher um nome, enviar mensagens e acompanhar as mensagens salvas no histórico local.

## Funcionalidades

- Escolha de nome de usuário na barra lateral (até 20 caracteres).
- Envio de mensagens (até 500 caracteres).
- Exibição do horário, nome e conteúdo de cada mensagem.
- Atualização automática do histórico a cada três segundos.
- Persistência local em `mensagens.json`.
- Logo vetorial própria em `logo.svg`.

## Requisitos

- Python 3.10 ou superior.
- Streamlit 1.37 ou superior (necessário para `st.fragment`).

## Como executar

1. Abra o terminal nesta pasta.
2. Crie e ative um ambiente virtual (opcional, mas recomendado):

   ```powershell
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```

3. Instale as dependências:

   ```powershell
   pip install -r requirements.txt
   ```

4. Inicie o aplicativo:

   ```powershell
   streamlit run app.py
   ```

O Streamlit abrirá o Chatte no navegador. O arquivo `mensagens.json` é criado automaticamente quando a primeira mensagem é enviada.

## Estrutura

```text
Chatte/
├── app.py
├── logo.svg
├── requirements.txt
└── README.md
```

## Como os dados são armazenados

As mensagens ficam em `mensagens.json`, na pasta do projeto. Esse armazenamento é adequado para um protótipo local de aprendizado. O arquivo não é um banco de dados multiusuário e pode apresentar limitações se várias pessoas gravarem ao mesmo tempo ou se o app for hospedado em um ambiente que não preserve arquivos locais.

## Próximas melhorias

- Exibir mensagens com os componentes `st.chat_message`.
- Adicionar opção para limpar o histórico.
- Migrar o armazenamento para SQLite.
- Criar salas ou conversas separadas.

## Tecnologias

- Python
- Streamlit
- JSON
