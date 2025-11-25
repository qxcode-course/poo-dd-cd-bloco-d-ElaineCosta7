class Fone:
    def __init__(self, id: str, number: str):
        self.__id: str = id
        self.__number: str = number

    #def isValid(self) -> bool:

    def getId(self) -> str:
        return self.__id
    def getNumber(self) -> str:
        return self.__number

    def __str__(self) -> str:
        return f""
    
class Contact:
    def __init__(self, name: str):
        self.__favorited: bool
        self.__fones: list[Fone] = []
        self.__name: str = name

    def getFones(self):
        return self.__fones
    def getName(self) -> str:
        return self.__name
    
    def setName(self, name: str) -> None:
        self.__name = name

    #def addFone(self, id: str, number: str) -> None: 

    #def rmFone(self, index: int) -> None:

    #def toogleFavorited(self) -> None:

    #def isFavorited(self) -> bool:

    def __str__(self) -> str:
        return f""
    
class Agenda:
    def __init__(self):
        self.__contacts: list[Contact] = []

    #def __findPosByName(self, name: str) -> int:

    def getContacts(self):
        return self.__contacts

    #def addContact(self, name: str, fones: list[Fone]):

    #def getContact(self, name: str) -> Contact | None:

    #def rmContact(self. name: str):

    #def search(self, pattern: str):

    #def getFavorited(self):

    def __str__(self) -> str:
        return f""

def main():
    agenda = Agenda
    while True:
        line: str = input()
        print("$" + line)
        args: list[str] = line.split(" ")
        if args[0] == "end":
            break
        elif args[0] == "show":
            print(agenda)
        else:
            print("comando invalido")
    
main()