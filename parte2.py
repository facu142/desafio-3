import soporte
import parte1

v = soporte.vector_known_range(300000)
c = [0] * 300000


def contar(vector):
	contador_casillas_no_vacias = 0
	for x in vector:
		c[x] += 1

	for num in c:
		if num != 0:
			contador_casillas_no_vacias += 1
	return contador_casillas_no_vacias


mas_freq, index_mas_freq = parte1.mas_frequente(v)


print('5.', contar(v))
print('6.', mas_freq)
print('7.', index_mas_freq)
