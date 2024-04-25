# MongoDB-Docker-Python-Manager

Activitat amb MongoDB.
<br>
Descripció breu del projecte:

Funcionament del Programa
-------------------------

El programa utilitza MongoDB per realitzar operacions sobre la base de dades especificada. Aquí està com funciona:

-   En executar el programa, aquest carrega la configuració de la base de dades des de l'arxiu `.env`.
-   Utilitza aquestes configuracions per connectar-se amb MongoDB a través de la classe `MongoActions`, que gestiona totes les operacions relacionades amb la base de dades.
-   Pots modificar l'arxiu `main.py` per personalitzar les accions o ampliar la funcionalitat del programa segons sigui necessari.


## Clonació del Repositori

Per obtenir una còpia del projecte a la teva màquina local per al desenvolupament i proves, segueix aquests passos:

1. Obre el teu terminal.
2. Canvia el directori de treball actual a la ubicació on vols clonar el repositori.
3. Escriu el següent comandament i prem `Enter` per crear una còpia local del repositori:

   ```bash
   git clone https://github.com/usuari/nom-del-repositori.git
   ```
Configuració de l'Entorn
------------------------

Abans d'executar el programa, necessites configurar les variables d'entorn:

1.  Al directori del projecte, trobaràs un arxiu anomenat `.env_example`.

2.  Canvia el nom d'aquest arxiu a `.env`:

    ```bash
    mv .env_example .env
    ```
    -   Obre l'arxiu `.env` amb un editor de textos i omple els valors adequats (realment nomes caldra posar la ruta a la bbdd de mongo):

1.  `CONNECTION_STRING=la_teva_cadena_de_connexió_a_mongodb`
    <br>
    `DATABASE_NAME=restaurants (per defecte)`
    <br>
    `COLLECTION_NAME=rest (per defecte)`

    Aquests valors són essencials perquè el programa es connecti correctament a la teva base de dades MongoDB.

### Configuració de MongoDB

Abans de començar a usar el programa, assegura't de configurar la teva base de dades MongoDB:

-   Crea una base de dades anomenada `restaurants`.
-   Dins de la base de dades `restaurants`, crea una col-lecció anomenada `rest`.
-   Importa el fitxer `restaurants.json` a la col-lecció `rest` utilitzant una eina com MongoDB Compass o mitjançant una línia de comandament mongoimport.

Execució del Programa
---------------------

Per executar el programa, assegura't d'estar al directori del projecte i després executa:

```bash
python main.py
```
Això iniciarà el procés definit a `main.py`, que farà ús de les configuracions de `MongoActions` per interactuar amb MongoDB.
