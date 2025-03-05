class Book:
  def __init__(self, title, author):
    self.title = title
    self.author = author

class Library:
  def __init__(self):
    self.books = []

  def add_book(self, book):
    
