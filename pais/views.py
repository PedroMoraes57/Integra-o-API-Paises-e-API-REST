from django.shortcuts import render
import requests
# Create your views here.
def busca_pais(request):
    dados = None
    erro = None
    pais = request.GET.get('pais', 'france')

    url = f'https://restcountries.com/v3.1/name/{pais}'
    try:
        resposta = requests.get(url, timeout=5)
        resposta.raise_for_status() 
        dados = resposta.json()
        if dados:
            dados = dados[0]
        else:
            erro = "País não encontrado."

    except requests.exceptions.RequestException:
        erro = "Erro ao buscar dados do país."

    pais ={
        'capital': dados.get('capital', ['Desconhecido'])[0],
    }
    return render(request, 'pais/dados_pais.html', {
        'dados': dados,
        'erro': erro,
        'pais': pais,
    })
