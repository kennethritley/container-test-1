import requests

for i in range(5):
    print(f'Give me input {i+1}/5: ', end='')
    message = input()
    requests.post('http://server:5001/receive', data=message)
