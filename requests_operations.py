import requests
import random
import time
from typing import Tuple

from bs4 import BeautifulSoup

import html_parser as parser

def _validate_string(s: str, from_="") -> Tuple[bool, str]:
    if type(s) is not str:
        return False, f"type({s}) is not str, {type(s)} instead"
    if len(s) == 0:
        return False, f"len({s}) is 0"
    return True, ""

def validate_url(url: str) -> Tuple[bool, str]:
    valid, reason = _validate_string(url, "url")
    if not valid:
        return valid, reason
    if not "tixcraft.com/ticket/" in url:
        return False, "只支援拓元售票系統（https://tixcraft.com/ticket/ 開頭）的頁面"
    if not url.startswith("http") or len(url) < 14:
        return False, "Not done yet."
    try:
        r = requests.head(url)
    except Exception as e:
        return False, e
    return r.status_code in [200, 302], f"{r.status_code}: {r.content}"

def validate_line_token(token: str) -> Tuple[bool, str]:
    valid, reason = _validate_string(token, "url")
    if not valid:
        return valid, reason

    headers = {
        "Authorization": "Bearer " + token,
    }
    r = requests.get("https://notify-api.line.me/api/status", headers=headers)
    return r.status_code == 200, f"{r.status_code}: {r.content}"

def request(url: str, headers: dict = {}) -> BeautifulSoup:
    while True:
        try:
            response = requests.get(url, headers=headers).text
            return BeautifulSoup(response, "html.parser")
        except Exception as e:
            delay = random.randint(2, 5)
            print(f"Requesting {url} failed. Will try in {delay} seconds. ({e})")
            time.sleep(delay)

def send_line_msg(token: str, title:str, msg_body: str, url: str) -> int:
    # https://notify-bot.line.me/my/
    headers = {
        "Authorization": "Bearer " + token,
        "Content-Type" : "application/x-www-form-urlencoded"
    }

    msg = f"\n[餘票監看程式通知] \n\n{title}\n\n"
    msg += f"{msg_body}"
    msg += f"\n網址: {url}"

    payload = {'message': msg }
    r = requests.post("https://notify-api.line.me/api/notify", headers=headers, params=payload)
    return r.status_code

if __name__ == "__main__":
    print(validate_url("https://tixcraft.com/ticket/area/23_tanya/13966"))
    print(validate_url("https://tixcraft.com/ticket/area/23_reneliu/14411"))
