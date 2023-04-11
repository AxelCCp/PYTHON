def compruebaEmail(mailUsuario):

    """
    Evalua un email recibido en busca del @. Si tiene un @ es correcto. Si tiene mas de un @ es incorrecto. Si el @ está al final es incorrecto.

    >>> compruebaEmail('juan@cursos.es')
    True

    >>> compruebaEmail('juancursos.es@')
    False

    >>> compruebaEmail('juancursos.es')
    False

    >>> compruebaEmail('juan@cursos@.es')
    False

    """
    arroba = mailUsuario.count('@')
    if(arroba != 1 or mailUsuario.rfind('@')==(len(mailUsuario)-1) or mailUsuario.find('@')==0):
        return False
    else:
        return True

import doctest
doctest.testmod()