#### ler horas

horas = int(input("Digite as horas:"))

#### ler minutos

minutos = int(input("Digite os minutos:"))

#### ler segundos

segundos = int(input("Digite os segundos:"))

## converte horas em segundos

horas_em_segundos = horas * 60 * 60

## converte minutos em segundos

minutos_em_segundos = minutos * 60

### soma todos os segundos

total = horas_em_segundos + minutos_em_segundos + segundos

### imprime soma

print(total)
