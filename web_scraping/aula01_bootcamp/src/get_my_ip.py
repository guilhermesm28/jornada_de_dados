import requests

url = "http://lumtest.com/myip.json"

# Fazendo a requisição GET
response = requests.get(url)

# Verifica se a requisição foi bem-sucedida (código de status 200)
if response.status_code == 200:
    # Imprime o conteúdo da resposta (o endereço IP retornado pelo site)
    print("ASN: ", response.json()["asn"].get("asnum"))
    print("Organization: ", response.json()["asn"].get("org_name"))
    print("City: ", response.json()["geo"].get("city"))
else:
    # Se a requisição não foi bem-sucedida, imprime o código de status
    print("Falha na requisição. Código de status: ", response.status_code)
