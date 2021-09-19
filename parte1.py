import soporte


def mas_frequente(list):
	contador = {}
	max_cont = 0
	max_numero = None

	for i in list:
		if i not in contador:
			contador[i] = 1
		else:
			contador[i] += 1

		if contador[i] > max_cont:
			max_cont = contador[i]
			max_numero = i

	return max_numero, max_cont


def principal():
	v = soporte.vector_unknown_range(300000)

	v_coincidentes = []

	for numero in v:
		if not numero in v_coincidentes:
			v_coincidentes.append(numero)

	print('1. ', len(v_coincidentes))
	print('2.', mas_frequente(v)[0])
	print('3.', mas_frequente(v)[1])


if __name__ == '__main__':
	principal()
