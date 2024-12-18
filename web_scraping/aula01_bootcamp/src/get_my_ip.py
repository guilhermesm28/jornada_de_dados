import requests

url = "http://lumtest.com/myip.json"

# Fazendo a requisição GET
response = requests.get(url)

# Verifica se a requisição foi bem-sucedida (código de status 200)
if response.status_code == 200:
    print(f'ASN: {response.json()["asn"].get("asnum")}')
    print(f'Organization: {response.json()["asn"].get("org_name")}')
    print(f'City: {response.json()["geo"].get("city")}')
    print(
        f'State: {response.json()["geo"].get("region_name")}-{response.json()["geo"].get("region")}'
    )
else:
    # Se a requisição não foi bem-sucedida, imprime o código de status
    print("Falha na requisição. Código de status: ", response.status_code)
