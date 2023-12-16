import PySimpleGUI as sg
from day17fun import convert

label1 = sg.Text("Enter feets: ")
input1 = sg.Input(key="feets")

label2 = sg.Text("Enter inches: ")
input2 = sg.Input(key="inches")

convert_button = sg.Button("Convert")
exit_button = sg.Button("Exit")

output_label = sg.Text("", key="output", text_color="white")

window = sg.Window("File Compressor", layout=[[label1, input1, ],
                                                   [label2, input2, ],
                                                   [convert_button, exit_button, output_label]])

while True:
    event, values = window.read()
    match event:
        case "Exit":
            break
        case sg.WIN_CLOSED:
            break
    print(event, values)
    try:
        feets = float(values['feets'])
        inches = float(values['inches'])
        meters = convert(feets, inches)
        window['output'].update(value=meters)
    except ValueError:
        sg.Popup("Enter values first", font=("Helvetica", 20))


