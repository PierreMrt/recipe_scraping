import PySimpleGUI as sg

from sqlite import execute_read_query
from scraper import update_all


def create_window():
    layout = [
        [sg.Button('Mettre à jour'), sg.Text(text='', key='TextUpdate')],
        [sg.InputText(), sg.Button('Recherche', pad=(0, 60), size=(20, 3)), sg.Button('Liste a-Z', size=(10, 3))],
        [sg.Radio('Toutes recettes', 'RandomChoice', default=True), sg.Radio('Faciles', 'RandomChoice'), sg.Radio('Rapides', 'RandomChoice')],
        [sg.Button('Au hasard', size=50)]
    ]

    return sg.Window('Window Title', layout, margins=(60, 60))

def run(window, conn):
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED: # if user closes window or clicks cancel
            break

        elif event == 'Mettre à jour':
           window.find_element('TextUpdate').update(value="Les recettes sont en train d'être mise à jour..")
           update_all(conn)

        elif event == 'Liste a-Z':
            print(list_az(conn))

        elif event == 'Recherche':
            print(f'recherche: {values[0]}')
        
        elif event == 'Au hasard':
            print(values[1], values[2], values[3])

        else:
            print(event)
        # print('You entered ', values[0])

    window.close()



def list_az(conn):
    q = "SELECT name from recipes"
    return execute_read_query(conn, q)


if __name__ == '__main__':
    window = create_window()
    run(window)