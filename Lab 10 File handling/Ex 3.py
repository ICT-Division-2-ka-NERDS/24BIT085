# Program to create a vCard from user input

def create_vcard():
    # Accept user details
    name = input("Enter full name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email address: ")
    address = input("Enter address: ")

    # Create vCard content
    vcard_content = f"""BEGIN:VCARD
VERSION:3.0
FN:{name}
TEL;TYPE=CELL:{phone}
EMAIL:{email}
ADR;TYPE=HOME:{address}
END:VCARD"""

    # Save vCard to a file
    with open("contact.vcf", "w") as vcard_file:
        vcard_file.write(vcard_content)

    print("vCard created successfully as 'contact.vcf'.")

# Call the function
create_vcard()