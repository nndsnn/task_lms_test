import sqlite3

input_sector = input()
input_usefulnes = int(input())

conn = sqlite3.connect("travellers.db")

cur = conn.cursor()

result = cur.execute("""select Gifts.gift, Gifts.received
                    from Gifts
                    INNER JOIN sectors ON Gifts.sector_id = sectors.id
                    where sectors.sector = ? and Gifts.usefulnes = ?
                    ORDER BY Gifts.year, Gifts.gift """).fetchall()
