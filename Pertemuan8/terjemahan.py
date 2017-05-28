import urllib2
from urllib2 import URLError

b = open('id_country.txt','r')
lines = b.readlines()
panjang = len(lines)

for i in range(panjang/3):
	print lines[i].replace('\n', ''),'\t', lines[i + panjang/2].replace('\n', ''), '\t', lines[i + panjang/3].replace('\n', '')
if panjang%2: 
		print lines[-1].replace('\n', '')

while True:
	try:
		bahasa_awal = raw_input("Masukkan kode bahasa awal (ex: id): ")
		bahasa_tujuan = raw_input("Masukkan kode bahasa tujuan (ex: en): ")
		kata = raw_input("Masukkan kata atau kalimat: ")
		url = 'https://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+")) #replace apabila terjadi kalimat
		agent = {'User-Agent':'Mozilla/5.0'}
		cari_hasil ='class="t0">'
		request = urllib2.Request(url, headers=agent)
		page = urllib2.urlopen(request).read()
		result = page[page.find(cari_hasil)+len(cari_hasil):]
		result = result.split("<")[0]
		print "%s -> Diterjemahkan menjadi: " % kata, result

	except URLError, e:
		print "Koneksi jaringan terputus.... Coba lagi !"