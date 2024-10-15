from zeconfig import ZeConfig

config = ZeConfig('./settings.toml').config()


class SqliteConfig:
    database: str = config['database']['db']
    
sqlset: SqliteConfig = SqliteConfig()
