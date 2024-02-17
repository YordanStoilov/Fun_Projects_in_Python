import requests
import hashlib


def request_api_data(query_characters):
    url = "https://api.pwnedpasswords.com/range/" + query_characters
    response = requests.get(url)
    if response.status_code != 200:
        raise RuntimeError(f"Error fetching: {response.status_code} -> Check the API and try again")
    return response


def read_response(hashes, hash_to_check):
    hash_lines = hashes.text.splitlines()
    for line in hash_lines:
        hash_value, count = line.split(":")
        if hash_value == hash_to_check:
            return count
    return 0


def pwned_api_check(password):
    sha1_pass = hashlib.sha1(password.encode("utf-8")).hexdigest().upper()
    first_5, tail = sha1_pass[:5], sha1_pass[5:]
    response = request_api_data(first_5)
    response_data = read_response(response, tail)
    if response_data != 0:
        return f"Bad news - your password has been breached {response_data} times!"
    return "Whew! Your password is safe!"


def main():
    while True:
        user_password = input("Let's see if your password is leaked...")
        result = pwned_api_check(user_password)
        print(result)


if __name__ == "__main__":
    main()
