import json

def feature_is_interesting(props):
    if props["Status"] == "ACTIVE":
        if props["Facility"] != None:
            if props["Facility"] in ["NG", "ESR", "TRL"]:
                return True
            if "BL" in props["Facility"]:
                return True
    return False

def get_features(original):
    filtered = []
    for feature in original:
        props = feature["properties"]
        if feature_is_interesting(props):
            filtered.append(
                { 
                    "type": "Feature", 
                    "properties": { 
                        "OBJECTID": props["OBJECTID"],
                        "SegmentName": props["SegmentName"],
                        "Facility": props["Facility"],
                    },
                    "geometry": feature["geometry"]
                }
            )
    return filtered

with open('Bicycle_Network.geojson') as f:
    original = json.load(f)

filtered = {}
filtered["type"] = original["type"]
filtered["name"] = original["name"]
filtered["crs"] = original["crs"]
filtered["features"] = get_features(original["features"])

with open('Bicycle_Network_Filtered.geojson', 'w') as f:
    json.dump(filtered, f)