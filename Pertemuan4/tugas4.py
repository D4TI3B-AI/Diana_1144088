import sys
print("Langkah dan solusi yang benar adalah dengan urutan 2-4-3-7-1-4-2\n")
print("1.petani dan gabah menyeberang\n 2.Petani dan ayam menyeberang\n 3.Petani dan Harimau menyeberang\n 4.Petani kembali\n 5.Petani dan harimau kembali\n 6.Petani dan gabah kembali\n 7.Petani dan ayam kembali")
def permainan():
	print(' Kondisi Awal\n Pulau kiri : (p,a,g,h) (1,1,1,1)\n Pulau kanan : (p,a,g,h) (0,0,0,0)')
	a = raw_input("Langkah ke-1 : ")
	if a == '2'		: b = raw_input("Pulau kiri : (0,0,1,1)\nPulau kanan : (1,1,0,0)\n Langkah ke-2 : ")
	else 			: print ('Game Over')
	if b == '4'		: c = raw_input("Pulau kiri : (1,0,1,1)\nPulau kanan : (0,1,0,0)\n Langkah ke-3 : ")
	else			: print ('Game Over')
	if c == '3'		: d = raw_input("Pulau kiri : (0,0,1,0)\nPulau kanan : (1,1,0,1)\n Langkah ke-4 : ")
	else			: print ('Game Over')
	if d == '7'		: e = raw_input("Pulau kiri : (1,1,1,0)\nPulau kanan : (0,0,0,1)\n Langkah ke-5 : ")
	else			: print ('Game Over')
	if e == '1'		: f = raw_input("Pulau kiri : (0,1,0,0)\nPulau kanan : (1,0,1,1)\n Langkah ke-6 : ")
	else			: print ('Game Over')
	if f == '4'		: g = raw_input("Pulau kiri : (1,1,0,0)\nPulau kanan : (0,0,1,1)\n Langkah ke-7 : ")
	else			: print ('Game Over')
	if g == '2'		: f = raw_input("Pulau kiri : (0,0,0,0)\nPulau kanan : (1,1,1,1)\n Selamat Anda Berhasil ! \n Kondisi akhir\nPulau kiri : (p,a,g,h) (0,0,0,0)\n Pulau kanan : (p,a,g,h) (1,1,1,1) ")
permainan()