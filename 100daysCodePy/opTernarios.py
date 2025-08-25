#operadores ternarios

esta_chuvendo = False


print("hj estou com as roupas " + ('secas.', 'molhadas.')[esta_chuvendo])
#if
print('hoje estou com as roupas ' + ('molhadas.' if esta_chuvendo else 'secas.'))

# se ler assim: "hoje estou com as roupas molhadas SE esriver estiver chovendo, SENÃO secas"

