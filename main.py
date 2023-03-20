import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy import text

print(sqlalchemy.__version__);

engine_url = 'sqlite:///stock.db'
engine = create_engine(engine_url, echo=True)

if Stocks.__tablename__ not in engine.table_names():
    create_table(engine)

# exit(0)

# process = CrawlerProcess(get_project_settings())

# process.crawl('stock_code')
# process.start()
