graph = {'Bandung' : ['Alun-alun Cimahi'],
			'Alun-alun Cimahi' : ['Jl. Kolonel Masturi', 'Jl.H.Gofur'],
			'Jl.H.Gofur' : ['Padalarang', 'Alun-alun Cimahi','Pakuhaji','Cilame'],
			'Padalarang' : ['Jl.H.Gofur','Cilame','Ngamprah'],
			'Cilame' : ['Ngamprah','Pakuhaji','Jl.H.Gofur','Padalarang'],
			'Ngamprah' : ['Pakuhaji','Cilame','Padalarang'],
			'Pakuhaji' : ['Ngamprah','Cisarua','Jl.H.Gofur','Jl.Cipageran'],
			'Jl.Cipageran' : ['Pakuhaji','Jl.Kolonel Masturi'],
			'Jl.Kolonel Masturi' : ['Cisarua','Cipageran','Jl.Encep Kartawiria','Alun-alun Cimahi'],
			'Jl.Encep Kartawiria' : ['Jl.Kolonel Masturi'],
			'Cisarua' : ['Pakuhaji','Jl.Kolonel Masturi']
			}

def jalur_terpendek(graph, awal, tujuan, jalur=[]):
	jalur = jalur + [awal]
	if awal == tujuan:
		return jalur
	if not graph.has_key(awal):
		return None
	jalurpendek = None
	for node in graph[awal]:
		if node not in jalur:
			newjalur = jalur_terpendek(graph, node, tujuan, jalur)
			if newjalur:
				if not jalurpendek or len(newjalur) < len(jalurpendek):
					jalurpendek = newjalur
	return jalurpendek
print("Jalur Jalan Kabupaten Bandung Barat-Kota Cimahi")
print("(Alun-alun Cimahi,Jl.H.Gofur,Padalarang,Cilame,Ngamprah)")
print("(Pakuhaji,Jl.Cipageran,Jl.Kolonel Masturi, Jl.Encep Kartawiria)")
print("\n")
awal = raw_input("Masukan titik awal : ")
tujuan = raw_input("Masukan titik tujuan : ")
hasil = jalur_terpendek(graph, awal, tujuan, jalur=[])
print "Jalur Terpendek yang dapat dilalui", hasil