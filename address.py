import requests

def get_address_from_coords(lat, lon, api_key):
    url = f"http://api.positionstack.com/v1/reverse"
    params = {
        "access_key": "c9fdd658115bca840ffa8861a34b6e0d"
,
        "query": f"{6.6778},{3.1654}",
        "limit": 1
    }
    response = requests.get(url, params=params)
    data = response.json()
    
    if "data" in data and len(data["data"]) > 0:
        return data["data"][0].get("label")
    return None

# Example usage
api_key = "YOUR_POSITIONSTACK_API_KEY"
address = get_address_from_coords(6.6778, 3.1654, api_key)
print(address)
