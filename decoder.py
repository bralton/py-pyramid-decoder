def decode(message_file):
    values_from_file = list()
    with open(message_file) as file:
        for line in file:
            lineValues = line.rstrip().split(' ')
            values_from_file.insert(len(values_from_file),(int(lineValues[0]), lineValues[1]))
    sorted_values_from_files = sorted(values_from_file)

    pyramid_line = 1
    current_index=0

    decrypted_message = list()

    while current_index < len(sorted_values_from_files):
        decrypted_message.insert(len(decrypted_message), sorted_values_from_files[current_index][1])
        pyramid_line += 1
        current_index += pyramid_line
    
    return ' '.join(decrypted_message)

print(decode('coding_qual_input.txt'))