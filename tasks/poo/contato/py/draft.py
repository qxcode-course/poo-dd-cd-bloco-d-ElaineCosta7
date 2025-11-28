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

    def addFone(self, id: str, number: str) -> None:
        self.__fones.append(f"{id}:{number}") 

    def rmFone(self, index: int) -> None:
        del self.__fones[index]

    #def toogleFavorited(self) -> None:

    #def isFavorited(self) -> bool:

    def __str__(self) -> str:
        fones = ", ".join(self.__fones)
        return f"- {self.__name} [{fones}]"

def main():
    contact = Contact
    while True:
        line: str = input()
        print("$" + line)
        args: list[str] = line.split(" ")
        try:
            if args[0] == "end":
                break
            elif args[0] == "show":
                print(contact)
            elif args[0] == "init":
                name = args[1]
                contact = Contact(name)
            elif args[0] == "add":
                id = args[1]
                number = int(args[2])
                contact.addFone(id, number)
            else:
                print("comando invalido")
        except Exception as e:
            print(e) 
main()