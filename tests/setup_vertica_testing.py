import vertica_python
import yaml


class SetupVerticaTesting:

    def __init__(self):
        with open("configs/testing-config.yml", 'r') as yaml_file:
            self.config = yaml.safe_load(yaml_file)
        
        with open("configs/config.yml", 'r') as yaml_file:
            print(self.config)
            self.config.update(yaml.safe_load(yaml_file))
            print(self.config)

        self.conn_info = self.config.get("conn_info")
        self.dims_schema = self.config.get("dims_schema")
        self.dims_table = self.config.get("dims_table")
        self.staging_schema = self.config.get("staging_schema")


    def create_schema(self, *schemas):
        with vertica_python.connect(**self.conn_info) as conn:
            cursor = conn.cursor()
            for schema in schemas:
                create_schema_query = f"CREATE SCHEMA IF NOT EXISTS {schema}"
                cursor.execute(create_schema_query)


    def create_table(self, schema_name, table_name):
        create_table_query = f"""
            CREATE TABLE IF NOT EXISTS {schema_name}.{table_name} (
                year INTEGER,
                month INTEGER,
                name VARCHAR(50),
                column3 DATE
            )
        """
        with vertica_python.connect(**self.conn_info) as conn:
            cursor = conn.cursor()
            cursor.execute(create_table_query)


    def populate_table(self, schema_name, table_name):
        truncate_query = f"TRUNCATE TABLE {schema_name}.{table_name}"
        insert_query = f"""
            INSERT INTO {schema_name}.{table_name} VALUES 
            (2024, 1, 'Sb', '2024-01-08'),
            (2024, 2, 'Sb', '2024-02-09'),
            (2024, 2, 'Bs', '2024-02-09');
        """

        with vertica_python.connect(**self.conn_info) as conn:
            cursor = conn.cursor()
            cursor.execute(truncate_query)
            cursor.execute(insert_query)

    
    def setup(self):
        self.create_schema(self.dims_schema, self.staging_schema)
        self.create_table(self.dims_schema, self.dims_table)
        self.populate_table(self.dims_schema, self.dims_table)

