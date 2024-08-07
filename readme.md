# datas.fun

## Quelques données à garder sous la main...

### France

#### Communes

-   `France/communes.json`
-   `France/communes.csv`

Sources

-   COG Code officiel géographique : [INSEE - 20/02/2024](https://www.insee.fr/fr/information/7766585)
-   Base du comparateur de territoires [INSEE - 27/06/2024](https://www.insee.fr/fr/statistiques/2521169)
-   Base officielle des codes postaux [data.gouv.fr - 01/08/2024 ](https://www.data.gouv.fr/fr/datasets/base-officielle-des-codes-postaux/)

Extrait

```json
{
    "insee_com":"92035",
    "insee_reg":"11",
    "insee_dep":"92",
    "commune":"Garenne-Colombes",
    "commune_article":"La Garenne-Colombes",
    "code_postal":"92250",
    "commune_type":"COM",
    "insee_parente":null,
    "lat":48.90713,
    "lng":2.24366,
    "superficie_km2":1.78,
    "population_2021":29932,
    "population_2015":29682,
    "menages_2021":13936,
    "naissances_2022":394,
    "deces_2022":169,
    "pop_15_64_totale_2021":20448,
    "pop_15_64_chomage_2021":1282,
    "pop_15_64_active_2021":16841
},
```

#### Départements

-   `France/departements.json`
-   `France/departements.csv`

Sources

-   COG Code officiel géographique : [INSEE - 20/02/2024](https://www.insee.fr/fr/information/7766585)
-   Quel est le centre géographique des 96 départements métropolitains [IGN - 07/07/2022](https://www.ign.fr/reperes/centre-geographique-des-departements-metropolitains)

Extrait

```json
{
    "insee_dep":"92",
    "insee_reg":"11",
    "departement":"Hauts-de-Seine",
    "departement_article":"Hauts-de-Seine",
    "lng":2.24583,
    "lat":48.84722,
    "aire":175,
    "lambda":"2\u00b014'45\" E",
    "phi":"48\u00b050'50\"",
    "insee_com_cheflieu":"92050",
    "insee_com_centre":"92100"
},
```

#### Régions

-   `France/regions.json`
-   `France/regions.csv`

Sources

-   COG Code officiel géographique : [INSEE - 20/02/2024](https://www.insee.fr/fr/information/7766585)
-   Quel est le centre géographique des 13 régions métropolitaines [IGN - 25/10/2021](https://www.ign.fr/reperes/centre-geographique-des-regions-metropolitaines)

Extrait

```json
{
    "insee_reg":"11",
    "region":"\u00cele-de-France",
    "region_article":"\u00cele-de-France",
    "lng":2.50472,
    "lat":48.70917,
    "aire":12068,
    "lambda":"2\u00b030'17\"",
    "phi":"48\u00b042'33\"",
    "insee_reg_cheflieu":"75056",
    "commune_centre":"Brunoy (Essonne)"
},
```

## Quelques fonctions à garder sous la main...

### Python

-   `tools/convert.py` diverses fonctions de conversions (dms_to_decimal, decimal_to_dms, coords_to_dms, lat_to_phi, lng_to_lambda)
-   `tools/df_2_geojson.py` convertir un dataframe en geojson
