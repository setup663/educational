class Parcer:

    def parcing(self, file):
        f_in = open(file, 'r', encoding='UTF-8')
        books = dict()
        for line in f_in:
            s = line.split()
            reader = s[1]
            n_books = int(s[2])
            if reader in books:
                books[reader] += n_books
            else:
                books[reader] = n_books
        f_in.close()
        return books