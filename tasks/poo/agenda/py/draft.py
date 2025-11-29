class Fone:
    def __init__(self, id: str, number: str):
        self.__id: str = id
        self.__number: str = number

    def isValid(self) -> bool:
        for _ in self.__number:
            if not (_.isdigit() or _ in "()" or _ in "."):
                return False
        return True

    def getId(self) -> str:
        return self.__id
    def getNumber(self) -> str:
        return self.__number

    def __str__(self) -> str:
        return f"{self.__id}:{self.__number}"
    
class Contact:
    def __init__(self, name: str):
        self.__favorited: bool = False
        self.__fones: list[Fone] = []
        self.__name: str = name

    def getFones(self):
        return self.__fones
    def getName(self) -> str:
        return self.__name
    
    def setName(self, name: str) -> None:
        self.__name = name

    def addFone(self, id: str, number: str) -> None: 
        fone = Fone(id, number)
        if not fone.isValid():
            raise Exception("fail: invalid number")
        
        self.__fones.append(fone)

    def rmFone(self, index: int) -> None:
        del self.__fones[index]

    def toogleFavorited(self) -> None:
        self.__favorited = not self.__favorited

    def isFavorited(self) -> bool:
        return self.__favorited

    def __str__(self) -> str:
        favorited = "@ " if self.__favorited is True else "- "
        fones = ", ".join(str(f) for f in self.__fones)
        return f"{favorited}{self.__name} [{fones}]"
    
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
        try:
            if args[0] == "end":
                break
            elif args[0] == "show":
                print(agenda)
            #elif args[0] == "add":
            else:
                print("comando invalido")
        except Exception as e:
            print(e) 
main()