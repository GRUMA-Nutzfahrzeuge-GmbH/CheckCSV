from Data import Loader, Writer
from tkinter import *


def main():
    window = Tk()
    window.title("Sysconf vergleichen nach Fehlern")

    Label(window, text="Name der Sysconf:", fg="black", font="none 12 bold").grid(row=1, column=0, sticky=W)
    Label(window, text="Name der Whitelist:", fg="black", font="none 12 bold").grid(row=2, column=0, sticky=W)
    Label(window, text="Name der Ausgabedatei:", fg="black", font="none 12 bold").grid(row=3, column=0, sticky=W)

    textentry_dif = Entry(window, width=60)
    textentry_dif.grid(row=1, column=1, sticky=W)
    textentry_dif.focus_set()
    textentry_whitlist = Entry(window, width=60)
    textentry_whitlist.grid(row=2, column=1, sticky=W)
    textentry_finished = Entry(window, width=60)
    textentry_finished.grid(row=3, column=1, sticky=W)
    textentry_error = Entry(window, width=50)
    textentry_error.config(state='readonly')
    textentry_error.grid(row=4, column=1, sticky=W)

    Button(window, text="Vergleichen", width=12,
           command=lambda: compare(textentry_whitlist.get(), textentry_dif.get(),textentry_finished.get(), textentry_error)).grid(row=4, column=0, sticky=W)
    window.bind('<Return>', (lambda event: compare(textentry_whitlist.get(), textentry_dif.get(),textentry_finished.get(), textentry_error)))

    window.mainloop()


def compare(textentry_whitelist, textentry_dif, textentry_finished, error):

    # Check if at the end is a csv
    if str(textentry_whitelist[-4:]) != '.csv':
        whitelist_path = textentry_whitelist + ".csv"
        dif_path = textentry_dif + ".csv"
    else:
        whitelist_path = textentry_whitelist
        dif_path = textentry_dif
    try:
        # generates the list to compare whitelist | sysconf_list
        whitelist = Loader.load_whitlist(whitelist_path)
        dif_list = Loader.load_dif(dif_path)
        wrong_list = []
        # compares the two different lists
        for data_dif in dif_list:
            for data_white in whitelist:
                counter = 0
                for index in range(0, 3):
                    if str(data_white[index]) == str(data_dif[index]):
                        counter = counter + 1

                if counter == 3:
                    break
            # all three parts of the key have to be identical
            if counter != 3:
                wrong_list.append(data_dif)
        # writes the wrong parts in an csv file
        Writer.write_csv(wrong_list, textentry_finished)
    except Exception as e:
        # writes the error message in the text box
        error.config(state='normal')
        error.insert(0, e)
        error.config(state='readonly')


if __name__ == '__main__':
    main()

