import PySimpleGUI as sg


def create_window():
    layout = [
        [sg.Button('Mettre à jour'), sg.Button('Liste a-Z')],
        [sg.InputText(), sg.Button('Recherche', pad=(0, 60), size=(20, 3))],
        [sg.Radio('Toutes recettes', 'RandomChoice', default=True), sg.Radio('Faciles', 'RandomChoice'), sg.Radio('Rapides', 'RandomChoice')],
        [sg.Button('Au hasard')]
    ]

    return sg.Window('Window Title', layout, margins=(60, 60))

def run(window):
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED: # if user closes window or clicks cancel
            break

        elif event == 'Mettre à jour':
            print('Mise a jour en cours')

        elif event == 'Liste a-Z':
            print('Liste de toutes les recettes')

        elif event == 'Recherche':
            print(values[0])
        
        elif event == 'Au hasard':
            print(values[1], values[2], values[3])

        else:
            print(event)
        # print('You entered ', values[0])

    window.close()

if __name__ == '__main__':
    window = create_window()
    run(window)