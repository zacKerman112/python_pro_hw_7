import xml.etree.ElementTree as ET


def xml_reader(filename) -> None:
    """an xml reader"""
    try:
        tree = ET.parse(filename)
        root = tree.getroot()

        print("Current goods in the shop:")

        for product in root.findall('product'):
            name = product.find('name').text
            quantity = product.find('quantity').text
            print(f"The name of product: {name}, quantity: {quantity}")

        for product in root.findall('products'):
            name = product.find('name').text
            if name == "Хліб":
                new_quantity = "120"
                quantity = root.find('quantity').text = new_quantity
                print(f"\nThe product {name} has a new quantity: {quantity}")

        with open(filename, "wb") as f:
            tree.write(f, encoding="utf-8", xml_declaration=True)
            print("The changes have been successfully added to the file")

    except FileNotFoundError:
        print("The file hasn`t been found")

    except ET.ParseError:
        print("The parsing issue occurred")

    except Exception:
        print("some issue occurred")
