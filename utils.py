import requests

def load_data_from_url(url: str) -> dict:
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Use local CSS
def local_css(file_name: str):
    with open(file_name) as file:
        return f'<style>{file.read()}</style>'