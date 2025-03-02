import requests
from flask import Flask, jsonify

app = Flask(__name__)

def fetch_rick_and_morty_data(species="Human", status="Alive", origin="Earth"):
    """
    Fetches characters from the Rick and Morty API based on the given criteria:
    - species (default "Human")
    - status (default "Alive")
    - origin (default "Earth")

    Returns a list of unique characters matching those conditions,
    each containing:
    - name
    - location
    - image
    """
    page = 1
    results = []
    seen_names = set()
    has_next = True

    while has_next:
        url = f"https://rickandmortyapi.com/api/character?page={page}&species={species}&status={status}"
        response = requests.get(url)
        data = response.json()

        # Check if 'results' exists in the data
        if 'results' in data:
            for character in data['results']:
                # Check if the character's origin contains 'Earth' (case-insensitive)
                if origin.lower() in character['origin']['name'].lower():
                    if character['name'] not in seen_names:
                        seen_names.add(character['name'])
                        results.append({
                            "name": character['name'],
                            "location": character['location']['name'],
                            "image": character['image']
                        })

            # If the 'info' dict has 'next', we keep going; otherwise we stop
            if data.get('info') and data['info'].get('next'):
                page += 1
            else:
                has_next = False
        else:
            has_next = False

    return results

@app.route("/healthcheck", methods=["GET"])
def healthcheck():
    """
    Healthcheck endpoint to verify the application is running.
    Returns a JSON with status "ok".
    """
    return jsonify({"status": "ok"}), 200

@app.route("/characters", methods=["GET"])
def get_characters():
    """
    Returns a JSON list of Rick and Morty characters that:
    - are Human
    - are Alive
    - have origin Earth
    """
    data = fetch_rick_and_morty_data()
    return jsonify(data), 200

if __name__ == "__main__":
    # Run the Flask application
    app.run(host="0.0.0.0", port=5000)
