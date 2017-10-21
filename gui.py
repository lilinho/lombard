from tkinter import *
from tkinter import messagebox as ms
import re
import xmlparse
import generatertf
import datetime
import menus as m
import flags as f

def calculate_percent(kwota):
    if int(kwota) <= 130:
        return 0.03
    elif int(kwota) <= 260:
        return 0.04
    elif int(kwota) <= 390:
        return 0.05
    elif int(kwota) <= 520:
        return 0.06
    elif int(kwota) <= 650:
        return 0.07
    elif int(kwota) <= 780:
        return 0.08
    else:
        return 0.09

if __name__ == '__main__':
    datazaw = ''
    datakon = ''
    miesiace = {'01': 31, '02': 29, '03': 31, '04': 30, '05': 31, '06': 30,
                '07': 31, '08': 31, '09': 30, '10': 31, '11': 30, '12': 31}

    main_window = Tk()
    def close():
        for win in f.window_list:
            try:
                win.destroy()
            except: 
                pass
        main_window.destroy()
    main_window.title("Generator umów")
    main_window.geometry("{}x{}".format(640, 480))
    main_window.grid_columnconfigure(0, weight=1)
    main_window.grid_columnconfigure(6, weight=1)
    main_window.grid_columnconfigure(3, weight=1)
    main_window.grid_rowconfigure(0, weight=1)
    main_window.grid_rowconfigure(3, weight=1)
    main_window.grid_rowconfigure(6, weight=1)
    main_window.grid_rowconfigure(14, weight=1)
    main_window.grid_rowconfigure(16, weight=1)
    main_window.protocol("WM_DELETE_WINDOW", close)

    def is_int(i):
        try:
            int(i)
            return True
        except ValueError:
            return False


    def is_float(i):
        try:
            float(i)
            return True
        except ValueError:
            return False


    def sprawdz_pesel(W):
        if len(pesel_text.get()) > 0:
            if len(pesel_text.get()) < 10:
                ms.showwarning("Błąd", "Za krótki pesel")
                pesel_text.focus()
                main_window.bell()
                return False
            if not re.search("\d{11}", pesel_text.get()):
                ms.showwarning("Błąd", "Niedozwolone znaki")
                pesel_text.focus()
                main_window.bell()
                return False
            val = (9 * int(pesel_text.get()[0]) + 7 * int(pesel_text.get()[1]) + 3 * int(pesel_text.get()[2]) +
                   1 * int(pesel_text.get()[3]) + 9 * int(pesel_text.get()[4]) + 7 * int(pesel_text.get()[5]) +
                   3 * int(pesel_text.get()[6]) + 1 * int(pesel_text.get()[7]) + 9 * int(pesel_text.get()[8]) +
                   7 * int(pesel_text.get()[9]))
            val = val % 10
            if not val == int(pesel_text.get()[10]):
                ms.showwarning("Błąd", "Cyfra kontrolna niezgodna")
                pesel_text.focus()
                main_window.bell()
                return False
            return True


    def sprawdz_dowod(W):
        if len(dowod_text.get()) > 0:
            if len(dowod_text.get()) < 9:
                ms.showwarning("Błąd", "Za krótka wartość")
                main_window.bell()
                dowod_text.focus()
                return False
            if not re.search("[A-Z]{3}\d{6}", dowod_text.get().upper()):
                ms.showwarning("Błąd", "Zły format")
                dowod_text.focus()
                main_window.bell()
                return False

        return True


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
        if is_int(S):
            return True
        elif S == '.' or S == ',':
          if '.' in procent_text.get() or ',' in procent_text.get():
              return False
          else:
              return True
        else:
            return False

    def calculate():
        if sprawdz_daty():
            procent = procent_text.get()
            procent = procent.replace(",", ".")
            procent = float(procent)
            kwotasprzedaz_text.delete(0, END)
            kwotasprzedaz_text.insert(0, str(obl_kwote(float(kwotakupno_text.get()), procent)))

    def spr_kwota(S, V):
        if V == 'key':
            if is_int(S):
                return True
            elif S == '.' or S == ',':
                if '.' in kwotakupno_text.get() or ',' in kwotakupno_text.get():
                    return False
                else:
                    return True
            else:
                return False
        elif V == 'focusout':
            procent_text.insert(0, str(calculate_percent(kwotakupno_text.get())))
            return True
        else:
            return True
                            

    def val_telefon(S, V):
        if V == 'key':
            if is_int(S):
                return True
            elif S == '-':
                return True
            else:
                return False
        elif V == 'focusout':
            if len(telefon_text.get()) > 0:
                if not re.search("\d{3}-\d{3}-\d{3}", telefon_text.get()):
                    ms.showwarning("Zły format", "Zły format telefonu. Oczekiwano XXX-XXX-XXX")
                    telefon_text.focus_set()
                    return False
        else:
            return True
    def porownaj_z_dzisiejsza(data):

        dzisiaj = datetime.date.today()
        if dzisiaj == data:
            return True
        else:
            odp = ms.askyesno("Zła data", "Wprowadzona data różni się od aktualnej. Zachować?")
            if odp is True:
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
            main_window.bell()
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

            if not porownaj_z_dzisiejsza(datazaw):
                main_window.bell()
                dzzaw.delete(0, END)
                mzaw.delete(0, END)
                rzaw.delete(0, END)
                dzzaw.focus_set()
                return False
        except ValueError:
            ms.showwarning("Błąd", "Niedozwolona data")
            main_window.bell()
            dzzaw.delete(0, END)
            mzaw.delete(0, END)
            rzaw.delete(0, END)
            dzzaw.focus_set()
            return False
        try:
            datakon = datetime.date(int(data_zak[2]), int(data_zak[1]), int(data_zak[0]))

            if datazaw > datakon:
                ms.showwarning("Błąd", "Niedozwolona data: data zawarcia jest późniejsza niż data zakończenia")
                main_window.bell()
                dzkon.delete(0, END)
                mkon.delete(0, END)
                rkon.delete(0, END)
                dzkon.focus_set()
                return False
        except ValueError:
            ms.showwarning("Błąd", "Niedozwolona data")
            main_window.bell()
            dzkon.delete(0, END)
            mkon.delete(0, END)
            rkon.delete(0, END)
            dzkon.focus_set()
            return False
        return True


    def validate_all():
        if len(imie_text.get()) == 0 or \
                        len(nazwisko_text.get()) == 0 or \
                        len(pesel_text.get()) == 0 or \
                        len(dowod_text.get()) == 0 or \
                        len(przedmiot_text.get('0.0', END)) == 0 or \
                        len(kwotasprzedaz_text.get()) == 0 or \
                        len(kwotakupno_text.get()) == 0 or \
                        len(procent_text.get()) == 0:
            ms.showwarning("Błąd", "Uzupelnij wszystkie pola")
            main_window.bell()
            return False

        return True


    def generate():
        if validate_all() and sprawdz_daty():
            dataz = dzzaw.get() + "-" + mzaw.get() + "-" + rzaw.get()
            datak = dzkon.get() + "-" + mkon.get() + "-" + rkon.get()
			
            numer = xmlparse.dodaj(imie_text.get().upper(), nazwisko_text.get().upper(),
                           pesel_text.get(), dowod_text.get().upper(),
                           przedmiot_text.get('0.0', 'end-1c').upper(), kwotakupno_text.get(),
                           kwotasprzedaz_text.get(), dataz, datak, telefon_text.get())
            generatertf.generuj(imie_text.get().upper(), nazwisko_text.get().upper(),
                           pesel_text.get(), dowod_text.get().upper(),
                           przedmiot_text.get('0.0', 'end-1c').upper(), kwotakupno_text.get(),
                           kwotasprzedaz_text.get(), dataz, datak, numer)
            imie_text.delete(0, END)
            nazwisko_text.delete(0, END)
            pesel_text.delete(0, END)
            dowod_text.delete(0, END)
            przedmiot_text.delete('0.0', END)
            kwotakupno_text.delete(0, END)
            kwotasprzedaz_text.delete(0, END)
            dzzaw.delete(0, END)
            mzaw.delete(0, END)
            rzaw.delete(0, END)
            dzkon.delete(0, END)
            mkon.delete(0, END)
            rkon.delete(0, END)
            procent_text.delete(0, END)
            telefon_text.delete(0, END)


    val_pesel = (main_window.register(sprawdz_pesel), '%W')
    val_dowod = (main_window.register(sprawdz_dowod), '%W')
    skok_dzien_zaw = (main_window.register(sdz_zaw), '%i', '%S', '%d')
    skok_miesiac_zaw = (main_window.register(sm_zaw), '%i', '%S', '%d')
    skok_rok_zaw = (main_window.register(sr_zaw), '%i', '%S', '%d')
    skok_dzien_kon = (main_window.register(sdz_kon), '%i', '%S', '%d')
    skok_miesiac_kon = (main_window.register(sm_kon), '%i', '%S', '%d')
    skok_rok_kon = (main_window.register(sr_kon), '%i', '%S', '%V', '%d')
    val_kwota = (main_window.register(spr_kwota), '%S', '%V')
    val_proc = (main_window.register(val_procent), '%S')
    val_phone = (main_window.register(val_telefon), '%S', '%V')
    daty_frame = Frame(main_window)
    menu_frame = Frame(main_window)

    top_menu = Menu(main_window)
    main_window.config(menu=top_menu)
    options_menu = Menu(top_menu, tearoff=0)
    help_menu = Menu(top_menu, tearoff=0)

    top_menu.add_cascade(label="Opcje", menu=options_menu)
    top_menu.add_cascade(label="Pomoc", menu=help_menu)

    options_menu.add_cascade(label="Znajdź klienta", \
                                command=m.znajdz_klienta)
    options_menu.add_cascade(label="Kalkulator odsetek", \
                                command=m.kalkulator)
    options_menu.add_cascade(label="Otwórz umowę", \
                                command=m.otworz_umowe)

    help_menu.add_cascade(label="Pomoc", command=m.pomoc)
    help_menu.add_cascade(label="Licencja/O programie", \
                                command=m.about)

    imie_label = Label(main_window, text="Imię")
    nazwisko_label = Label(main_window, text="Nazwisko")
    pesel_label = Label(main_window, text="PESEL")
    dowod_label = Label(main_window, text="Seria i nr dowodu")
    telefon_label = Label(main_window, text="Numer telefonu")
    przedmiot_label = Label(main_window, text="Nazwa przedmiotu")
    datazaw_label = Label(daty_frame, text="Data zawarcia umowy (DD/MM/RRRR)")
    datakon_label = Label(daty_frame, text="Data końca umowy (DD/MM/RRRR)")
    kwotakupno_label = Label(main_window, text="Kwota zastawu")
    procent_label = Label(main_window, text="Procent")
    kwotasprzedaz_label = Label(main_window, text="Kwota pożyczki")
    imie_text = Entry(main_window, width=25)
    nazwisko_text = Entry(main_window, width=25)
    pesel_text = Entry(main_window, width=11, validate='focusout', validatecommand=val_pesel)
    dowod_text = Entry(main_window, width=11, validate='focusout', validatecommand=val_dowod)
    telefon_text = Entry(main_window, width=11, validate='all', validatecommand=val_phone)
    przedmiot_text = Text(main_window, height=2, width=25)
    dzzaw = Entry(daty_frame, width=3, validate='all', validatecommand=skok_dzien_zaw)
    mzaw = Entry(daty_frame, width=3, validate='all', validatecommand=skok_miesiac_zaw)
    rzaw = Entry(daty_frame, width=5, validate='all', validatecommand=skok_rok_zaw)
    dzkon = Entry(daty_frame, width=3, validate='all', validatecommand=skok_dzien_kon)
    mkon = Entry(daty_frame, width=3, validate='all', validatecommand=skok_miesiac_kon)
    rkon = Entry(daty_frame, width=5, validate='all', validatecommand=skok_rok_kon)
    dash1 = Label(daty_frame, text="/")
    dash2 = Label(daty_frame, text="/")
    dash3 = Label(daty_frame, text="/")
    dash4 = Label(daty_frame, text="/")
    kwotakupno_text = Entry(main_window, width=7, validate='all', validatecommand=val_kwota)
    procent_text = Entry(main_window, width=5)
    kwotasprzedaz_text = Entry(main_window, width=7)
    oblicz_button = Button(main_window, text="Oblicz", width=10, height=1, borderwidth=3, command=calculate)
    generuj_button = Button(main_window, text="Generuj", width=10, height=3, borderwidth=6, command=generate)
    menu_frame.grid(column=1, row=0)
    imie_label.grid(column=1, row=1, sticky="W")
    imie_text.grid(column=1, row=2, sticky="W", columnspan=2)
    nazwisko_label.grid(column=1, row=4, sticky="W")
    nazwisko_text.grid(column=1, row=5, sticky="W", columnspan=2)
    pesel_label.grid(column=1, row=7, sticky="E")
    pesel_text.grid(column=2, row=7, sticky="W")
    dowod_label.grid(column=1, row=9, sticky="W")
    dowod_text.grid(column=2, row=9, sticky="W")
    telefon_label.grid(column=1, row=10, sticky="W")
    telefon_text.grid(column=2, row=10, sticky="W")
    przedmiot_label.grid(column=4, row=1, sticky="W", columnspan=2)
    przedmiot_text.grid(column=4, row=2, sticky="WN", columnspan=2, rowspan=2)
    daty_frame.grid(column=4, row=4, columnspan=2, rowspan=4)

    datazaw_label.grid(column=0, row=0, sticky="W", columnspan=5)
    dzzaw.grid(column=0, row=1)
    dash1.grid(column=1, row=1)
    mzaw.grid(column=2, row=1)
    dash2.grid(column=3, row=1)
    rzaw.grid(column=4, row=1)
    datakon_label.grid(column=0, row=2, sticky="W", columnspan=5)
    dzkon.grid(column=0, row=3)
    dash3.grid(column=1, row=3)
    mkon.grid(column=2, row=3)
    dash4.grid(column=3, row=3)
    rkon.grid(column=4, row=3)

    kwotakupno_label.grid(column=4, row=10, sticky="W")
    kwotakupno_text.grid(column=5, row=10, sticky="W")
    procent_label.grid(column=4, row=11, sticky="W")
    procent_text.grid(column=5, row=11, sticky="W")
    kwotasprzedaz_label.grid(column=4, row=12, sticky="W")
    kwotasprzedaz_text.grid(column=5, row=12, sticky="W")
    oblicz_button.grid(column=5, row=13, sticky="W")
    generuj_button.grid(column=5, row=15, sticky="E")

    main_window.mainloop()
