import requests
from bs4 import BeautifulSoup

URL = "https://www.ica.se/butiker/kvantum/malmo/ica-kvantum-malmborgs-limhamn-1004076/"


def fetch_offers(url: str = URL):
    """Fetch the offers from the ICA store page and return a list of offers."""
    response = requests.get(url)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, "html.parser")

    # ICA's pages usually include an "Erbjudanden" (Offers) section with
    # items in <li> elements. The exact CSS classes may vary so this script
    # uses a broad search for commonly used words.
    offer_elements = soup.find_all(string=lambda s: s and "erbjud" in s.lower())

    offers = []
    for elem in offer_elements:
        # Extract a short snippet around each element to serve as the offer text.
        parent = elem.parent.get_text(separator=" ", strip=True)
        if parent not in offers:
            offers.append(parent)
    return offers


if __name__ == "__main__":
    offers = fetch_offers()
    if not offers:
        print("No offers found. The page layout may have changed.")
    else:
        print("Offers found:")
        for offer in offers:
            print(f"- {offer}")
