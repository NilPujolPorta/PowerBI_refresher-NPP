# PowerBI_Refresher-NPP
## Informació
- Per executar el programa s'ha de tenir instalat el python versio 3 o mes.
- Requeriments a requirements.txt.
- El fitxer compilar.bat transforma el .py en .pyc que es mes eficient i rapid.
- Executar amb opcio -h per veure mes opcions i funcionalitats.

## Instal·lació
- Utilitzant `pip`
```
pip install PowerBI-refresher-NPP
```

## Ús
- A la linea de commandes `PowerBI-refresher-NPP [opcions]`
- ```python -m refresher [opcions]```
- ```./synology_API-runner.py [opcions]```
- Executar el fitxer `refresh.py [opcions]`, `refresh.cpython-39.pyc [opcions]` o `./synology_API-runner.py [opcions]`

### Opcions
```
usage: PowerBI-refresher-NPP [-h] [--init-wait NUM_SEC] [--refresh-wait NUM_SEC] [-f RUTA] [-q] [-v]

Serveix per actualitzar localment un document en PowerBI desktop.

optional arguments:
  -h, --help            show this help message and exit
  --init-wait NUM_SEC   temps d'espera d'obertura del PowerBI. Per defecte es 60 segons.
  --refresh-wait NUM_SEC
                        Temps d'espera despres de actualitzar. Per defecte es 60 segons.
  -f RUTA, --file RUTA  Especificar la ruta del fitxer a actualitzar. Per defecte es: ../apis.pbix
  -q, --quiet           Nomes mostra els errors i el missatge de acabada per pantalla.
  -v, --versio          Mostra la versio
```
