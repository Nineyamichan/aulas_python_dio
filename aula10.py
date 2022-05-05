# --- data atual
from datetime import date, time, datetime, timedelta
#https://docs.python.org/pt-br/3/library/datetime.html -diretizes

def trabalhando_com_datetime():
    data_atual = datetime.now()
    print(data_atual)
    print(data_atual.strftime(('%d/%m/%Y %H:%M:%S')))
    print(data_atual.strftime(('%c')))
    print(data_atual.day)
    print(data_atual.year)
    print(data_atual.weekday())
    tupla = ('segunda', 'terça', 'quarta', 'quinta', 'sexta', 'sabado', 'domingo')
    print(tupla[data_atual.weekday()])
    data_criada = datetime(2022,5,20,15,30,20)
    print(data_criada)
    print(data_criada.strftime('%c'))

    # -- converter string para datetime
    data_string = '01/01/2022'
    data_convert = datetime.strptime(data_string, '%d/%m/%Y')
    print(data_convert)
    print(type(data_convert))
    nova_data = data_convert - timedelta(days=365)
    print(nova_data)



def trabalhando_com_date():
    data_atual = date.today()
    data_atual_srt = data_atual.strftime('%d/%m/%Y')
    print(data_atual_srt)
    print(type(data_atual_srt))

def trabalhando_com_time():
    horario = time(hour=15, minute=18,second=30)
    print(horario)
    horario_str = horario.strftime('%H:%M:%S')
    print(horario_str)
    print(type(horario_str))

if __name__ == '__main__':
    #trabalhando_com_time()
    trabalhando_com_datetime()

