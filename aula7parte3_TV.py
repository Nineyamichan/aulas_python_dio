class Television:
    def __init__(self) -> object:
        self.ligada = False
        self.canal = 5

    def power (self):
        if self.ligada == True:
            self.ligada = False
        else:
            self.ligada = True

    def aumenta_canal(self):
        if self.ligada:
           self.canal+=1


    def diminui_canal(self):
        if self.ligada:
         self.canal-=1

# -- Definir como main
if __name__ == '__main__':
    television = Television()
    print('A sua tv está ligada: {}'.format(television.ligada))
    television.power()
    print('A sua tv está ligada: {}'.format(television.ligada))
    television.power()
    print('A sua tv está ligada: {}'.format(television.ligada))
    print('Canal: {}'.format(television.canal))
    television.power()
    print('A sua tv está ligada: {}'.format(television.ligada))
    television.aumenta_canal()
    television.aumenta_canal()
    print('Canal:{}'.format(television.canal))
    television.diminui_canal()
    print('Canal: {}'.format(television.canal))