import requests


def http_post(url, headers, payload):
    try:
        response = requests.post(url, data=payload, headers=headers)
    except requests.RequestException:
        raise Exception("POST Exception")

    if response.ok:
        return response

    raise Exception(f"Post method error {response.status_code}: {response.reason}")


def http_get(url, headers):
    try:
        response = requests.post(url, headers=headers)
    except requests.RequestException:
        raise Exception("GET Exception")

    if response.ok:
        return response

    raise Exception(f"Get method error {response.status_code}: {response.reason}")