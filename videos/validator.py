from validators import url

def titulo_valido(titulo_video):
    return len(titulo_video) > 2

def descricao_valida(descricao_video):
    return len(descricao_video) > 1

def url_valida(url_video):
    return url(url_video)
