# Activity 1
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", 180)
book2 = Book("To Kill a Mockingbird", "Harper Lee", 281)
book3 = Book("The Alchemist", "Paulo Coelho", 208)
print(book1.title)  
print(book2.author)  
print(book3.pages) 
# Inheritance to explore encapsulation
class EBook(Book):
    def __init__(self, title, author, pages, file_size):
        super().__init__(title, author, pages)
        self.file_size = file_size

# Activity 2
class Entity:
    def move(self):
        pass
class Car(Entity):
    def move(self):
        print("Car:Driving on the road")
class Boat(Entity):
    def move(self):
        print("Boat:Sailing on the water")
class Airplane(Entity):
    def move(self):
        print("Airplane:Flying in the sky")      
objects = [Car(), Boat(), Airplane()]
for obj in objects:
    obj.move()  
