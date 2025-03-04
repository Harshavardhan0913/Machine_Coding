class Database:
    def __init__(self):
        self.tables = {}
        self.table_id = 1
        pass

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
    def __init__(self, columns=[]):
        self.rows = {}
        self.row_id = 1
        self.columns = columns

    def add_column(self, column):
        if column in self.columns:
            print(f"{column} column already in table")
            return -1
        self.columns.append(column)
        return 1

    def delete_column(self, column):
        if column not in self.columns:
            print(f"{column} column not in table")
            return -1
        idx = self.columns.index(column)
        self.columns.pop(idx)
        return 1

    def create_row(self, row_data: dict):
        if not row_data:
            print("Row is empty")
            return -1
        for column in row_data.keys():
            if column not in self.columns:
                print(f"{column} column not in row. Aborting.")
                return -1
        self.rows[self.row_id] = Row(row_data)
        row_id = self.row_id
        self.row_id += 1
        print("Successfully created row")
        return row_id

    def delete_row(self, row_id):
        if row_id not in self.rows.keys():
            print(f"Row id: {row_id} not in Table")
            return -1
        del self.rows[row_id]
        print(f"Successfully deleted row: {row_id}")
        return 1
    
    def get_row(self, row_id):
        if row_id not in self.rows:
            print(f" Row :{row_id} not in Table")
            return -1
        return self.rows[row_id]

    def get_all_rows(self):
        return self.rows
    
    def update_row(self, row_id, row_data):
        if row_id not in self.rows.keys():
            print(f"Row: {row_id} not in table")
            return -1
        for column in row_data.keys():
            if column not in self.columns:
                print(f"{column} column not in row. Aborting.")
                return -1
        self.rows[row_id].update_row(row_data)
        return row_id



class Row:
    def __init__(self, row_data):
        self.row_data = row_data
    
    def update_row(self, row_data):
        for column, value in row_data.items():
            self.row_data[column] = value
    
    def __repr__(self):
        data = ""
        for key, value in self.row_data.items():
            data += f"{key}: {value}; "
        return data


def run():
    database = Database()
    columns = ['name', 'number', 'city']
    table_id = database.create_table(columns)
    table = database.get_table(table_id)
    row_data = {
        "name": "Harsha",
        "number": 12345,
        "city": "Hyderabad"
    }
    row_id = table.create_row(row_data)
    print(table.get_all_rows())
    print(table.get_row(row_id))
    table.delete_row(row_id)
    table.delete_row(10)

    row_data = {
        "name": "Raj",
        "number": 1345,
        "city": "Hyderabad"
    }
    row_id = table.create_row(row_data)
    print(table.get_row(row_id))
    row_data = {
        "number": 118
    }
    table.update_row(row_id, row_data)
    print(table.get_row(row_id))
    row_data = {
        "number": 200,
        "address": "Bangalore"
    }
    table.update_row(row_id, row_data)
    

if __name__=='__main__':
    run()