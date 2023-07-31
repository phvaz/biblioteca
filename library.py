import tkinter as tk

class Book:
    def __init__(self, title, genre, author, availability):
        self.title = title
        self.genre = genre
        self.author = author
        self.availability = True

    def __str__(self):
        return f"Title: {self.title}, Genre: {self.genre}, Author: {self.author}, Availability: {self.availability}"

class Library:
    def __init__(self):
        self.shelf = []

    def add_books(self, book):
        self.shelf.append(book)

    def remove_book(self, book):
        self.shelf.remove(book)
        self.availability = False
        
    def search_book(self, search):
        for book in self.shelf:
            if search.lower() in book.title.lower() or search.lower() in book.author.lower() or search.lower() in book.genre.lower():
                if book.availability:
                    return 'O livro está disponível.'
        return 'Este livro não está disponível.'
        

# Criando objetos livro
livro1 = Book('Hamlet', 'Romance', 'Shakespeare', True)
livro2 = Book('Harry Potter', 'Fantasy', 'J.K. Rowling', True)

# Istânciando objeto livraria
livraria = Library()

# Adicionando ou removendo objetos da livraria
livraria.add_books(livro1)
livraria.add_books(livro2)

print(livraria.search_book('Shakespeare'))

# Função para lidar com a interface GUI

def handle_search():
    search_text = entry.get()
    result = livraria.search_book(search_text)
    result_label.config(text=result)

# Implementação da GUI 

window = tk.Tk()
window.title('Biblioteca')
window.geometry("250x150")
label = tk.Label(window, text='Pesquisar livro: ')
label.pack()
entry = tk.Entry(window)
entry.pack()
search_buttom = tk.Button(window, text='Pesquisar', command=handle_search)
search_buttom.pack()
result_label = tk.Label(window, text="") 
result_label.pack() 
window.mainloop()