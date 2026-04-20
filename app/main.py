from app.playwright_script import gerar_nota
from app.s3_upload import upload_to_s3

def main():
    file_path = gerar_nota()
    upload_to_s3(file_path)
    print("Nota gerada e enviada para o S3 com sucesso!")

if __name__ == "__main__":
    main()