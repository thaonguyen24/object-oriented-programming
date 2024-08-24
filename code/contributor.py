
# This file contains the Contributor and ContributorWithRole classes.
class Contributor:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name
    

class ContributorWithRole:
    def __init__(self, contributor: Contributor, role: str):
        self.contributor = contributor
        self.role = role

    def __str__(self):
        return f"{self.contributor}, ({self.role})"
