import json
import sqlite3
from pathlib import Path

def ingest(pages, connection):
    connection.execute('CREATE TABLE IF NOT EXISTS records(id TEXT PRIMARY KEY, amount REAL, updated_at TEXT)')
    connection.execute('CREATE TABLE IF NOT EXISTS state(name TEXT PRIMARY KEY, watermark TEXT)')
    watermark_row=connection.execute("SELECT watermark FROM state WHERE name='orders'").fetchone()
    watermark=watermark_row[0] if watermark_row else ''
    applied=0
    for page in pages:
        for row in page['items']:
            if row['updated_at']<=watermark: continue
            previous=connection.execute('SELECT updated_at FROM records WHERE id=?',(row['id'],)).fetchone()
            if not previous or row['updated_at']>previous[0]:
                connection.execute('INSERT INTO records VALUES (?,?,?) ON CONFLICT(id) DO UPDATE SET amount=excluded.amount,updated_at=excluded.updated_at',(row['id'],row['amount'],row['updated_at']))
                applied+=1
            watermark=max(watermark,row['updated_at'])
    connection.execute("INSERT INTO state VALUES('orders',?) ON CONFLICT(name) DO UPDATE SET watermark=excluded.watermark",(watermark,))
    connection.commit()
    return applied

def run(path='data/api_pages.json'):
    pages=json.loads(Path(path).read_text())
    db=sqlite3.connect(':memory:')
    first=ingest(pages,db); second=ingest(pages,db)
    return {'first_load_applied':first,'rerun_applied':second,'stored_records':db.execute('SELECT COUNT(*) FROM records').fetchone()[0]}

if __name__ == '__main__':
    import json
    print(json.dumps(run(), indent=2))
