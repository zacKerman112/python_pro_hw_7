import xml.etree.ElementTree as ET


def xml_reader(filename: str) -> None:
    """A function for reading and updating product information in an XML file."""
    try:
        tree = ET.parse(filename)
        root = tree.getroot()

        print("Current goods in the shop:")

        for product in root.findall('product'):
            name_elem = product.find('name')
            quantity_elem = product.find('quantity')

            if name_elem is not None and quantity_elem is not None:
                print(f"The name of product: {name_elem.text}, quantity: {quantity_elem.text}")

        for product in root.findall('product'):
            name_elem = product.find('name')
            if name_elem is not None and name_elem.text == "Хліб":
                new_quantity = "120"
                quantity_elem = product.find('quantity')
                if quantity_elem is not None:
                    quantity_elem.text = new_quantity
                    print(f"\nThe product {name_elem.text} has a new quantity: {new_quantity}")

        tree.write(filename, encoding="utf-8", xml_declaration=True)
        print("The changes have been successfully added to the file")

    except FileNotFoundError:
        print("The file hasn't been found")
    except ET.ParseError:
        print("The parsing issue occurred")
    except Exception as e:
        print(f"Some issue occurred: {e}")


if __name__ == "__main__":
    xml_reader('products.xml')