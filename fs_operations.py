import json


def json_file_operation(file_name, operation, data=None, index=None):
    try:
        if operation == 'read':
            with open(file_name, 'r') as file:
                return json.load(file)

        elif operation == 'write':
            with open(file_name, 'w') as file:
                json.dump(data, file)
                print(f'Appended {len(data)} lines to {file_name}')

        elif operation == 'delete':
            with open(file_name, 'r') as file:
                data = json.load(file)
                print(type(data))
                if index is not None and index < len(data):
                    data = [item for item in data if item != index]
                else:
                    print(f'Error: Index {index} out of range for file: {file_name}')
            with open(file_name, 'w') as file:
                json.dump(data, file)
                print(f'Removed any and all occurrences of value: {index} from file: {file_name}')

    except FileNotFoundError:
        if operation == 'write' and data is not None:
            print(f'File {file_name} not found, creating a new one and adding {len(data)} lines')
            with open(file_name, 'w') as file:
                json.dump(data, file)
                print(f'Appended {len(data)} lines to {file_name}')
        else:
            print(f'Error: {file_name} not found, creating a new one')
    except json.JSONDecodeError:
        print(f'Error: Invalid JSON format in file: {file_name}')


def write_to_file(data, file_name):
    try:
        current_data = json_file_operation(file_name, 'read')
        if current_data is None:
            current_data = []
        current_data.extend(data)
        json_file_operation(file_name, 'write', data=current_data)
    except FileNotFoundError:
        print(f'Error: {file_name} not found, creating new one and adding {len(data)} lines')
        json_file_operation(file_name, 'write', data=data)


def read_from_file(file_name):
    return json_file_operation(file_name, 'read')


def delete_from_file(value, file_name):
    json_file_operation(file_name, 'delete', index=value)
