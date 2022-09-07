"""
BMKG Earthquake Info Package
"""
import requests
from bs4 import BeautifulSoup


def data_extraction():

    try:
        content = requests.get('https://bmkg.go.id')
    except Exception:
        return none

    if content.status_code == 200:
        soup = BeautifulSoup(content.text, 'html.parser')
        date_time = soup.find('span', {'class': 'waktu'})
        date_time = date_time.text.split(', ')

        date = date_time[0]  #date_time.text.split(', ')[0]
        time = date_time[1]  # date_time.text.split(', ')[1]

        result = soup.find("div", {'class': "col-md-6 col-xs-6 gempabumi-detail no-padding"})
        result = result.findChildren('li')

        i = 0
        magnitudo = None
        kedalaman = None
        ls = None
        bt = None
        lokasi = None
        dirasakan = None

        for res in result:
            if i == 1:
                magnitudo = res.text
            elif i == 2:
                kedalaman = res.text
            elif i == 3:
                koordinat = koordinat.text.split[' - ']
                koordinat = res.text
                ls = koordinat[0]
                bt = koordinat[1]
            elif i == 4:
                lokasi = res.text
            elif i == 5:
                dirasakan = res.text
            i = i + 1

        hasil = dict()
        hasil['date'] = date                             #'06 September 2022'
        hasil['time'] = time                             #'09:31:23 WIB'
        hasil['magnitudo'] = magnitudo                   #'4.2'
        hasil['kedalaman'] = kedalaman
        hasil['koordinat'] = koordinat
        hasil['lokasi'] = lokasi #{'ls' : 12 , 'bt': 118.48}
        hasil['dirasakan'] = dirasakan

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
    print(f"Kedalaman : {result['kedalaman']}")
    print(f"Location : LS: {result['lokasi']['ls']} , BT: {result['location']['bt']}")
    print(f"Central : {result['central']}")
    print(f"Dirasakan : {result['dirasakan']}")
