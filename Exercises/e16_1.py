import PySimpleGUI as sg

sg.theme("Black")
label1 = sg.Text("Enter feet: ")
label2 = sg.Text("Enter inches: ")

input1 = sg.Input()
input2 = sg.Input()

convert_button = sg.Button("Convert")


windows = sg.Window("Convertor", layout=[[label1, input1],[label2,input2],[convert_button]])

event, values = windows.read()

windows.close()