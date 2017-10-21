import xml.etree.ElementTree as et
import sys, os

def dodaj(imie, nazwisko, pesel, dowod, przedmiot, kwota_kupna, kwota_sprzedazy,
          data_zaw, data_kon, telefon):
    path = os.path.dirname(os.path.realpath(__file__))
    path = path.replace("\\", "/")
    tree = et.ElementTree(file='umowy.xml')
    root = tree.getroot()
    nr = int(root.attrib['numer']) + 1
    root.set('numer', str(nr))
    umowa = et.SubElement(root, 'umowa')
    umowa.set('nr', str(nr))
    name = et.SubElement(umowa, 'imie')
    name.text = imie
    surname = et.SubElement(umowa, 'nazwisko')
    surname.text = nazwisko
    pes = et.SubElement(umowa, 'pesel')
    pes.text = pesel
    dow = et.SubElement(umowa, 'dowod')
    dow.text = dowod
    tel = et.SubElement(umowa, 'telefon')
    tel.text = telefon
    prod = et.SubElement(umowa, 'przedmiot')
    prod.text = przedmiot
    kw_kup = et.SubElement(umowa, 'kwota_kupna')
    kw_kup.text = kwota_kupna
    kw_sp = et.SubElement(umowa, 'kwota_sprzedazy')
    kw_sp.text = kwota_sprzedazy
    data_um = et.SubElement(umowa, 'data_zawarcia')
    data_um.text = data_zaw
    data_konc = et.SubElement(umowa, 'data_koncowa')
    data_konc.text = data_kon
    tree = et.ElementTree(root)
    tree.write('umowy.xml')
    return str(nr)

def klient(pesel):
    path = os.path.dirname(os.path.realpath(__file__))
    path = path.replace("\\", "/")
    tree = et.ElementTree(file='umowy.xml')
    root = tree.getroot()
    dane = []
    subtree =''
    umowy = root.getchildren()
    for umowa in umowy:
        umowa_child = umowa.getchildren()
        for u_child in umowa_child:
            if u_child.tag == 'pesel' and u_child.text == pesel:
                subtree = umowa_child
                break
        if len(subtree) > 0:
            break
    for element in subtree:
        dane.append(element.text)

    return dane[:5]

def umowy(ps):
    path = os.path.dirname(os.path.realpath(__file__))
    path = path.replace("\\", "/")
    tree = et.ElementTree(file='umowy.xml')
    root = tree.getroot()
    dane = []
    l = []
    subtree = ''
    umowy = root.getchildren()
    for umowa in umowy:
        umowa_child = umowa.getchildren()
        for u_child in umowa_child:
            if u_child.tag == 'pesel' and u_child.text == ps:
                dane.append(umowa.attrib)
                subtree = umowa_child
                for el in subtree:
                    if el.tag == 'przedmiot' or el.tag == 'data_zawarcia' or el.tag == 'data_koncowa':
                        dane.append(el.text)
                    
    return dane

def zmien_numer(nowy, stary):
    path = os.path.dirname(os.path.realpath(__file__))
    path = path.replace("\\", "/")
    tree = et.ElementTree(file='umowy.xml')
    root = tree.getroot()
    for tel in root.iter('telefon'):
        if tel.text == stary:
            tel.text = nowy

    tree = et.ElementTree(root)
    tree.write(path + '/umowy.xml')
    print(tree)
