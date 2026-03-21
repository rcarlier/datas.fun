# ROME : Répertoire Opérationnel des Métiers et des Emplois

Source:

- https://www.data.gouv.fr/datasets/repertoire-operationnel-des-metiers-et-des-emplois-rome
- Numero de version : 60
- Date de publication : 18/09/2025
- Date de validation : 27/08/2025
- Titre/commentaire : ROME 4.0 version 60 - 25M09
- Récupération le 21/03/2026

## conversion en UTF8 (pour mémoire)

```py
import os
import glob
import chardet
for filepath in glob.glob("json/*"):
    with open(filepath, "rb") as f:
        raw = f.read()
        detected = chardet.detect(raw)
        encoding = detected["encoding"]

    if encoding and encoding.lower() != "utf-8":
        text = raw.decode(encoding)
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(text)
```
