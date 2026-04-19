from playwright.sync_api import sync_playwright
from config.settings import USER, PASSWORD, CLIENT_ID, SERVICE_VALUE
import os

def gerar_nota():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(accept_downloads=True)
        page = context.new_page()

        page.goto("https://www.nfse.gov.br/EmissorNacional/DPS/Simplificada")

        # login
        page.fill('input[name="Inscricao"]', USER)
        page.fill('input[name="Senha"]', PASSWORD)
        page.click('button[type="submit"]')

        page.wait_for_timeout(3000)

        # preencher dados
        page.fill('input[name="InscricaoCliente"]', CLIENT_ID)

        # clicar no botão de pesquisa
        page.click('#btn_InscricaoCliente_pesquisar')
        page.wait_for_timeout(3000)

        # abrir o dropdown e selecionar o serviço
        page.click('#IdServicoFavorito_chosen')
        page.wait_for_selector('#IdServicoFavorito_chosen .chosen-results li')
        page.click('.chosen-results li:has-text("Emissão NFS")')

        # preencher valor do serviço
        page.fill('input[name="ValorServico"]', SERVICE_VALUE)

        # page.click('button:has-text("Emitir")')
        page.click('button[type="submit"]')
        page.wait_for_timeout(5000)

        # espera sucesso
        page.wait_for_selector('.alert-success')

        print("Baixando nota...")

        # download
        with page.expect_download() as download_info:
            page.click('#btnDownloadDANFSE')

        download = download_info.value

        os.makedirs("notas", exist_ok=True)
        file_path = os.path.join("notas", download.suggested_filename)
        download.save_as(file_path)

        print(f"Nota salva em: {file_path}")

        browser.close()

        return file_path