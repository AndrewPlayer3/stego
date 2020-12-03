import PySimpleGUI as sg
import numpy as np
from encryption import gen_key
from PIL import Image
import os
import io
import stego as st

# ------------------------------------------------------------------
# Set Theme
# ------------------------------------------------------------------
sg.theme('Black')
# ------------------------------------------------------------------

# ------------------------------------------------------------------
# Get the png image that the user wants to encode/decode
# ------------------------------------------------------------------
image = sg.popup_get_file('PNG Image to open', default_path='')
if not image:
    sg.popup_cancel('Cancelling')
    raise SystemExit()
# ------------------------------------------------------------------

# ------------------------------------------------------------------
# Layout 
# ------------------------------------------------------------------
image_elem = sg.Image(image)

layout = [
            [image_elem]
           ,[sg.Text('Enter your keypath: '), sg.InputText()]
           ,[sg.Text('Enter your message: '), sg.InputText()] 
           ,[sg.Text('Channels are 0,1,2 for RGB, and 1,2,3 for RGBA(PNG with Transparency), respectively')]
           ,[sg.Text('Enter desired channel: '), sg.InputText()]
           ,[sg.Button('Encode'), 
             sg.Button('Decode'),
             sg.Button('Gen Key'),
             sg.Button('Open'),
             sg.Button('Close')]
         ]

window = sg.Window('Image Browser', layout, return_keyboard_events=True,
                   location=(0, 0), use_default_focus=False)
# ------------------------------------------------------------------

# ------------------------------------------------------------------
# GUI Loop
# ------------------------------------------------------------------
while True:
    # Reads the Message Form
    event, values = window.read()
    print(event, values)
    # Perform the button operations
    if event == sg.WIN_CLOSED:
        break
    if event == 'Encode':
        if st.encode(values[1], image, values[2], int(values[3])):
            sg.popup("Image Encoded Successfully")
            # Update Image Preview After Encoding
            image_elem.update(image)
        else:
            sg.popup("ERROR: Larger image needed for this message!")
    if event == 'Decode':
        sg.popup(st.decode(values[1], image, int(values[3])))
    if event == 'Gen Key':
        gen_key()
    if event == 'Open':
        image = sg.popup_get_file('PNG Image to open', default_path='')
        image_elem.update(image)
    if event == 'Close':
        break

window.close()
# ------------------------------------------------------------------


