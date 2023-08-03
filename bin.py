# Bank Identification Number Lookup
import requests

def get_bin_info(bin_number):
    api_url = f"https://lookup.binlist.net/{bin_number}"
    response = requests.get(api_url)

    if response.status_code == 200:
        bin_info = response.json()
        return bin_info
    else:
        print("Error: Unable to fetch BIN information.")
        return None

if __name__ == "__main__":
    bin_number = input("Enter the BIN number: ")
    bin_info = get_bin_info(bin_number)
    if bin_info:
        print("BIN Information:")
        print(f"Issuer: {bin_info.get('bank', {}).get('name')}")
        print(f"Card Type: {bin_info.get('type')}")
        print(f"Country: {bin_info.get('country', {}).get('name')}")
    else:
        print("BIN not found or invalid.")
