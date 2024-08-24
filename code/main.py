
# Description: This file contains the main function that creates contributors, contributors with roles, library items, and a catalog. It also finds an item in the catalog and displays information about items in the catalog.
from contributor import Contributor, ContributorWithRole
from library_items import Book, Magazine, Dvd, Cd
from catalog import Catalog


def main():
    # Create contributors
    JKRowling = Contributor("J. K. Rowling")
    StephenKing = Contributor("Stephen King")
    WilliamShakespeare = Contributor("William Shakespeare")
    AliceJohnson = Contributor("Alice Johnson")
    BobBrown = Contributor("Bob Brown")
    ChristopherNolan = Contributor("Christopher Nolan")
    StevenSpielberg = Contributor("Steven Spielberg")
    RidleyScott = Contributor("Ridley Scott")
    ChrisColumbus = Contributor("Chris Columbus")
    StephenFry = Contributor("Stephen Fry")
    TheBeatles = Contributor("The Beatles")
    LadyGaga = Contributor("Lady Gaga")
    LeonardoDiCaprio = Contributor("Leonardo DiCaprio")
    CillianMurphy = Contributor("Cillian Murphy")
    JeffGoldBlum = Contributor("Jeff Goldblum")
    LauraDern = Contributor("Laura Dern")
    DanielRadcliffe = Contributor("Daniel Radcliffe")
    EmmaWatson = Contributor("Emma Watson")
    RupertGrint = Contributor("Rupert Grint")


    # Create contributors with role
    JKRowling_author = ContributorWithRole(JKRowling, "author")
    StephenKing_author = ContributorWithRole(StephenKing, "author")
    WilliamShakespeare_author = ContributorWithRole(WilliamShakespeare, "author")
    AliceJohnson_editor = ContributorWithRole(AliceJohnson, "editor")
    BobBrown_editor = ContributorWithRole(BobBrown, "editor")
    ChristopherNolan_director = ContributorWithRole(ChristopherNolan, "director")
    StevenSpielberg_director = ContributorWithRole(StevenSpielberg, "director")
    RidleyScott_director = ContributorWithRole(RidleyScott, "director")
    ChrisColumbus_director = ContributorWithRole(ChrisColumbus, "director")
    StephenFry_narrator = ContributorWithRole(StephenFry, "narrator")
    TheBeatles_artist = ContributorWithRole(TheBeatles, "artist")
    LadyGaga_artist = ContributorWithRole(LadyGaga, "artist")
    LadyGaga_actress = ContributorWithRole(LadyGaga, "actress")
    LeonardoDiCaprio_actor = ContributorWithRole(LeonardoDiCaprio, "actor")
    CillianMurphy_actor = ContributorWithRole(CillianMurphy, "actor")
    JeffGoldBlum_actor = ContributorWithRole(JeffGoldBlum, "actor")
    LauraDern_actress = ContributorWithRole(LauraDern, "actress")
    DanielRadcliff_actor = ContributorWithRole(DanielRadcliffe, "actor")
    EmmaWatson_actress = ContributorWithRole(EmmaWatson, "actress")
    RupertGrint_actor = ContributorWithRole(RupertGrint, "actor")
        

    # Create library items
    book1 = Book("Harry Potter and the Philosopher's Stone", [JKRowling_author], 1997, "English", "9780747532743", "Bloomsbury", 823.914)
    book2 = Book("The Shining", [StephenKing_author], 1977, "English", "9780385121675", "Doubleday", 813.540)
    book3 = Book("Macbeth", [WilliamShakespeare_author], 1986, "German", "9783150000175", "Reclam", 764.876)
    magazine1 = Magazine("Vogue", [AliceJohnson_editor], 1892, "German", 123456789, "Conde Nast", 1, 1, "Fashion")
    magazine2 = Magazine("National Geographic", [BobBrown_editor], 1888, "English", 123456788, "National Geographic Society", 1, 1, "Science")
    dvd1 = Dvd("Inception", [ChristopherNolan_director, LeonardoDiCaprio_actor, CillianMurphy_actor], 2010, "English", "Action", "PG-13", "Warner Bros. Pictures")
    dvd2 = Dvd("Harry Potter and the Philosopher's Stone", [ChrisColumbus_director, DanielRadcliff_actor, EmmaWatson_actress, RupertGrint_actor], 2001, "German", "Fantasy", "PG", "Warner Bros. Pictures")
    dvd3 = Dvd("Jurassic Park", [StevenSpielberg_director, JeffGoldBlum_actor, LauraDern_actress], 1993, "German", "Sci-fi", "PG-13", "Universal Pictures")
    dvd4 = Dvd("House of Gucci", [RidleyScott_director, LadyGaga_actress], 2021, "German", "Drama", "PG-13", "Universal Pictures")
    cd1 = Cd("Abbey Road", [TheBeatles_artist], 1969, "English", "Rock", "Music")
    cd2 = Cd("Harry Potter and the Philosopher's Stone", [StephenFry_narrator], 2001, "English", "fantasy", "Audiobook")
    cd3 = Cd("Chromatica", [LadyGaga_artist], 2020, "English", "Pop", "Music")


    # Create a catalog
    catalog = Catalog()
    catalog.add_item(book1)
    catalog.add_item(book2)
    catalog.add_item(book3)
    catalog.add_item(magazine1)
    catalog.add_item(magazine2)
    catalog.add_item(dvd1)
    catalog.add_item(dvd2)
    catalog.add_item(dvd3)
    catalog.add_item(dvd4)
    catalog.add_item(cd1)
    catalog.add_item(cd2)
    catalog.add_item(cd3)


    # Display information about all items in the catalog
    # catalog.display_itemlist()

    # Remove an item from the catalog
    # catalog.remove_item(book3)

    # Display information about items in the catalog
    # catalog.display_info("Harry Potter")

    # Find location of items
    # catalog.find_item("Harry Potter and the Philosopher's Stone")

    # Check if an item is reserved
    # catalog.is_item_reserved("Harry Potter and the Philosopher's Stone", "Book")

    # Set the reserved status of an item
    # catalog.set_item_reserved("Harry Potter and the Philosopher's Stone", "book", True)
    
    # Display information of available items only
    # catalog.display_available_items()


if __name__ == "__main__":
    main()
