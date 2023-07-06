import PySimpleGUI as sg
 # Define the layout of the GUI
layout = [
    [sg.Column([[sg.Text('Ship name:', size=(20,1))]], element_justification='right'), sg.Column([[sg.Combo([], key='ship_name', enable_events=True, size=(30,1))]])],
    [sg.Column([[sg.Text('Firing angle (10 or 20):', size=(20,1))]], element_justification='right'), sg.Column([[sg.Input(key='firing_angle')]])],
    [sg.Column([[sg.Text('Length of firing angle:', size=(20,1))]], element_justification='right'), sg.Column([[sg.Input(key='length')]])],
    [sg.Column([[sg.Text('Increment:', size=(20,1))]], element_justification='right'), sg.Column([[sg.Input(key='increment')]])],
    [sg.Column([[sg.Text('Target distance:', size=(20,1))]], element_justification='right'), sg.Column([[sg.Input(key='distance')]])],
    [sg.Column([[sg.Text('Approximating angle:', size=(20,1))]], element_justification='right'), sg.Column([[sg.Input(key='approximation')]])],
    [sg.Column([[sg.Button('Calculate Increment'), sg.Button('Calculate Approximation')]], element_justification='right'), sg.Column([[sg.Multiline(key='note_box', size=(20, 5), font=('Helvetica', 12))]])]
]
 # Create the window
window = sg.Window('Angle Calculator', layout, keep_on_top=True)
 # Define the list to store ship names and their corresponding increment values
ship_list = []
 # Define the event loop
while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break
    elif event == 'Calculate Increment':
        try:
            length = float(values['length'])
            angle = float(values['firing_angle'])
            increment = length / angle
            ship_name = values['ship_name']
            if ship_name not in [item[0] for item in ship_list]:
                ship_list.append((ship_name, increment))
                window['ship_name'].update(values=[item[0] for item in ship_list])
            else:
                index = [item[0] for item in ship_list].index(ship_name)
                ship_list[index] = (ship_name, increment)
            window['increment'].update(increment)
        except ValueError:
            sg.popup('Please enter valid numbers for Length and Firing angle')
    elif event == 'Calculate Approximation':
        try:
            distance = float(values['distance'])
            increment = float(values['increment'])
            approximation = distance / increment
            window['approximation'].update(approximation)
        except ValueError:
            sg.popup('Please enter valid numbers for Target distance')
    elif event == 'ship_name':
        ship_name = values['ship_name']
        index = [item[0] for item in ship_list].index(ship_name)
        increment = ship_list[index][1]
        window['increment'].update(increment)
    elif event == 'Calculate':
        try:
            length = float(values['length'])
            angle = float(values['firing_angle'])
            distance = float(values['distance'])
            increment = length / angle
            approximation = distance / increment
            ship_name = values['ship_name']
            if ship_name not in [item[0] for item in ship_list]:
                ship_list.append((ship_name, increment))
                window['ship_name'].update(values=[item[0] for item in ship_list])
            else:
                index = [item[0] for item in ship_list].index(ship_name)
                ship_list[index] = (ship_name, increment)
            window['increment'].update(increment)
            window['approximation'].update(approximation)
        except ValueError:
            sg.popup('Please enter valid numbers for Length, Firing angle, and Target distance',keep_on_top=True)
 # Close the window
window.close()