def read_binary_file_hex(file_path):
    with open(file_path, 'rb') as binary_file:
        binary_content = binary_file.read()
        hex_values = [format(byte, '02X') for byte in binary_content]
        return hex_values

def format_in_columns(hex_values, columns=16):
    formatted_output = [hex_values[i:i+columns] for i in range(0, len(hex_values), columns)]
    return formatted_output

def extract_values_at_row_and_columns(formatted_output, row_number, columns_to_extract):
    extracted_values = [formatted_output[row_number-1][col-1] for col in columns_to_extract]
    return extracted_values

def show_values_at_row_and_columns(formatted_output, row_number, columns_to_show):
    values_to_show = [formatted_output[row_number-1][col-1] for col in columns_to_show]
    print(f"\nWartości z kolumn {', '.join(map(str, columns_to_show))} w wierszu {row_number}: {values_to_show}")
    return values_to_show

def convert_hex_values(values, conversion_key):
    converted_values = [conversion_key.get(value, value) for value in values]
    return converted_values

file_path = '/home/gabriel/Dokumenty/PIN1865 cim1.bin'
hex_values = read_binary_file_hex(file_path)
formatted_output = format_in_columns(hex_values)

#for i, row in enumerate(formatted_output, start=1):
    #print(f"{i:4}: {row}")

row_number_to_extract = 102
columns_to_extract = [10, 12, 14, 16]
extracted_values = extract_values_at_row_and_columns(formatted_output, row_number_to_extract, columns_to_extract)

#print(f"\nWartości z kolumn 10, 12, 14, 16 w wierszu {row_number_to_extract}: {extracted_values}")


columns_to_show = [10, 12, 14, 16]
converted_values = convert_hex_values(extracted_values, {'03': 1, '48': 2, '5F': 3, '65': 4, '72': 5, '39': 6, '2E': 7, 'D1': 8, 'C6': 9, '14': 0})
print("                      ")
print("-------------------------------------")
print(">>> OPEL CIM 95160 CALCULATOR 1.0 <<<")
print("-------------------------------------")
print("                      ")
print("    --------------------------")
print(f"       PIN CODE: {converted_values}")
print("    --------------------------")
print("                      ")
print("                      ")


#/home/gabriel/Dokumenty/PIN1865 cim1.bin