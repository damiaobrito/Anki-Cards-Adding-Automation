import requests
import json

class AnkiNote:
    
    def __init__(self, front, back):
        self.front = front
        self.back = back

class AnkiConnect:
    
    ANKICONNECT_URL = "http://localhost:8765"

    @staticmethod
    def add_note(deck_name, note_type, note):
        fields = {
            "Front": note.front,
            "Back": note.back
        }

        new_note = {
            'deckName': deck_name,
            'modelName': note_type,
            'fields': fields,
            'options': {
                "allowDuplicate": False,
            },
            'tags': []
        }

        request_data = json.dumps({
            'action': 'addNote',
            'version': 6,
            'params': {
                'note': new_note
            }
        })

        response = requests.post(AnkiConnect.ANKICONNECT_URL, request_data)

        if response.status_code == 200:
            print(f'Added note {note.front} successfully')
        else:
            print(f'AnkiConnect returned error code {response.status_code}')

# Define your note
NOTE_TYPE = "Basic"

# Define the deck to add the note to
DECK_NAME = "teste"

# Define your list of notes
notes_data = [
    {
        "Front": "<h1>teste</h1><p>teste</p>",
        "Back": "<p>resultado do teste</p>"
    },
]


# Create AnkiNote objects
notes = [AnkiNote(front=data["Front"], back=data["Back"]) for data in notes_data]

# Add notes to AnkiConnect
for note in notes:
    AnkiConnect.add_note(deck_name=DECK_NAME, note_type=NOTE_TYPE, note=note)
