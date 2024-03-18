'''
`NI-DMM` (Python module: nidmm)
[readthedocs.io](https://nidmm.readthedocs.io/en/latest/nidmm.html)

INCOMPLETE:
    - En caso de error hay que devolver un false
    - Hay que cerrar session con self.session.close
    - Al usar range=-1 lo configuramos en AUTO
    - Hay que buscar las opciones de NULL
    - Añadir espera o indicación al terminar el self test y el self cal

mypyc:
    mypyc INSTRUMENTS/PXI_DMM.py
    import nidmm # type: ignore / ** Hay que incluirla en el pip freeze para importarla
    En el valor -1 para rango auto, estaba re-definiendo la variable, y eso no le gusta a mypyc
    NMB_FUNCTIONS genera error al indicarlo de esa forma en el class, hay que plantearse sacarlo fuera
'''