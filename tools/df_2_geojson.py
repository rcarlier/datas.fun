import os
import json
import pandas as pd


def dataframe_to_geojson(df, lat="latitude", lng="longitude", columns=None, output=None):
    """
    df = dataframe, all columns became properties (except if columns is full)
    columns = list of columns to put in properties

    lat = nom de la colonne latitude
    lng = nom de la colonne longitude
    output = si différent de None, un fichier est sauvegardé
    """
    features = []
    for _, row in df.iterrows():
        if columns is None:
            properties = {col: row[col] if pd.notnull(
                row[col]) else None for col in df.columns}
        else:
            properties = {col: row[col] if pd.notnull(
                row[col]) else None for col in columns}

        feature = {
            'type': 'Feature',
            'geometry': {
                'type': 'Point',
                'coordinates': [row[lng], row[lat]]
            },
            'properties': properties
        }
        features.append(feature)
    geojson = {
        'type': 'FeatureCollection',
        'features': features
    }
    if output is not None:
        with open(output, 'w') as f:
            json.dump(geojson, f, indent=4)

    return geojson


if __name__ == "__main__":
    cur_path = os.path.dirname(os.path.realpath(__file__))

    csv_file = os.path.join(cur_path, 'test.csv')
    geo1 = os.path.join(cur_path, 'test1.geojson')
    geo2 = os.path.join(cur_path, 'test2.geojson')

    try:
        df = pd.read_csv(csv_file)
        geo = dataframe_to_geojson(
            df,
            lat="lat", lng="lng",
            output=geo1
        )
        geo = dataframe_to_geojson(
            df,
            lat="lat", lng="lng",
            columns=["nom", "adresse"],
            output=geo2
        )

    except:
        print("File doesn't exists ?")
