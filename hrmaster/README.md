# hrmaster

A script célja tömbösítve rögzíteni a munkavégzés helyét a céges hrmaster rendszerben.

## Felépítése

A repository a következőket tartalmazza:
- hrmaster.py - python script, amely a hrmaster REST végpontok meghívását végzi a megfelelő paraméterekkel
- config.yaml - a script bemenő paramétereit tárolja
- Dockerfile - docker image file, amely a python script futtatására alkalmas környezetet állítja elő, majd futtatja a scriptet

## Futtatás

A futtatás szoftveres előfeltételként csak telepített Docker-re van szükség.

1. Konfigurációk beállítása:
   - config.yaml fájlban találhatóak
   - access_token: a hrmaster-ben belépés után bármely REST hívásból kinyerhető az Authorization fejléc értéke, ezt kell itt megadni (a "Bearer " utáni részt)
   - end_date: mely dátumig bezárólag végezze el a program a munkavégzés helyének rögzítését
   - officedays: az itt megjelölt napok lesznek minden héten a "bejárós" napok, a többi pedig az otthoni
2. Docker image létrehozása: a /hrmaster mappában állva adjuk ki a következő parancsot: `docker build . -t hrmaster`
3. Docker container indítása: a /hrmaster mappában állva adjuk ki a következő parancsot: `docker run hrmaster`
