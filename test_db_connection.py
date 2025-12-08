#!/usr/bin/env python3
"""Test PostgreSQL/PostGIS database connection"""

import psycopg2
from psycopg2.extras import RealDictCursor

# Database connection parameters
DB_CONFIG = {
    'dbname': 'agufmdb',
    'user': 'agufm2025',
    'password': 'agufm2025',
    'host': 'localhost',
    'port': '5432'
}


def test_connection():
    """Test the database connection and PostGIS extension"""
    try:
        # Connect to the database
        conn = psycopg2.connect(**DB_CONFIG)
        print("✓ Successfully connected to PostgreSQL database!")

        # Create a cursor
        cur = conn.cursor(cursor_factory=RealDictCursor)

        # Test basic query
        cur.execute("SELECT version();")
        version = cur.fetchone()
        print(f"✓ PostgreSQL version: {version['version']}")

        # Test PostGIS extension
        cur.execute("SELECT PostGIS_Version();")
        postgis_version = cur.fetchone()
        print(f"✓ PostGIS version: {postgis_version['postgis_version']}")

        # List all tables
        cur.execute("""
            SELECT table_name 
            FROM information_schema.tables 
            WHERE table_schema = 'public'
            ORDER BY table_name;
        """)
        tables = cur.fetchall()
        print(f"\n✓ Tables in database: {len(tables)}")
        if tables:
            for table in tables:
                print(f"  - {table['table_name']}")
        else:
            print("  (no tables yet)")

        # Close cursor and connection
        cur.close()
        conn.close()
        print("\n✓ Connection test successful!")
        return True

    except psycopg2.Error as e:
        print(f"✗ Database error: {e}")
        return False
    except Exception as e:
        print(f"✗ Error: {e}")
        return False


if __name__ == "__main__":
    test_connection()
