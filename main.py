import requests

def check_url_status(url):
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            return True, response.status_code
        else:
            return False, response.status_code
    except requests.exceptions.RequestException as e:
      
        return False, str(e)

def scan_urls(file_path):
    with open(file_path, 'r') as file:
        urls = file.readlines()

    results = {}
    for url in urls:
        url = url.strip()
        if url:
            is_valid, status = check_url_status(url)
            results[url] = {'valid': is_valid, 'status': status}
            status_text = f"OK ({status})" if is_valid else f"Broken ({status})"
            print(f"{url}: {status_text}")

    return results

file_path = 'urls.txt'
scan_urls(file_path)
