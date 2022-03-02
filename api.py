import json
from urllib import request

url = "https://al-quran-8d642.firebaseio.com/data.json?print=pretty"

# lakukan http request
response = request.urlopen(url)

# parsing data json
data = json.loads(response.read())

# gunakan perulangan untuk menampilkan data
print ('Assalamualaikum wr.wb, berikut adalah daftar arti nama surat dalam alquran')

nomor = int(input('awkaowkwaokwa '))
i = nomor
print(f"{i}. {data[i-1]['nama']} ({data[i-1]['asma']}) memiliki arti {data[i-1]['arti']}")
print (f"Memiliki banyak ayat : {data[i-1]['ayat']}")
print (f"{data[i-1]['keterangan']}")

print("ngikngok")