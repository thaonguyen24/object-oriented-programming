
from abc import ABC, abstractmethod
from contributor import ContributorWithRole


class LibraryItem(ABC):
    def __init__(self, title: str, contributors: list[ContributorWithRole], release_year: int, language: str, reserved: bool = False):
        self.title = title
        self.contributors = contributors
        self.release_year = release_year
        self.language = language
        self.reserved = reserved  # True if the item is reserved, False otherwise

    @abstractmethod
    def locate(self) -> str:
        """Abstract method to locate the item in the library"""
        pass

    def is_reserved(self) -> bool:
        """Return True if the item is reserved, False otherwise"""
        return self.reserved
    
    def set_reserved(self, reserved: bool):
        """Set the reserved status of the item"""
        self.reserved = reserved

    @abstractmethod
    def display_info(self) -> str:
        """Abstract method to display information about the item"""
        pass
    

# Example for inheriting from the LibraryItem class
class Book(LibraryItem):
    def __init__(self, title: str, contributors: list[ContributorWithRole], release_year: int, language: str, isbn: int, publisher: str, dds_number: int):
        super().__init__(title, contributors, release_year, language)
        self.isbn = isbn
        self.publisher = publisher
        self.dds_number = dds_number  # Dewey Decimal System number

    # Overriding the locate method
    def locate(self) -> str:
        return f"Book {self.title} is located on shelf number {self.dds_number}"
    
    # Overriding the display_info method
    def display_info(self) -> str:
        author = ", ".join([c.contributor.name for c in self.contributors if c.role == "author"])
        return (f"Book Info: \nTitle: {self.title}\nAuthor(s): {author}\nLanguage: {self.language}\n"
                f"Publisher: {self.publisher}\nISBN: {self.isbn}\nRelease Year: {self.release_year}\n"
                f"Reserve Status: {'Reserved' if self.reserved else 'Available'}")
    

class Magazine(LibraryItem):
    def __init__(self, title: str, contributors: list[ContributorWithRole], release_year: int, language: str, issn: int, publisher: str, volume: int, issue: int, subject: str):
        super().__init__(title, contributors, release_year, language)
        self.issn = issn
        self.publisher = publisher
        self.volume = volume
        self.issue = issue
        self.subject = subject  # e.g. fashion, science, sports

    # Overriding the locate method
    def locate(self) -> str:
        return f"Magazine {self.title} is located in shelf area {self.subject}"
    
    # Overriding the display_info method
    def display_info(self) -> str:
        editor = ", ".join([c.contributor.name for c in self.contributors if c.role == "editor"])
        return (f"Magazine Info: \nTitle: {self.title}\nVolume: {self.volume}\nIssue: {self.issue}\nSubject: {self.subject}\n"
                f"Editor(s): {editor} \nPublisher: {self.publisher}\nISSN: {self.issn}\nRelease Year: {self.release_year}\n"
                f"Reserve Status: {'Reserved' if self.reserved else 'Available'}")
    

class Dvd(LibraryItem):
    def __init__(self, title: str, contributors: list[ContributorWithRole], release_year: int, language: str, genre: str, age_rating: str, studio: str):
        super().__init__(title, contributors, release_year, language)
        self.genre = genre  # e.g. action, comedy, drama
        self.age_rating = age_rating
        self.studio = studio

    # Overriding the locate method
    def locate(self) -> str:
        return f"DVD {self.title} is located in shelf area {self.genre}"
    
    # Overriding the display_info method
    def display_info(self) -> str:
        director = ", ".join([c.contributor.name for c in self.contributors if c.role == "director"])
        cast = ", ".join([c.contributor.name for c in self.contributors if c.role == "actor" or c.role == "actress"])
        return (f"DVD Info: \nTitle: {self.title}\nDirector(s): {director}\nCast: {cast}\n"
                f"Genre: {self.genre}\nAge Rating: {self.age_rating}\nStudio: {self.studio}\n"
                f"Reserve Status: {'Reserved' if self.reserved else 'Available'}")
    

class Cd(LibraryItem):
    def __init__(self, title: str, contributors: list[ContributorWithRole], release_year: int, language: str, genre: str, category: str):
        super().__init__(title, contributors, release_year, language)
        self.genre = genre  # e.g. rock, pop, classical
        self.category = category  # e.g. music or audiobook

    # Overriding the locate method
    def locate(self) -> str:
        return f"CD {self.title} is located in shelf area {self.category} with genre {self.genre}"
    
    # Overriding the display_info method
    def display_info(self) -> str:
        artist = ", ".join([c.contributor.name for c in self.contributors if c.role == "artist"])
        narrator =", ".join([c.contributor.name for c in self.contributors if c.role == "narrator"])
        
        if self.category.lower() == "music":  # If the CD is a music CD
            return (f"CD Info: \nTitle: {self.title}\nArtist(s): {artist}\nGenre: {self.genre}\n"
                f"Category: {self.category}\nRelease Year: {self.release_year}\n"
                f"Reserve Status: {'Reserved' if self.reserved else 'Available'}")
        elif self.category.lower() == "audiobook":  # If the CD is an audiobook
            return(f"CD Info: \nTitle: {self.title}\nNarrator(s)= {narrator}\nGenre: {self.genre}\n"
                f"Category: {self.category}\nRelease Year: {self.release_year}\n"
                f"Reserve Status: {'Reserved' if self.reserved else 'Available'}")
