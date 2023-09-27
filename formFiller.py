#! python3
# formFiller.py - Automatically fills in the form
import time

import pyautogui as pag

formData = [{'name': 'Alice', 'fear': 'eavesdroppers', 'source': 'wand',
    'robocop': 4, 'comments': 'Tell Bob I said hi.'},
    {'name': 'Bob', 'fear': 'bees', 'source': 'amulet', 'robocop': 4,
    'comments': 'n/a'},
    {'name': 'Carol', 'fear': 'puppets', 'source': 'discount crystal ball',
    'robocop': 1, 'comments': 'Please take the puppets out of the break room.'},
    {'name': 'Alex Murphy', 'fear': 'ED-209', 'source': 'money (e.g. batman)',
    'robocop': 5, 'comments': 'Protect the innocent. Serve the public trust. Uphold the law.'},
    ]

# TODO: Wait until the form page has loaded
pag.PAUSE = 5
print('Ensure that the browser window is active and the form is loaded')
for person in formData:
    # TODO: Give the user a chance to kill the script
    print('>>> 2 second pause to let the user press Ctrl-C <<<')
    time.sleep(2)

    # TODO: Fill out the Name Field
    print(f'Entering {person["name"]} info...')
    pag.write(['\t', '\t', '\t', '\t'], 0.5)
    for i in person['name']:
        pag.write(i,0.1)
    pag.write('\t')

    # TODO: Fill out the Greatest fear field
    for i in person['fear']:
        pag.write(i)
    pag.write(['\t'])

    # TODO: Fill out the Source of Wizard Powers Field
    if person['source'].lower() == 'wand':
        pag.press('enter')
        pag.write(['down', '\n', '\t'], 0.5)
    if person['source'].lower() == 'amulet':
        pag.write(['\n', 'down', 'down', '\n','\t'],0.5)
    if person['source'].lower() == 'discount crystal ball':
        pag.write(['\n', 'down', 'down', 'down', '\n', '\t'], 0.5)
    if person['source'].lower() == 'money (e.g. Batman)':
        pag.write(['\n', 'down', 'down', 'down', 'down', '\n', '\t'],0.5)

    # TODO: Fill out the Robocop Field

    for i in range(person['robocop']-1):
        pag.write(['right'])
    pag.write(['\t', '\t'])

    # TODO: Fill out the additional comments field
    for i in person['comments']:
        pag.write(i,0.1)
    pag.write(['\t'])

    # TODO: Click Submit
    time.sleep(0.5)
    pag.press('enter')

    # TODO: Wait until the form has loaded
    print('Submitted form.')
    time.sleep(5)

    # TODO: Click the submit another response link
    pag.press('tab')
    pag.press('enter')



