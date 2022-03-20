import PySimpleGUI as sg
from main import voce

def main():
    layout = [[(sg.Text('Voice Assistant', size=[80, 1]))],
              [sg.Output(size=(100, 20))],
              [
               sg.Button('START', button_color=(sg.YELLOWS[0], sg.BLUES[0])),
               sg.Button('EXIT', button_color=(sg.YELLOWS[0], sg.GREENS[0]))]]

    window = sg.Window('Your voice assistant', layout, default_element_size=(30, 2))

    # ---===--- Loop taking in user input and using it to query HowDoI web oracle --- #
    while True:
        event, value = window.read()
        if event == 'START':
            voce()
        else:
            break
    window.close()

if __name__ == '__main__':
    main()