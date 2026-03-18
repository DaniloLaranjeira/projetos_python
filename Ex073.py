times = ('Flamengo', 'Palmeiras', 'Cruzeiro', 'Mirassol', 'Fluminense',
         'Botafogo','Bahia', 'São Paulo', 'Grêmio', 'RB Bragantino',
         'Atlético-MG', 'Santos', 'Corinthians', 'Vasco', 'Vitória',
         'Internacional', 'Ceará', 'Fortaleza', 'Juventude', 'Sport')
print(end='\n')
print(f'Lista de times: {times}', end='\n')

print(f'Os 5 primeiros times são: {times[0:5]}', end='\n')

print(f'Os 4 últimos times são: {times[16:]}', end='\n')

print(f'Times em ordem alfabética: {sorted(times)}', end='\n')

print(f'O Santos está na {times.index('Santos')+1} posição', end='\n')