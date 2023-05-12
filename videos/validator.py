from validators import url

def titulo_valido(titulo_video):
    return len(titulo_video) > 2

#def descricao_valida(descricao_video):
#    return len(descricao_video) > 1

def url_valida(url_video):
    return url(url_video)

def titulo_categoria_valido(titulo_cor):
    return len(titulo_cor) != 0

def cor_categoria_valido(cor):
    return len(cor) != 0