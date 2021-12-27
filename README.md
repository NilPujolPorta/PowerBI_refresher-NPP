# PowerBI_Refresher-NPP
## Informació
- Per executar el programa s'ha de tenir instalat el python versio 3 o mes.
- Requeriments a requirements.txt.
- El fitxer compilar.bat transforma el .py en .pyc que es mes eficient i rapid.
- Executar amb opcio -h per veure mes opcions i funcionalitats.

## Ús
- Executar el fitxer `synology_API.py` o `synology_API.cpython-39.pyc` amb les opcions adients. Llavors les dades es guardaran a `dadesSynology.json` i si la opcio de excel esta activada tambe es guardara a `revisio_copies_seguretat_synology_vs1.xlsx`

- Opcions
```
usage: refresh.cpython-39.pyc [-h] [--init-wait NUM_SEC] [--refresh-wait NUM_SEC] [-f RUTA] [-q] [-v]

Serveix per actualitzar dashboard de PowerBI desktop localment.

optional arguments:
  -h, --help            show this help message and exit
  --init-wait NUM_SEC   temps d'espera d'obertura del PowerBI. Per defecte es 60 segons.
  --refresh-wait NUM_SEC
                        Temps d'espera despres de actualitzar. Per defecte es 60 segons.
  -f RUTA, --file RUTA  Especificar la ruta del fitxer a actualitzar. Per defecte es: ../apis.pbix
  -q, --quiet           Nomes mostra els errors i el missatge de acabada per pantalla.
  -v, --versio          Mostra la versio
```
