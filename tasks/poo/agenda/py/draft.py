class Fone:
    def __init__(self, id: str, number: str):
        self.__id: str = id
        self.__number: str = number

    def isValid(self) -> bool:
        for c in self.__number:
            if not (c.isdigit() or c in "()-."):
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
        self.__name: str = name
        self.__favorited: bool = False
        self.__fones: list[Fone] = []

    def getFones(self):
        return self.__fones
    
    def getName(self) -> str:
        return self.__name
    
    def getFavorited(self):
        return self.__favorited
    
    def setName(self, name: str) -> None:
        self.__name = name

    def addFone(self, id: str, number: str) -> None: 
        fone = Fone(id, number)
        if not fone.isValid():
            raise Exception("fail: invalid number")
        
        self.__fones.append(fone)

    def rmFone(self, index: int) -> None:
        try:
            index = int(index)
            del self.__fones[index]
        except:
            raise Exception(f"fail: fone {index} not found")

    def favorite(self) -> None:
        self.__favorited = True

    def unfavorite(self) -> None:
        self.__favorited = False

    def toggleFavorite(self):
        self.__favorited = not self.__favorited

    def __str__(self) -> str:
        fav = "@ " if self.__favorited else "- "
        fones = ", ".join(str(f) for f in self.__fones)
        return f"{fav}{self.__name} [{fones}]"
    
class Agenda:
    def __init__(self):
        self.__contacts: dict[str, Contact] = {}

    def __findPosByName(self, contact: Contact):
        return contact.getName()
    
    def getContacts(self):
        return self.__contacts

    def addContact(self, name: str, tokens: list[str]):
        if name not in self.__contacts:
            self.__contacts[name] = Contact(name)

        contact = self.__contacts[name]

        for token in tokens:
            if ":" not in token:
                raise Exception("fail: invalid format")
            id, number = token.split(":")
            contact.addFone(id, number)

    def getContact(self, name: str) -> Contact:
        try:
            return self.__contacts[name]
        except KeyError:
            raise Exception(f"fail: contact {name} not found")

    def rmContact(self, name: str):
        if name not in self.__contacts:
            raise Exception(f"fail: contact {name} not found")
        del self.__contacts[name]
    
    def search(self, pattern: str) -> list[Contact]:
        result: list[Contact] = []

        for contact in self.__contacts.values():

            if pattern in contact.getName():
                result.append(contact)
                continue

            for fone in contact.getFones():
                if pattern in fone.getId() or pattern in fone.getNumber():
                    result.append(contact)
                    break
        
        result.sort(key=self.__findPosByName)
        return result

    def getFavorited(self) -> list[Contact]:
        retorno = [c for c in self.__contacts.values() if c.getFavorited()]
        retorno.sort(key=self.__findPosByName)
        return retorno

    def __str__(self) -> str:
        lista = list(self.__contacts.values())
        lista.sort(key=self.__findPosByName)
        return "\n".join(str(c) for c in lista)

def main():
    agenda = Agenda()
    while True:
        line: str = input()
        print("$" + line)
        args: list[str] = line.split(" ")
        try:
            if args[0] == "end":
                break
            elif args[0] == "show":
                print(agenda)
            elif args[0] == "add":
                agenda.addContact(args[1], args[2:])
            elif args[0] == "rmFone":
                agenda.getContact(args[1]).rmFone(args[2])
            elif args[0] == "rm":
                agenda.rmContact(args[1])
            elif args[0] == "search":
                for c in agenda.search(args[1]):
                    print(c)
            elif args[0] == "fav":
                agenda.getContact(args[1]).favorite()
            elif args[0] == "unfav":
                agenda.getContact(args[1]).unfavorite()
            elif args[0] == "tfav":
                agenda.getContact(args[1]).toggleFavorite()
            elif args[0] == "favs":
                for c in agenda.getFavorited():
                    print(c)
            else:
                print("fail: invalid comand")
        except Exception as e:
            print(e) 
main()
