import database as db
import psycopg2

# Main execution logic
def main(con):
    """
    Main menu
    """
    pass


if __name__ == '__main__':
    con = db.connect_db()
    db.create_tables(con=con)
    main(con=con)