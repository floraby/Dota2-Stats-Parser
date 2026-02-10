import requests

# Simple parser for OpenDota API
# Need to register for a private API key later
def get_player_stats(account_id):
    url = f"https://api.opendota.com/api/players/{account_id}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        print(f"Player Name: {data['profile']['personaname']}")
        print(f"Rank Tier: {data['rank_tier']}")
    else:
        print("Failed to fetch data from API")

if __name__ == "__main__":
    # My personal ID for testing
    get_player_stats(12345678)
