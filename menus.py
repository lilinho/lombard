from tkinter import *
import os
from tkinter import messagebox as ms
import xmlparse
import flags as f
import datetime

datazaw = ''
datakon = ''


def zmien(nowy, stary):
    xmlparse.zmien_numer(nowy, stary)
def klient_szczegoly(pesel):
    try:
        dane_osobowe = xmlparse.klient(pesel)
        um = xmlparse.umowy(pesel)
        klient_szcz = Tk()
        f.window_list.append(klient_szcz)
        klient_szcz.title("Klient " + dane_osobowe[0] + " " + dane_osobowe[1])
        klient_szcz.geometry("{}x{}".format(400, 400))
        klient_szcz.resizable(height=False, width=False)
        klient_szcz.grid_rowconfigure(0, weight=1)
        klient_szcz.grid_rowconfigure(6, weight=1)
        klient_szcz.grid_rowconfigure(8, weight=1)
        klient_szcz.grid_columnconfigure(1, weight=1)
        klient_szcz.grid_columnconfigure(3, weight=1)
        klient_szcz.grid_columnconfigure(5, weight=1)
        imie_1 = Label(klient_szcz, text="Imię: ")
        imie_2 = Label(klient_szcz, text=dane_osobowe[0])
        nazwisko_1 = Label(klient_szcz, text="Nazwisko: ")
        nazwisko_2 = Label(klient_szcz, text=dane_osobowe[1])
        pesel_l_1 = Label(klient_szcz, text="PESEL: ")
        pesel_l_2 = Label(klient_szcz, text=dane_osobowe[2])
        dow_label_1 = Label(klient_szcz, text="Seria i numer dowodu: ")
        dow_label_2 = Label(klient_szcz, text=dane_osobowe[3])
        tel_label = Label(klient_szcz, text="Telefon: ")
        tel_text = Entry(klient_szcz, width=11)
        zmien_telefon = Button(klient_szcz, text="Zmien numer telefonu", width=22, command=lambda: zmien(tel_text.get(), dane_osobowe[4]))
        umowy_fr = Frame(klient_szcz)
        scroll_y = Scrollbar(umowy_fr)
        scroll_x = Scrollbar(umowy_fr, orient=HORIZONTAL)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.pack(side=BOTTOM, fill=X)
        umowy_lista = Listbox(umowy_fr, yscrollcommand=scroll_y.set, xscrollcommand=scroll_x.set, width=300)
        i = 0
        while i < len(um):
            details = "Umowa nr: " + um[i]['nr'].zfill(4)
            details += ", towar: " + um[i+1]
            details += " (Z dnia: " + um[i+2] + " do " + um[i+3] + ")"
            umowy_lista.insert(END, details)
            i = i+4
        umowy_lista.pack(side=LEFT, fill=BOTH)
        scroll_y.config(command=umowy_lista.yview)
        scroll_x.config(command=umowy_lista.xview)
        imie_1.grid(row=1, column=1, sticky="E")
        imie_2.grid(row=1, column=2, sticky="W")
        nazwisko_1.grid(row=2, column=1, sticky="E")
        nazwisko_2.grid(row=2, column=2, sticky="W")
        pesel_l_1.grid(row=3, column=1, sticky="E")
        pesel_l_2.grid(row=3, column=2, sticky="W")
        dow_label_1.grid(row=4, column=1, sticky="E")
        dow_label_2.grid(row=4, column=2, sticky="W")
        tel_label.grid(row=5, column=1, sticky="E")
        tel_text.grid(row=5, column=2)
        tel_text.insert(0, dane_osobowe[4])
        zmien_telefon.grid(row=5, column=4)
        umowy_fr.grid(column=1, row=7, columnspan=5)
        klient_szcz.mainloop()
    except Exception as e:
        print(e)
        ms.showwarning("Błąd", "Nie ma takiego numeru PESEL")
        return
    
def otworz(numer):
    if len(numer) > 0:
        try:
            os.system('start write C:/Users/' + os.getlogin() + '/Desktop/Umowy/' + numer + '.rtf')
            
        except:
            ms.showwarning("Błąd", "Nie znaleziono umowy")
def pomoc():
    os.system('start write Pomoc.rtf')
def znajdz_klienta():
    klient = Tk()
    f.window_list.append(klient)
    klient.title("Znajdź klienta")
    klient.geometry("{}x{}".format(300, 200))
    klient.resizable(width=False, height=False)
    klient.grid_rowconfigure(0, weight=1)
    klient.grid_rowconfigure(2, weight=1)
    klient.grid_rowconfigure(4, weight=1)
    klient.grid_columnconfigure(0, weight=1)
    klient.grid_columnconfigure(4, weight=1)
    pesel_label = Label(klient, text="Wpisz PESEL")
    pesel_text = Entry(klient, width=15)
    open_b = Button(klient, text="Otwórz", command=lambda: klient_szczegoly(pesel_text.get()), width=10, height=2, borderwidth=6)
    pesel_label.grid(column=1, row=1, sticky="E")
    pesel_text.grid(column=2, row=1, sticky="W")
    open_b.grid(column=2, row=3, sticky="W", columnspan=2)
    pesel_text.bind("<Return>", lambda x: klient_szczegoly(pesel_text.get()))
    klient.mainloop()
