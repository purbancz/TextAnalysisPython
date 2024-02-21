class open_conll:
    def __init__(self, filename):
        self.filename = filename

    def __enter__(self):
        self.file = open(self.filename, 'r', encoding='utf-8')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()

    def __iter__(self):
        return self

    def __next__(self):
        line = self.file.readline()
        if not line:
            raise StopIteration
        # return [word.strip('"') for word in line.split()]
        tokens = line.strip().split()
        tokens[:2] = [token[1:-1] for token in tokens[:2]]
        return tokens


if __name__ == "__main__":
    with open_conll("nkjp.conll") as infile:
        for token in infile:
            print(token)
