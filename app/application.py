import base64
import json
import os
import requests


def main():
    target_hostname = os.getenv("TARGET_HOST")
    if target_hostname is None:
        raise ValueError("Missing TARGET_HOST env var!")
    builtwith_token = os.getenv("BUILTWITH_TOKEN")
    if builtwith_token is None:
        raise ValueError("Missing BUILTWITH_TOKEN env var!")
    url = "https://api.builtwith.com/v12/api.json"
    params = {"KEY": builtwith_token, "LOOKUP": target_hostname}
    results = requests.get(url, params=params)
    results_raw = results.json()
    results = json.dumps(results_raw).encode('utf-8', errors='replace')
    encoded = base64.b64encode(results)
    print(encoded)


if __name__ == "__main__":
    main()
