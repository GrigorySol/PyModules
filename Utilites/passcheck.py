import requests
import hashlib


def request_api_data(hash_part: str) -> str:
    url = f"https://api.pwnedpasswords.com/range/{hash_part}"
    data = requests.get(url)
    if data.status_code != 200:
        raise RuntimeError(f"Error fetching: {data.status_code}")
    return data.text


def get_hashes_for_password(password: str) -> (str, str):
    password_hash = hashlib.sha1(password.encode("utf-8")).hexdigest()
    hash_part, hash_remain = password_hash[:5], password_hash[5:]
    hashes = request_api_data(hash_part)
    return hashes, hash_remain


def compare_password_hash(hashes: str, check_hash: str) -> str | int:
    for h, amount in (line.split(":") for line in hashes.splitlines()):
        if h.capitalize() == check_hash.capitalize():
            return amount
    return 0


def check_password(args: list) -> str | int:
    for password in args:
        hashes, check_hash = get_hashes_for_password(password)
        amount = compare_password_hash(hashes, check_hash)
        yield amount


if __name__ == "__main__":
    import sys
    sys.exit(check_password(sys.argv[1:]))
