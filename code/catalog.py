
from library_items import LibraryItem


class Catalog: 
    def __init__(self):
        self.itemlist = []
    

    def add_item(self, item: LibraryItem):
        """Add an item to the catalog"""
        self.itemlist.append(item)


    def remove_item(self, item: LibraryItem):
        """Remove an item from the catalog"""
        if item in self.itemlist:
           self.itemlist.remove(item)
        else:
            raise ValueError("Item not found in the catalog")
    

    def display_itemlist(self):
        """Display information about all items in the catalog"""
        if not self.itemlist:
            print("The catalog is empty")
        for item in self.itemlist:
            print(item.display_info())
            print("-" * 50)  # Separate items with a line
    
   
    def display_info(self, title: str) -> str:
        """Search item and display information in the catalog"""
        matching_items = [item for item in self.itemlist
                            if item.title.lower() == title.lower() or title.lower() in item.title.lower()]  # Case insensitive search
    
        if matching_items:  # If items are found
            separate = "-" * 50
            return print(f"\n{separate}\n".join(item.display_info() for item in matching_items))  # Display information about the items
        return print(f"Item {title} not found in the catalog")  # If no items are found


    def find_item(self, title: str) -> str:
        """Find location of an item in the catalog"""
        matching_items = [item for item in self.itemlist 
                          if item.title.lower() == title.lower() or title.lower() in item.title.lower()]  # Case insensitive search
        
        if matching_items:  # If items are found
            separate = "-" * 50
            return print(f"\n{separate}\n".join(item.locate() for item in matching_items))  # Return the location of the items
        return print(f"Item '{title}' not found in the catalog")  # If no items are found
            

    def is_item_reserved(self, title: str, classname: str) -> bool:
        """Check if an item is reserved by title and classname"""
        for item in self.itemlist:
            if item.title.lower() == title.lower() and item.__class__.__name__.lower() == classname.lower():  # Case insensitive search
                return print(f"{title} ({classname}) is available"  # Return the availability status
                             if not item.is_reserved() else f"{title} ({classname}) is reserved")
        return print(f"Item {title} ({classname}) not found")  # If the item is not found
    

    def set_item_reserved(self, title: str, classname: str, reserved: bool) -> str:
        """Set the reserved status of an item"""
        for item in self.itemlist:
            if item.title.lower() == title.lower() and item.__class__.__name__.lower() == classname.lower():  # Case insensitive search
                item.set_reserved(reserved)  # Set the reserved status
                return print(f"{title} ({classname}) reserved status set to {reserved}")
        return print(f"Item {title} ({classname}) not found")  # If the item is not found


    def display_available_items(self) -> str:
        """Display information about available items in the catalog"""
        available_items = [item for item in self.itemlist if not item.is_reserved()]  # Filter items that are not reserved
        if available_items:
            separate = "-" * 50  # Separate items with a line
            return print(f"\n{separate}\n".join([item.display_info() for item in available_items]))  # Return information about the available items
        return print("No available items in the catalog")  # If no items are available
