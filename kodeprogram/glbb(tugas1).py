import time
start_time = time.time()

print("Menghitung (besarnya jarak yang ditempuh benda (St) dalam GLBB)")
vo = raw_input("Masukan kecepatan awal benda (Vo) m/detik : ")
t = raw_input("Masukan waktu temput benda(t) detik: ")
a = raw_input("Masukan perlamabatan benda (a) m/detik2: ")
if vo =='sembilan':
	vo=9
if vo =='delapan':
	vo=8
if vo =='tujuh':
	vo=7
if vo =='enam':
	vo=6
if vo =='lima':
	vo=5
if vo =='empat':
	vo=4
if vo == 'tiga':
	vo=3
if vo == 'dua':
	vo=2
if vo == 'satu':
	vo=1
if t =='satu':
	t=1
if t =='dua':
	t=2
if t =='tiga':
	t=3
if t =='empat':
	t=4
if t =='lima':
	t=5
if t =='enam':
	t=6
if t =='tujuh':
	t=7
if t =='delapan':
	t=8
if t =='sembilan':
	t=9
if a =='sembilan':
	a=9
if a =='delapan':
	a=8
if a =='tujuh':
	a=7
if a =='enam':
	a=6
if a =='lima':
	a=5
if a =='empat':
	a=4
if a =='tiga':
	a=3
if a =='dua':
	a=2
if a =='satu':
	a=1
St = (vo * t) - (a * (t*t) / 2) 
print ("Maka jarak yang ditempuh benda (St) ", St)

print("waktu eksekusi : %s detik " % (time.time() - start_time))