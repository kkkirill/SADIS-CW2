class FileReader:

    def __init__(self):
        pass

    def get_content_from_file(self, filename: str) -> str:
        with open(filename, 'r', encoding='windows-1251') as f:
            f.seek(0)
            if not f.read(1):
                return ''
            else:
                f.seek(0)
                return '|'.join(map(lambda s: s.strip(), f.readlines()))

    def write_to_file(self, content: str, filename: str) -> bool:
        with open(filename, 'w') as f:
            f.write(content)
        return f.closed

    def append_to_file(self, content: str, filename: str) -> bool:
        with open(filename, 'a') as f:
            f.write(content)
        return f.closed
