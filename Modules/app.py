'''
    ========== APLICAÇÃO PRINCIPAL ==========
'''

import flet as ft
import pandas as pd
import openpyxl
import bot

# Variável global que verifica se foi feito o upload do arquivo.
is_uploaded = False
# Variável que armazena a planilha lida.
global planilha
# Variável que armazena o caminho da planilha.
global file_path

<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 6257821 (Final version UI)
# Parâmetros padrão.
USUARIO = "06151282205"
SENHA = "M@riane8291"

<<<<<<< HEAD
=======
>>>>>>> ea536f6 (First Commit for UI)
=======
>>>>>>> 6257821 (Final version UI)
# Componentes.
# Título do app.
titulo_text = ft.Text(
    "BOT AUTOMAÇÃO PLANILHA RENOVAÇÃO",
    size=18,
    weight=ft.FontWeight.BOLD,
    font_family="Roboto",
    text_align=ft.TextAlign.CENTER
)

# Botões.
upload_button = ft.ElevatedButton(
    "Upload",
    icon=ft.Icons.UPLOAD_FILE,
)

executar_button = ft.ElevatedButton(
    "Executar",
    icon=ft.Icons.PLAY_CIRCLE
)

<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 6257821 (Final version UI)
# Campos para os parâmetros
usuario_field = ft.TextField(
    label="Digite seu nome de usuário",
    value=str(USUARIO),
    width=300
)

senha_field = ft.TextField(
    label="Digite a sua senha",
    value=str(SENHA),
    width=300
)

<<<<<<< HEAD
=======
>>>>>>> ea536f6 (First Commit for UI)
=======
>>>>>>> 6257821 (Final version UI)
# Status inicial.
status = ft.Text("Esperando planilha renovação...", text_align=ft.TextAlign.CENTER)

# Tela principal.
def main_page():
    return ft.View(
        "/main",
        controls=[
            ft.Column(
                [
                    # Cabeçalho
                    ft.Row([titulo_text], alignment=ft.MainAxisAlignment.CENTER),
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 6257821 (Final version UI)
                    ft.Container(height=300),

                    # Card de login sistema gestão.
                    ft.Row(
                         [usuario_field, senha_field],
                         alignment=ft.MainAxisAlignment.CENTER
                         ),

                    ft.Container(height=60),
<<<<<<< HEAD
=======
                    ft.Container(height=400),
>>>>>>> ea536f6 (First Commit for UI)
=======
>>>>>>> 6257821 (Final version UI)

                    # Botão de upload, executar e caixa de status.
                    ft.Container(
                        width=700,  # Mesma largura do card de configurações
                        content=ft.Column(
                            [
                                ft.Row(
                                    [upload_button, executar_button],
                                    alignment=ft.MainAxisAlignment.CENTER,
                                    spacing=50
                                ),
                                ft.Container(height=20),
                                ft.Card(
                                    content=ft.Container(
                                        content=ft.Column(
                                            [
                                                ft.Text("Status:", 
                                                       weight=ft.FontWeight.BOLD,
                                                       text_align=ft.TextAlign.CENTER),
                                                status,
                                            ],
                                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                        ),
                                        padding=20,
                                        alignment=ft.alignment.center,
                                    ),
                                ),
                            ],
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER
                        ),
                    ),
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER
            ),
        ],
    )

# Função principal para gerenciar as views.
def main(page: ft.Page):

    page.title = "Bot Automação Planilha"
    page.window_width = 800
    page.window_height = 700
    page.window_min_width = 600
    page.window_min_height = 600
    page.padding = 20
    page.scroll = ft.ScrollMode.AUTO

    # Função para upload do arquivo.
    def upload_file_result(e: ft.FilePickerResultEvent):
        global is_uploaded
        global planilha
        global file_path
        # Se arquivo encontrado.
        if e.files:
            # Obtém o caminho do arquivo selecionado.
            file_path = e.files[0].path

            try:
                planilha = pd.read_excel(file_path)
                is_uploaded = True
                status.value = "Arquivo carregado com sucesso!"
                status.update()
            except Exception as err:
                status.value = f"Erro ao processar o arquivo: {err}"
                status.update()

    # Função para fazer a limpeza da planilha.
    def execute_file(e):
        global is_uploaded
        if is_uploaded:

            status.value = "Processando arquivo..."
            status.update()
            # Verificar se as colunas necessárias existem
            if 'Codigo' not in planilha.columns:
                status.value = "Planilha deve conter coluna Codigo"
                status.update()
                return

<<<<<<< HEAD
<<<<<<< HEAD
            status.value = "Abrindo sistema gestão..."
            status.update()
            bot.abrir_gestao("06151282205", "M@riane8291")
            status.value = "Sistema aberto com sucesso!"
            status.update()

            status.value = "Procurando por clientes ..."
=======
            status.value = "Faça login no whatsApp web com o QR Code."
=======
            status.value = "Abrindo sistema gestão..."
>>>>>>> 6257821 (Final version UI)
            status.update()
            bot.abrir_gestao("06151282205", "M@riane8291")
            status.value = "Sistema aberto com sucesso!"
            status.update()

<<<<<<< HEAD
            status.value = "Enviando mensagens..."
>>>>>>> ea536f6 (First Commit for UI)
=======
            status.value = "Procurando por clientes ..."
>>>>>>> 6257821 (Final version UI)
            status.update()

            status.value = "Planilha processada com sucesso!"
            status.update()

        else:
            status.value = "Faça upload da planilha primeiro."
            status.update()

    #Cria o FilePicker para selecionar os arquivos.
    file_picker = ft.FilePicker(on_result=upload_file_result)

    # Associando funções aos botões.
    upload_button.on_click = lambda e: file_picker.pick_files(
        allow_multiple = False,
        allowed_extensions = ["xlsx"],
        )
    executar_button.on_click = execute_file

    # Configurando a página inicial.
    page.overlay.append(file_picker)
    page.views.append(main_page())
    page.update()

ft.app(target=main) 