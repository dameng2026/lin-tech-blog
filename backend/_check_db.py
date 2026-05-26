import sys
sys.path.insert(0, '.')
from src.app.core.config import settings
from sqlalchemy import create_engine, text

engine = create_engine(settings.DATABASE_URL)
with engine.connect() as conn:
    result = conn.execute(text('SELECT id, title, is_published FROM articles ORDER BY id'))
    rows = result.fetchall()
    if rows:
        for row in rows[:20]:
            title_preview = row[1][:50] if row[1] else '(empty)'
            print(f'id={row[0]}, title={title_preview}, is_published={row[2]}')
    else:
        print('articles 表没有任何数据')

    count = conn.execute(text('SELECT COUNT(*) FROM articles')).scalar()
    published_count = conn.execute(text("SELECT COUNT(*) FROM articles WHERE is_published = 1")).scalar()
    print(f'\n总计: {count}, is_published=1: {published_count}')