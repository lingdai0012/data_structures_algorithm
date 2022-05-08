# python3


class Query:
    def __init__(self, query):
        self.type = query[0]
        self.number = int(query[1])
        if self.type == "add":
            self.name = query[2]


class PhoneBook:
    def __init__(self):
        self.__phone_book = {}

    def add(self, query: Query):
        self.__phone_book[query.number] = query.name

    def delete(self, query: Query):
        if self.find(query) != "not found":
            self.__phone_book.pop(query.number)
        else:
            pass

    def find(self, query: Query):
        return self.__phone_book.get(query.number, "not found")

    def get_phone_book(self):
        return self.__phone_book


def read_queries():
    n = int(input())
    return [Query(input().split()) for i in range(n)]


def write_responses(result):
    print("\n".join(result))


def process_queries(queries):
    result = []
    # # Keep list of all existing (i.e. not deleted yet) contacts.
    contacts = PhoneBook()
    for cur_query in queries:
        if cur_query.type == "add":
            contacts.add(cur_query)
        elif cur_query.type == "del":
            contacts.delete(cur_query)
        else:
            result.append(contacts.find(cur_query))
    return result


if __name__ == "__main__":
    write_responses(process_queries(read_queries()))
