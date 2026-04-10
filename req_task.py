import requests


def save_page_to_file(url: str, filename: str) -> None:
    """A function that saves the HTML content of a page to a file."""
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        with open(filename, "w", encoding="utf-8") as file:
            file.write(response.text)

        print(f"The page has been saved successfully and saved to {filename}")

    except requests.exceptions.HTTPError as http_err:
        print(f"An HTTP error: {http_err}")
    except requests.exceptions.ConnectionError as conn_err:
        print(f"A connection error: {conn_err}")
    except requests.exceptions.Timeout:
        print("The time has run out")
    except Exception as error:
        print(f"An error found: {error}")


if __name__ == "__main__":
    target_url = (
        "https://www.youtube.com/watch?v=dQw4w9WgXcQ&list=RDdQw4w9"
        "WgXcQ&start_radio=1"
    )
    output_file = "page_content.txt"

    save_page_to_file(target_url, output_file)