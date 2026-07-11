import sqlite3

DB_NAME = "markets.db"


def init_db():
    conn = sqlite3.connect(DB_NAME)

    conn.execute("""
    CREATE TABLE IF NOT EXISTS market_history(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        market_id TEXT,
        question TEXT,
        yes_price REAL,
        no_price REAL,
        volume REAL,
        liquidity REAL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    conn.commit()
    conn.close()


def save_market(
    market_id,
    question,
    yes_price,
    no_price,
    volume,
    liquidity
):
    conn = sqlite3.connect(DB_NAME)

    conn.execute(
        """
        INSERT INTO market_history
        (
            market_id,
            question,
            yes_price,
            no_price,
            volume,
            liquidity
        )

        VALUES(?,?,?,?,?,?)
        """,
        (
            market_id,
            question,
            yes_price,
            no_price,
            volume,
            liquidity
        )
    )

    conn.commit()
    conn.close()


def get_history(market_id):

    conn = sqlite3.connect(DB_NAME)

    cursor = conn.execute(
        """
        SELECT
            yes_price,
            no_price,
            volume,
            liquidity,
            created_at

        FROM market_history

        WHERE market_id=?

        ORDER BY id DESC

        LIMIT 20
        """,
        (market_id,)
    )

    rows = cursor.fetchall()

    conn.close()

    return rows
