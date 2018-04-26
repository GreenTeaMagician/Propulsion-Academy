
class Book:
		
	def __init__(self, title, author):
		self.title = title
		self.author = author
		
	def __str__(self):
		return f"{self.title} by {self.author}"#st(self.title) + " and " + str(self.author)
		
		
class Bookcase():
	
	def __init__(self, books):
		self.books = self.create_books(books) 
		
	def create_books(self, books):
		return [Book(t ,a) for t, a in books]

'''
	def create_books(cls, book_list):
		books = []
		
		for title, author in book_list:
			books.append(Book(title, author))
		retur cls(books)
'''
		
	def __iter__(self):
		for book in self.books:
			yield str(book)



