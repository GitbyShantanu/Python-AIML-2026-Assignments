# WAP to implement a class named Bookstore with following specs: 
# Class should contain 2 instance variables Name(Book Name) and Author
# Class should contain 1 class variable NoOfBooks (initialise it to 0)

# Define a constructor (__init__) that accepts Name and Author and initialise instance variables. 
# Inside constructor, increment the class variable NoOfBooks by 1 whenever a new obj is created. 

# Implement an instance method: 
#   Display() - should display book details in format: 
#   <BookName> by <Author>. No of Books : <NoOfBooks> 

# Example Usage: 
# obj1 = BookStore("Linux System Programming", "Robert Love")
# obj1.Display() 
# obj2. BookStore("C Programming", "Dennis Ritchie")
# obj2.Display() 

class BookStore:
    NoOfBooks = 0
    def __init__(self, Name, Author):
        self.Name = Name
        self.Author = Author
        BookStore.NoOfBooks += 1

    def Display(self):
        print(f"{self.Name} by {self.Author}. No of Books : {BookStore.NoOfBooks}")

    
obj1 = BookStore("Linux System Programming", "Robert Love")
obj1.Display()

obj2 = BookStore("C Programming", "Dennis Ritchie")
obj2.Display()