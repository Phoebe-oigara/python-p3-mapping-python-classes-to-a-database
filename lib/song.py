from config import CONN, CURSOR

class Song:
    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS songs (
                id INTEGER PRIMARY KEY,
                name TEXT,
                album TEXT
            )
        """
        CURSOR.execute(sql)

    @classmethod
    def create(cls, name, album):
        song = cls(name, album)
        song.save()
        return song

    def __init__(self, name, album):
        self.id = None
        self.name = name
        self.album = album

    def save(self):
        sql = """
            INSERT INTO songs (name, album)
            VALUES (?, ?)
        """
        CURSOR.execute(sql, (self.name, self.album))
        self.id = CURSOR.lastrowid
