import requests

from requests.exceptions import HTTPError

try:
    url = "http://localhost:8080/random?bound=5&origin=1&size=100"

    response = requests.get(url)

    json = response.json()

    randnums = json['numArray']
    sum = 0
    for num in randnums:
        print(num)
        sum += num
    print("Sum of Numbers = ", sum)

except HTTPError as err:
    print(f'Http Error occured: {err}')
