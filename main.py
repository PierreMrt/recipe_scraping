from gui import create_window, run
from sqlite import execute_read_query, create_connection


def main():
    conn = create_connection('db_recettes.sqlite')
    window = create_window()
    run(window, conn)


if __name__ == '__main__':
    main()
