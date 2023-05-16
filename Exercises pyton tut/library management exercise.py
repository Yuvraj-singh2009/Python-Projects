class library:
    def __init__(self):
        self.books = []
        self.no_of_books = 0
    def listadd(self,newbook):
        self.books.append(newbook)
        self.no_of_books = len(self.books)
    def info(self):
        print(f"list of books is {self.books} and no. of books is {self.no_of_books}")
l1 = library()
# l1.listadd(input("enter your books:\n"))
l1.listadd(input("enter first books name \n"))
l1.listadd(input("enter second books name \n"))
l1.listadd(input("enter third books name \n"))

l1.info()

