from flask import Flask, jsonify, send_from_directory, request
import requests
import math

app = Flask(__name__, static_url_path='', static_folder='static')

PARKS_URL = "https://gis.burnaby.ca/arcgis/rest/services/OpenData/OpenData1/MapServer/6/query"

facilities = []


def assign_tags(name):
    name = (name or "").lower()
    tags = []

    if "dog" in name:
        tags.append("dog-friendly")
    if "play" in name:
        tags.append("playground")
    if "trail" in name or "ravine" in name:
        tags.append("nature")
    if "lake" in name or "water" in name:
        tags.append("water")

    return tags


# get center point from polygon
def get_center(geometry):
    try:
        ring = geometry["rings"][0]

        xs = [point[0] for point in ring]
        ys = [point[1] for point in ring]

        return sum(ys) / len(ys), sum(xs) / len(xs)

    except:
        return None, None


def load_data():
    global facilities

    params = {
    "where": "1=1",					
    "outFields": "*",
    "returnGeometry": "true",
    "outSR": 4326,
    "f": "json"
    }

    r = requests.get(PARKS_URL, params=params)
    data = r.json()						

    facilities = []

    for rec in data.get("features", []):

        attrs = rec["attributes"]
        geom = rec.get("geometry", {})

        lat, lon = get_center(geom)

        facilities.append({
            "id": attrs.get("OBJECTID"),
            "name": attrs.get("NAME") or attrs.get("PARK_NAME") or "Unnamed Park",
            "lat": lat,
            "lon": lon,
            "neighbourhood": "",
            "tags": assign_tags(
                attrs.get("NAME") or attrs.get("PARK_NAME")
            )
        })

    print("LOADED:", len(facilities))


def distance(lat1, lon1, lat2, lon2):
    R = 6371

    dLat = math.radians(lat2-lat1)
    dLon = math.radians(lon2-lon1)

    a = (
        math.sin(dLat/2)**2 +
        math.cos(math.radians(lat1)) *
        math.cos(math.radians(lat2)) *
        math.sin(dLon/2)**2
    )

    return R * 2 * math.atan2(
        math.sqrt(a),
        math.sqrt(1-a)
    )


@app.route("/api/facilities")
def get_facilities():

    q = request.args.get("q", "").lower()
    tag = request.args.get("tag", "").lower()

    results = facilities

    if q:
        results = [
            f for f in results
            if q in f["name"].lower()
        ]

    if tag:
        results = [
            f for f in results
            if tag in f["tags"]
        ]

    return jsonify(results)


@app.route("/")
def index():
    return send_from_directory("static", "index.html")


if __name__ == "__main__":
    load_data()
    app.run(host="0.0.0.0", port=5000)