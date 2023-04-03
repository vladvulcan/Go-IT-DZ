import csv


def write_contacts_to_file(filename, contacts):
    with open(filename, 'w', newline='') as fh:
        field_names = ["name", "email", "phone", "favorite"]
        writer = csv.DictWriter(fh, fieldnames=field_names)
        writer.writeheader()
        for contact in contacts:
            writer.writerow({"name": contact["name"], "email":contact["email"], "phone": contact["phone"], "favorite":contact["favorite"]})

def read_contacts_from_file(filename):
    with open(filename, 'r', newline='') as fh:
        list = []
        reader = csv.DictReader(fh)
        for row in reader:
            if row['favorite'] == 'True':
                row['favorite'] = True
            if row['favorite'] == 'False':
                row['favorite'] = False
            list.append(row)
        return list