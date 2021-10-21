import sys
import requests

hits = []

def main(argv):
    URL = str(argv[1])
    wordList = open(str(argv[2]), "r")
    for wline in wordList:
        stat = request((URL + wline))
        match stat:
            case 200:
                succy = str(URL + wline).strip()
                print(f'{succy.strip()} - {stat}')
                hits.append(succy.strip())

            case _:
                print(f'{stat}')
    ll = len(hits)
    print(f'''
Status Page''')
    for i in range(0, int(ll)):
        print(f'''
{stat}    {hits[i]}''')

def request(URL):
    r = requests.get(URL.strip())
    status = r.status_code
    return status

main(sys.argv)