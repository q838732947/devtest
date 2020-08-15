import requests


def get_token():
    host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=e7uXVRluWOyqA71RkG7g2bQG&client_secret=LwGKgljR9r1wPgVxLC79qWbPaXjtGcUs'
    response = requests.get(host)
    if response:
        print(response.json())
        print(response.json()["refresh_token"])
        return response.json()["refresh_token"]


def main():
    token = get_token()
    url = f"https://aip.baidubce.com/rest/2.0/ocr/v1/general_basic?access_token={token}"
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    data = {"image": ""}
    r = requests.post(url=url, headers=headers, data=data)
    print(r.text)


if __name__ == '__main__':
    get_token()
