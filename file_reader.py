class FileReader:

    def __init__(self):
        pass

    def get_accounts(self, filename: str = 'accounts.txt') -> str:
        with open(filename, 'r') as f:
            return '|'.join(map(lambda s: s.strip(), f.readlines()))

    def write_to_accounts(self, content: str, filename: str = '') -> bool:
        pass

    def append_to_accounts(self, content: str, filename: str = '') -> bool:
        with open(filename, 'a') as f:
            f.write(content)
        return f.closed