def kalkulator():
    def is_int(i):
        try:
            int(i)
            return True
        except ValueError:
            return False


    def sdz_zaw(i, S, d):
        if d == '1':
            if is_int(S):
                if i == '1':
                    mzaw.focus_set()
                return True
            else:
                return False
        else:
            return True
    def sm_zaw(i, S, d):
        if d == '1':
            if is_int(S):
                if i == '1':
                    rzaw.focus_set()
                return True
            else:
                return False
        else:
            return True


    def sr_zaw(i, S, d):
        if d == '1':
            if is_int(S):
                if i == '3':
                    dzkon.focus_set()
                return True
            else:
                return False
        else:
            return True


    def sdz_kon(i, S, d):
        if d == '1':
            if is_int(S):
                if i == '1':
                    mkon.focus_set()
                return True
            else:
                return False
        else:
            return True


    def sm_kon(i, S, d):
        if d == '1':
            if is_int(S):
                if i == '1':
                    rkon.focus_set()
                return True
            else:
                return False
        else:
            return True


    def sr_kon(i, S, V, d):
        if V == 'key':
            if d == '1':
                if is_int(S):
                    if i == '3':
                        kwotakupno_text.focus_set()
                    return True
                else:
                    return False
            else:
                return True
        elif V == 'focusout':
            if len(procent_text.get()) > 0:
                if sprawdz_daty():
                    return True
                else:
                    return False
            else:
                return True
        else:
            return True


    def obl_kwote(kwota, proc):
        proc = proc / 100
        delta = datakon - datazaw

        delta = delta.days
        kwotak = kwota
        for i in range(int(delta)):
            kwotak += kwotak * proc
        return round(kwotak, 2)


    def val_procent(S):
        if is_int(S) or S == '.' or S == ',':
            return True
        else:
            return False
            
    def calculate():
        if sprawdz_daty():
            procent = procent_text.get()
            procent = procent.replace(",", ".")
            procent = float(procent)
            kwotasprzedaz_text.insert(0, str(obl_kwote(float(kwotakupno_text.get()), procent)))

    def spr_kwota(S):
        if is_int(S):
            return True
        elif S == '.' or S == ',':
            if '.' in kwotakupno_text.get() or ',' in kwotakupno_text.get():
                return False
            else:
                return True
        else:
            return False


    def sprawdz_daty():
        if len(dzzaw.get()) == 0 or \
                        len(mzaw.get()) == 0 or \
                        len(rzaw.get()) == 0 or \
                        len(dzkon.get()) == 0 or \
                        len(mkon.get()) == 0 or \
                        len(rkon.get()) == 0:
            ms.showwarning("Błąd", "Uzupelnij wszystkie pola")
            return False
        data_zaw = []
        data_zak = []
        global datazaw
        global datakon
        if dzzaw.get()[0] == '0':
            data_zaw.append(int(dzzaw.get()[1]))
        else:
            data_zaw.append(int(dzzaw.get()))

        if mzaw.get()[0] == '0':
            data_zaw.append(int(mzaw.get()[1]))
        else:
            data_zaw.append(int(mzaw.get()))

        data_zaw.append(rzaw.get())
        if dzkon.get()[0] == '0':
            data_zak.append(int(dzkon.get()[1]))
        else:
            data_zak.append(int(dzkon.get()))

        if mkon.get()[0] == '0':
            data_zak.append(int(mkon.get()[1]))
        else:
            data_zak.append(int(mkon.get()))

        data_zak.append(rkon.get())
        try:
            datazaw = datetime.date(int(data_zaw[2]), int(data_zaw[1]), int(data_zaw[0]))
        except ValueError:
            ms.showwarning("Błąd", "Niedozwolona data")
            dzzaw.delete(0, END)
            mzaw.delete(0, END)
            rzaw.delete(0, END)
            dzzaw.focus_set()
            return False
        try:
            datakon = datetime.date(int(data_zak[2]), int(data_zak[1]), int(data_zak[0]))

            if datazaw > datakon:
                ms.showwarning("Błąd", "Niedozwolona data: data zawarcia jest późniejsza niż data zakończenia")
                dzkon.delete(0, END)
                mkon.delete(0, END)
                rkon.delete(0, END)
                dzkon.focus_set()
                return False
        except ValueError:
            ms.showwarning("Błąd", "Niedozwolona data")
            dzkon.delete(0, END)
            mkon.delete(0, END)
            rkon.delete(0, END)
            dzkon.focus_set()
            return False
        return True
    calc = Tk()
    f.window_list.append(calc)
    calc.title("Kalkulator odsetek")
    calc.geometry("{}x{}".format(300, 200))
    calc.resizable(width=False, height=False)
    calc.grid_rowconfigure(0, weight=1)
    calc.grid_rowconfigure(5, weight=1)
    calc.grid_rowconfigure(9, weight=1)
    calc.grid_rowconfigure(13, weight=1)
    calc.grid_rowconfigure(15, weight=1)
    calc.grid_columnconfigure(0, weight=1)
    calc.grid_columnconfigure(6, weight=1)
    skok_dzien_zaw = (calc.register(sdz_zaw), '%i', '%S', '%d')
    skok_miesiac_zaw = (calc.register(sm_zaw), '%i', '%S', '%d')
    skok_rok_zaw = (calc.register(sr_zaw), '%i', '%S', '%d')
    skok_dzien_kon = (calc.register(sdz_kon), '%i', '%S', '%d')
    skok_miesiac_kon = (calc.register(sm_kon), '%i', '%S', '%d')
    skok_rok_kon = (calc.register(sr_kon), '%i', '%S', '%V', '%d')
    val_kwota = (calc.register(spr_kwota), '%S')
    val_proc = (calc.register(val_procent), '%S')
    
    datazaw_label = Label(calc, text="Data zawarcia umowy (DD/MM/RRRR)")
    datakon_label = Label(calc, text="Data końca umowy (DD/MM/RRRR)")
    kwotakupno_label = Label(calc, text="Kwota zastawu")
    procent_label = Label(calc, text="Procent")
    kwotasprzedaz_label = Label(calc, text="Kwota pożyczki")
    kwotakupno_text = Entry(calc, width=7, validate='all', validatecommand=val_kwota)
    procent_text = Entry(calc, width=5, validate='all', validatecommand=val_proc)
    kwotasprzedaz_text = Entry(calc, width=7)
    dzzaw = Entry(calc, width=3, validate='all', validatecommand=skok_dzien_zaw)
    mzaw = Entry(calc, width=3, validate='all', validatecommand=skok_miesiac_zaw)
    rzaw = Entry(calc, width=5, validate='all', validatecommand=skok_rok_zaw)
    dzkon = Entry(calc, width=3, validate='all', validatecommand=skok_dzien_kon)
    mkon = Entry(calc, width=3, validate='all', validatecommand=skok_miesiac_kon)
    rkon = Entry(calc, width=5, validate='all', validatecommand=skok_rok_kon)
    dash1 = Label(calc, text="/")
    dash2 = Label(calc, text="/")
    dash3 = Label(calc, text="/")
    dash4 = Label(calc, text="/")
    oblicz_button = Button(calc, text="Oblicz", width=10, command=calculate)
    datazaw_label.grid(column=1, row=1, sticky="W", columnspan=5)
    dzzaw.grid(column=1, row=2)
    dash1.grid(column=2, row=2)
    mzaw.grid(column=3, row=2)
    dash2.grid(column=4, row=2)
    rzaw.grid(column=5, row=2)
    datakon_label.grid(column=1, row=3, sticky="W", columnspan=5)
    dzkon.grid(column=1, row=4)
    dash3.grid(column=2, row=4)
    mkon.grid(column=3, row=4)
    dash4.grid(column=4, row=4)
    rkon.grid(column=5, row=4)

    kwotakupno_label.grid(column=1, row=6, sticky="W", columnspan=3)
    kwotakupno_text.grid(column=4, row=6, sticky="W", columnspan=2)
    procent_label.grid(column=1, row=7, sticky="W", columnspan=3)
    procent_text.grid(column=4, row=7, sticky="W", columnspan=2)
    kwotasprzedaz_label.grid(column=1, row=12, sticky="W", columnspan=3)
    kwotasprzedaz_text.grid(column=4, row=12, sticky="W", columnspan=2)
    oblicz_button.grid(column=1, row=13, sticky="W", columnspan=3)
