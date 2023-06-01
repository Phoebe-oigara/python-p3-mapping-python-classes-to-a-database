#!/usr/bin/env python3

from config import CONN, CURSOR
from song import Song

if __name__ == '__main__':
    Song.create_table()

    CURSOR.execute("PRAGMA table_info(songs)").fetchall()

    hello = Song("Hello", "25")
    hello.save()

    despacito = Song("Despacito", "Vida")
    despacito.save()

    CONN.commit()
    CONN.close()
