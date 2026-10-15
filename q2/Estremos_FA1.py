class Publication:
    def __init__(self, title, author):
        self.__title = title
        self.__author = author

    def get_title(self):
        return self.__title

    def get_author(self):
        return self.__author

    def set_title(self, title):
        self.__title = title

    def set_author(self, author):
        self.__author = author

    def display_info(self):
        print("Title:", self.get_title())
        print("Author:", self.get_author())


class Book(Publication):
    def __init__(self, title, author, number_pages):
        Publication.__init__(self, title, author)
        self.__number_of_pages = 0
        self.set_number_of_pages(number_pages)

    def get_number_of_pages(self):
        return self.__number_of_pages

    def set_number_of_pages(self, number_pages):
        if number_pages > 0:
            self.__number_of_pages = number_pages
        else:
            print("Number of pages must be positive.")

    def display_info(self):
        Publication.display_info(self)
        print("Number of pages:", self.get_number_of_pages())


class Magazine(Publication):
    def __init__(self, title, author, issue_number):
        Publication.__init__(self, title, author)
        self.__issue_number = 0
        self.set_issue_number(issue_number)

    def get_issue_number(self):
        return self.__issue_number

    def set_issue_number(self, issue_number):
        if issue_number > 0:
            self.__issue_number = issue_number
        else:
            print("Issue number must be positive.")

    def display_info(self):
        Publication.display_info(self)
        print("Issue number:", self.get_issue_number())


pub1 = Publication("Journal of Experimental Psychology", "Ratchiff, R. & Van Dongen, H.")
pub2 = Publication("Philippine Daily Report", "Dela Cruz, J.")
book1 = Book("The Hobbit", "J.R.R. Tolkien", 310)
book2 = Book("Noli Me Tangere", "Jose Rizal", 438)
mag1 = Magazine("National Geographic", "Various Authors", 202)
mag2 = Magazine("Time", "Various Authors", 15)

print("Publication Information:")
pub1.display_info()
print()
pub2.display_info()

print("\nBook Information:")
book1.set_number_of_pages(-310)
book1.display_info()
print(book1.get_number_of_pages())
print()
book2.display_info()

print("\nMagazine Information:")
mag1.display_info()
print(mag1.get_issue_number())
print()
mag2.set_issue_number(0)
mag2.display_info()
