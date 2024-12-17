import csv
from faker import Faker

def create_fixed_width_file(filename, num_rows=10):
    fake = Faker()
    
    # Define the field widths (Offsets from the spec)
    field_widths = [5, 12, 3, 2, 13, 7, 10, 13, 20, 13]
    
    try:

        # Open the file in the specified encoding (Windows-1252)
        with open(filename, "w", encoding="windows-1252") as f:
            for _ in range(num_rows):
                # Generating data using Faker
                name = fake.first_name()
                last_name = fake.last_name()
                age = str(fake.random_int(min=18, max=80))
                gender = fake.random_element(elements=("M", "F"))
                occupation = fake.job()[:13]
                city = fake.city()[:7]
                phone = fake.phone_number()[:10]
                email = fake.email()[:13]
                address = fake.city()[:20]
                postal_code = fake.zipcode()

                # Combine the generated fields into a single row
                row = [name, last_name, age, gender, occupation, city, phone, email, address, postal_code]
                
                # Create a fixed-width line for each row
                line = ""
                for i in range(len(row)):
                    field = str(row[i])
                    line += field.ljust(field_widths[i])
                f.write(line + "\n")
            print("File has been created successfully")
    except:
        print("There is a problem while creating a file")

            
def parse_fixed_width_file(input_filename, output_filename):
    # Offsets from the spec
    field_widths = [5, 12, 3, 2, 13, 7, 10, 13, 20, 13]
    
    # Column names from the spec
    column_names = ["f1", "f2", "f3", "f4", "f5", "f6", "f7", "f8", "f9", "f10"]
    
    try:
        # Opening the file (Windows-1252 encoding) and the CSV file with UTF-8 Encoding
        with open(input_filename, "r", encoding="windows-1252") as infile, open(output_filename, "w", newline="", encoding="utf-8") as outfile:
            writer = csv.DictWriter(outfile, fieldnames=column_names)
            writer.writeheader()
            
            # Reading File
            for line in infile:
                fields = []
                start = 0
                for width in field_widths:
                    field = line[start:start + width].strip()
                    fields.append(field)
                    start += width
                
                # Creating dictionary
                row_dict = {}
                for i in range(len(column_names)):
                    row_dict[column_names[i]] = fields[i]
                
                # Writting Data
                writer.writerow(row_dict)
            print("CSV File has been created Successfully")
    except:
        print("There is probelm while creating CSV File")


#n=int(input("Please enter No of rows for the input file: "))
#hding above line to run code in docker without any intervention
n=300
create_fixed_width_file("input_file.txt",n)
parse_fixed_width_file("input_file.txt", "output_file.csv")




