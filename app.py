from flask import Flask, jsonify
import requests

app = Flask(__name__)

def fetch_characters_filtered(species="human", status="Alive", origin="Earth"):
    base_url = "https://rickandmortyapi.com/api/character"
    all_characters = []
    page = 1

    while True:
        response = requests.get(base_url, params={"page": page, "species": species, "status": status, "origin": origin})
        if response.status_code != 200:
            break

        data = response.json()

        for character in data.get("results", []):
            # Only append if origin contains "Earth"
            if "Earth" in character["origin"]["name"]:
                all_characters.append({
                    "name": character["name"],
                    "location": character["location"]["name"],
                    "image": character["image"]
                })

        # Check if there's a next page
        if data["info"]["next"] is None:
            break
        page += 1

    return all_characters

@app.route("/healthcheck", methods=["GET"])
def healthcheck():
    return jsonify({"status": "OK"}), 200

@app.route("/characters", methods=["GET"])
def get_characters():
    characters_data = fetch_characters_filtered()
    return jsonify(characters_data), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
