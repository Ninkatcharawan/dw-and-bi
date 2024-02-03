# Data Modeling I

## Getting Started

```sh
python -m venv ENV
source ENV/bin/activate
pip install -r requirements.txt
```

### Prerequisite when install psycopg2 package

For Debian/Ubuntu users:

```sh
sudo apt install -y libpq-dev
```

For Mac users:

```sh
brew install postgresql
```

## Running Postgres

```sh
docker-compose up
```

To shutdown, press Ctrl+C and run:

```sh
docker-compose down
```

## Running ETL Scripts

```sh
python create_tables.py
python etl.py
```
## Add Repu Table 

```sh
table_drop_repo = "DROP TABLE IF EXISTS repo"  # Add drop table statement for repo
```

```sh
table_create_repo = """
    CREATE TABLE IF NOT EXISTS repo (
        id int,
        name text,
        url text,
        PRIMARY KEY(id)
    )
```

Repu Table มีประโยชน์สำหรับการวิเคราะห์ในอนาคต เนื่องจากมีข้อมูลเกี่ยวกับพื้นที่เก็บข้อมูลภายในระบบ
