"""Profile PostgreSQL queries with EXPLAIN ANALYZE for database-side insight."""

import time

import psycopg2


def profile_postgres_query(query, db_config):
    """Connect to PostgreSQL, run EXPLAIN ANALYZE, and return the plan rows."""
    connection = psycopg2.connect(
        host=db_config["host"],
        port=db_config["port"],
        database=db_config["database"],
        user=db_config["user"],
        password=db_config["password"],
    )

    cursor = connection.cursor()

    explain_query = f"EXPLAIN ANALYZE {query}"

    start = time.perf_counter()
    cursor.execute(explain_query)
    result = cursor.fetchall()
    end = time.perf_counter()

    elapsed = end - start

    print(f"[POSTGRES] Query profiling completed in {elapsed:.4f} seconds")

    for row in result:
        print(row[0])

    cursor.close()
    connection.close()

    return result
