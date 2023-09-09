import requests

def get_ip():
    ip = requests.get('https://api.ipify.org').text
    print('Votre IP est: ' + ip)

get_ip()
