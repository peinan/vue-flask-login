from pathlib import Path


class DBInfo:
    db_name: str = 'user.db'
    db_path: str = (Path(__file__).parent / db_name).resolve().__str__()
