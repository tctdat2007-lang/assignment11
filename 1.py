class Publication:
    def __init__(self, name):
        self.name = name


class Book(Publication):
    def __init__(self, name, author, pages):
        super().__init__(name)
        self.author = author
        self.pages = pages

    def print_information(self):
        print(f"Book: {self.name}")
        print(f"Author: {self.author}")
        print(f"Pages: {self.pages}")


class Magazine(Publication):
    def __init__(self, name, chief_editor):
        super().__init__(name)
        self.chief_editor = chief_editor

    def print_information(self):
        print(f"Magazine: {self.name}")
        print(f"Chief editor: {self.chief_editor}")

magazine = Magazine("Donald Duck", "Aki Hyyppä")
book = Book("Compartment No. 6", "Rosa Liksom", 192)

magazine.print_information()
print()
book.print_information()
