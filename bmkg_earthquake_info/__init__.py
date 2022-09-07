"""
BMKG Earthquake Info Package
"""
import requests
from bs4 import BeautifulSoup


def data_extraction():
    """
    Tanggal: 06 September 2022,
    Waktu: 09:31:23 WIB
    Magnitudo: 4.2
    Kedalaman: 10 km
    Lokasi: LS=2.67  BT=118.48
    Pusat Gempa: Pusat gempa berada di laut 45 km Barat Mamuju
    Dirasakan: Dirasakan (Skala MMI): II - III Mamuju
    Selengkapnya →
    """

    try:
        content = requests.get('https://bmkg.go.id')
    except Exception:
        return none

    if content.status_code == 200:
    #    print(content.text)
#       soup = BeautifulSoup(content)
#       print(soup.prettify())


        hasil = dict()
        hasil['date'] = '06 September 2022'
        hasil['time'] = '09:31:23 WIB'
        hasil['magnitudo'] = '4.2'
        hasil['location'] = {'ls': 2.67, 'bt': 118.48}
        hasil['central'] = 'Central of earthquake was in 45 KM Sea of west mamuju'

        return hasil
    else:
        return none


def data_show(result):
    if result is None:
        print("Can not find data from BMKG")
        return

    print('\nThe last Earthquake from BMKG')
    print(f"Date : {result['date']}")
    print(f"Time : {result['time']}")
    print(f"Magnitudo : {result['magnitudo']}")
    print(f"Location : LS: {result['location']['ls']} , BT: {result['location']['bt']}")
    print(f"Central : {result['central']}")



