import json
from datetime import datetime

class NoteManager:
    def __init__(self):
        self.notes = []

    def create_note(self, title, content, date=None):
        if date is None:
            date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        note = {
            'title': title,
            'content': content,
            'date': date
        }
        self.notes.append(note)

    def save_notes(self, filename):
        with open(filename, 'w') as file:
            json.dump(self.notes, file)

    def load_notes(self, filename):
        with open(filename, 'r') as file:
            self.notes = json.load(file)

    def read_notes(self):
        for i, note in enumerate(self.notes):
            print(f"Примечание {i+1}:")
            print(f"Заголовок: {note['title']}")
            print(f"Содержание: {note['content']}")
            print(f"Дата: {note['date']}")
            print()

    def edit_note(self, index, new_title, new_content):
        if index < 1 or index > len(self.notes):
            print("Ошибочный индекс примечания")
            return
        self.notes[index-1]['title'] = new_title
        self.notes[index-1]['content'] = new_content

    def delete_note(self, index):
        if index < 1 or index > len(self.notes):
            print("Ошибочный индекс примечания")
            return
        del self.notes[index-1]

    def list_notes(self):
        for i, note in enumerate(self.notes):
            print(f"{i + 1}. {note['title']} - {note['date']}")

    def find_notes_by_date(self, date):
        notes_found = []
        for note in self.notes:
            if note['date'] == date: notes_found.append(note)
        if len(notes_found) == 0:
            print("Примечания не найдены")
            return
        print(f"Найдено {len(notes_found)} примечаний:")
        for i, note in enumerate(notes_found):
            print(f"Примечание {i+1}:")
            print(f"Заголовок: {note['title']}")
            print(f"Содержание: {note['content']}")
            print(f"Дата: {note['date']}")
            print()            

         
manager = NoteManager() # используется для работы с заметками

manager.create_note("Заметка 1", "Описание заметки 1", datetime.now().strftime("%Y-%m-%d"))
manager.create_note("Заметка 2", "Описание заметки 2", datetime.now().strftime("%Y-%m-%d"))
manager.create_note("Заметка 3", "Описание заметки 3", "2021-01-01")
manager.save_notes("notes.json") # для сохранения заметок

manager.load_notes("notes.json") # для загрузка заметок
manager.read_notes() # для чтения заметок

manager.delete_note(2) # необходимо для удаления и заметки

manager.find_notes_by_date(datetime.now().strftime("%Y-%m-%d")) # для выборки заметок по дате















