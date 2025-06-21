"""Calculos de Fisica Elemental"""

def calor(masa, calor_especifico, temperatura_final, temperatura_inicial):
    """
    Calcula el calor transferido a un cuerpo.
    
    :param masa: Masa del cuerpo en kg
    :param calor_especifico: Calor especifico del material en J/(kg*K)
    :param temperatura_final: Temperatura final en K
    :param temperatura_inicial: Temperatura inicial en K

    :return: Calor transferido en Joules
    """
    return calor_especifico * masa* (temperatura_final - temperatura_inicial)

