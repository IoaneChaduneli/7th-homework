import sys, csv

def define_argument(argument):
    if len(argument) < 3: 
        sys.exit('Too few arguments are passed')
    if len(argument) > 3:
        sys.exit('Too much arguments are passed')
    
    if argument[1].split('.')[1] != 'csv':
        sys.exit('Not a Csv file')
    

def main(argument):
    define_argument(argument)
    with open(argument[1], 'r') as csv_file:
        reader = csv.DictReader(csv_file)
        with open(argument[2], 'w', newline='') as new_csv:
            fieldnames = ['first', 'last', 'house']
            writer = csv.DictWriter(new_csv, fieldnames=fieldnames)
            writer.writeheader()

        for element in reader:
            new_dict = {}
            name_parts = element['name'].split(',')
            name_parts.append(element['house'])

            first_name = name_parts[0].strip()
            last_name = name_parts[1].strip()
            house = name_parts[2].strip()

            new_dict['first'] = first_name
            new_dict['last'] = last_name
            new_dict['house'] = house
            writer.writerow(new_dict)


if __name__ == '__main__':
    main(sys.argv)