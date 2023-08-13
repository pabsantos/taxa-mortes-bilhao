import requests

url_frota_combustivel = [
    "https://www.gov.br/transportes/pt-br/assuntos/transito/arquivos-senatran/estatisticas/renavam/2013/junho/3quantidadeveiculosufmunicipiocombustivel_jun_2013.zip",
    "https://www.gov.br/transportes/pt-br/assuntos/transito/arquivos-senatran/estatisticas/renavam/2014/junho/3_frotaporufmunicipiocombustivel_jun2014.xlsx",
    "https://www.gov.br/transportes/pt-br/assuntos/transito/arquivos-senatran/estatisticas/renavam/2015/junho/3_frota_por_uf_municipio_combustivel_jun_2015.rar",
    "https://www.gov.br/transportes/pt-br/assuntos/transito/arquivos-senatran/estatisticas/renavam/2016/junho/3_frota_por_uf_municipio_combustivel_jun_2016.rar",
    "https://www.gov.br/transportes/pt-br/assuntos/transito/arquivos-senatran/estatisticas/renavam/2017/junho/3_-_combustivel_-_junho_-_2017.xlsx",
    "https://www.gov.br/transportes/pt-br/assuntos/transito/arquivos-senatran/estatisticas/renavam/2018/junho/d_frota_por_uf_municipio_combustivel_jun_2018.xlsx",
    "https://www.gov.br/transportes/pt-br/assuntos/transito/arquivos-senatran/estatisticas/renavam/2019/junho/d_frota_por_uf_municipio_combustivel_junho_2019.xlsx",
    "https://www.gov.br/transportes/pt-br/assuntos/transito/arquivos-senatran/estatisticas/renavam/2020/junho/d_frota_por_uf_municipio_combustivel_junho_2020.xlsx"
]

SAVE_PATH = "data-raw/"

def create_file_name(url, ano):
    extension_name = url.split(".")[-1]
    file_name = f"frota_combustivel_{str(ano)}.{extension_name}"
    return file_name

def create_list_names():
    names_list = []
    for url, ano in zip(url_frota_combustivel, range(2013, 2021, 1)):
        names_list.append(create_file_name(url, ano))
    return(names_list)

def download_frota(url, file_name):
    response = requests.get(url)

    if response.status_code == 200:
        with open(SAVE_PATH + file_name, 'wb') as file:
            file.write(response.content)

        print(f"File '{file_name}' downloaded successfully.")
    else:
        print('Failed to download the file. Status code:', response.status_code)

def download_files():
    for url, file_name in zip(url_frota_combustivel, create_list_names()):
        download_frota(url, file_name)

download_files()
