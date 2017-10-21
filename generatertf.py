import sys, os

def generuj(imie, nazwisko, pesel, dowod, przedmiot, kwota_kupna, kwota_sprzedazy,
          data_zaw, data_kon, numer):
    path1 = os.path.dirname(os.path.realpath(__file__))
    path1 = path1.replace("\\", "/")
    numer = numer.zfill(4)
    klient = imie + " " + nazwisko + ", PESEL: " + pesel + ", SERIA I NUMER DOWODU: " + dowod
    path = 'C:/Users/' + os.getlogin() + '/Desktop/Umowy/'
    if not os.path.exists(path):
        os.makedirs(path)
    template = open('umowa_wzor.rtf').read().rstrip('\x00')
    places = {'num': numer,
              'data_1': data_zaw,
              'dane_k': klient,
              'przedmiot': przedmiot,
              'kwota_z': kwota_kupna,
              'data_2': data_kon,
              'kwota_p': kwota_sprzedazy}
    open(path + numer + '.doc', 'a').write(template % places)
    os.system('start write ' + path + numer + '.doc')
