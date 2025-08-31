from bs4 import BeautifulSoup

def scrape_data(html_content: str) -> list:
    """
    Simulates web scraping. It takes HTML content as a string, parses it using BeautifulSoup,
    and extracts job descriptions. In a real application, this would make an HTTP request to a URL.

    Args:
        html_content(str): A string containing the HTML to parse.
    Returns:
        list: A list of strings, where each string is a job description
    """
    soup = BeautifulSoup(html_content, 'html.parser')
    descriptions = [desc.get_text() for desc in soup.find_all(class_='job-description')]
    return descriptions