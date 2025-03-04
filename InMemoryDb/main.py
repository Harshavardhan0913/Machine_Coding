from datetime import datetime
class Database:
    def __init__(self):
        self.tables = {}
        self.table_id = 1
        self.created_time = datetime.now()

    def create_table(self, columns = []):
        self.tables[self.table_id] = Table(columns)
        table_id = self.table_id
        self.table_id += 1
        return table_id

    def delete_table(self, table_id):
        if table_id not in self.tables:
            print(f"Table id:{table_id} not present in the db.")
            return -1
        del self.tables[table_id]
    
    def get_table(self, table_id):
        if table_id not in self.tables:
            print(f"Table id:{table_id} not present in the db.")
            return -1
        return self.tables[table_id]
        

class Table:
    def __init__(self, columns:dict={}):
        self.rows = {}
        self.row_id = 1
        self.columns_map = columns
        self.index = {}
        self.created_time = datetime.now()

    def add_column(self, column, column_type):
        if column in self.columns_map.keys():
            print(f"{column} column already in table")
            return -1
        self.columns_map[column] = column_type
        print("Column added successfully")
        return 1

    def delete_column(self, column):
        if column not in self.columns:
            print(f"{column} column not in table")
            return -1
        del self.columns_map[column]
        del self.index[column]
        return 1

    def create_row(self, row_data: dict):
        if not row_data:
            print("Row is empty")
            return -1
        row_columns = row_data.keys()
        if set(row_columns) != set(self.columns_map.keys()):
            print("Invalid Columns")
            return -1
        for column in row_data.keys():
            if type(row_data[column])!= self.columns_map[column]:
                print("Incorrect column type")
                return -1
        row_id = self.row_id
        for column_name, value in row_data.items():
            if column_name not in self.index:
                self.index[column_name] = {}
            if value not in self.index[column_name]:
                self.index[column_name][value] = []
            self.index[column_name][value].append(row_id)
        self.rows[row_id] = Row(row_data, self.columns_map)
        self.row_id += 1
        print("Successfully created row")
        return row_id

    def delete_row(self, row_id):
        if row_id not in self.rows.keys():
            print(f"Row id: {row_id} not in Table")
            return -1
        row = self.rows[row_id].get_row()
        del self.rows[row_id]
        for column, value in row.items():
            if column in self.index:
                if value in self.index[column]:
                    if row_id in self.index[column][value]:
                        self.index[column][value].remove(row_id)
        print(f"Successfully deleted row: {row_id}")
        return 1
    
    def get_row(self, row_id):
        if row_id not in self.rows:
            print(f" Row :{row_id} not in Table")
            return -1
        print(f"Row id: {row_id} Data: {self.rows[row_id]}")

    def get_rows_by_index(self, column_name, value):
        if column_name not in self.index.keys():
            print("Column not present in index")
            return -1
        if value not in self.index[column_name].keys():
            print("Value not present in column")
            return -1
        row_ids = self.index[column_name][value]
        for row_id in row_ids:
            print(f"Row id: {row_id} Data: {self.rows[row_id]}")

    def get_all_rows(self):
        for row_id, row in self.rows.items():
            print(f"Row id: {row_id} Data: {row}")
    
    def update_row(self, row_id, row_data):
        if row_id not in self.rows.keys():
            print(f"Row: {row_id} not in table")
            return -1
        for column in row_data.keys():
            if column not in self.columns_map.keys():
                print(f"{column} column not in row. Aborting.")
                return -1
            if type(row_data[column]) != self.columns_map[column]:
                print(f"Column type mismatch")
                return -1
        self.rows[row_id].update_row(row_data)
        return row_id



class Row:
    def __init__(self, row_data, columns_type):
        self.row_data = row_data
        self.columns_type = columns_type
        self.created_time = datetime.now()
    
    def get_row(self):
        return self.row_data

    def update_row(self, row_data):
        self.row_data = row_data
        return 1
    
    def __repr__(self):
        data = ""
        for key, value in self.row_data.items():
            data += f"{key}: {value}; "
        return data


def run():
    database = Database()
    columns = {'name': str, 'number': int, 'city': str}
    table_id = database.create_table(columns)
    table = database.get_table(table_id)
    row_data = {
        "name": "Harsha",
        "number": 12345,
        "city": "Hyderabad"
    }
    row_id = table.create_row(row_data)
    row_data = {
        "name": "Harsha",
        "city": "Hyderabad"
    }
    table.create_row(row_data)
    table.get_all_rows()
    table.get_row(row_id)
    table.delete_row(row_id)
    table.delete_row(10)

    row_data = {
        "name": "Raj",
        "number": 1345,
        "city": "Hyderabad"
    }
    row_id = table.create_row(row_data)
    row_data = {
        "name": "Harsha",
        "number": 1345,
        "city": "Bangalore"
    }
    table.create_row(row_data)
    table.get_row(row_id)
    table.get_rows_by_index("number", 1345)
    row_data = {
        "number": 118
    }
    table.update_row(row_id, row_data)
    table.get_row(row_id)
    row_data = {
        "number": 200,
        "address": "Bangalore"
    }
    table.update_row(row_id, row_data)
    row_data = {
        "number": "200",
    }
    table.update_row(row_id, row_data)

    table.add_column("country", str)
    

if __name__=='__main__':
    run()