def otworz_umowe():
    umowa = Tk()
    f.window_list.append(umowa)
    umowa.title("Otwórz umowę")
    umowa.geometry("{}x{}".format(300, 200))
    umowa.resizable(width=False, height=False)
    umowa.grid_rowconfigure(0, weight=1)
    umowa.grid_rowconfigure(2, weight=1)
    umowa.grid_rowconfigure(4, weight=1)
    umowa.grid_columnconfigure(0, weight=1)
    umowa.grid_columnconfigure(4, weight=1)
    numer_label = Label(umowa, text="Wpisz numer umowy (czterocyfrowy)")
    numer_text = Entry(umowa, width=5)
    open_b = Button(umowa, text="Otwórz", command=lambda: otworz(numer_text.get()), width=10, height=2, borderwidth=6)
    numer_label.grid(column=1, row=1, sticky="E")
    numer_text.grid(column=2, row=1, sticky="W")
    open_b.grid(column=2, row=3, sticky="W", columnspan=2)
    numer_text.bind("<Return>", lambda x: otworz(numer_text.get()))
    umowa.mainloop()
def about():
    howto = Tk()
    f.window_list.append(howto)
    howto.title("Licencja/O programie...")
    howto.geometry("{}x{}".format(300, 250))
    howto.resizable(width=False, height=False)
    how_label = Label(howto, text="\n Program został stworzony i przeznaczony"
                                  "\n do użytku przez"
                                  "\n WPISAĆ DANE"
                                  "\n przez: Tomasz Pawelec (c)2017"
                                  "\n Zabrania się udostępniania programu"
                                  "\n osobom trzecim")
    how_label.pack()
    howto.mainloop()
