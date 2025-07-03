package com.example;

import java.io.IOException;
import org.jsoup.Jsoup;
import org.jsoup.nodes.Document;
import org.jsoup.nodes.Element;
import org.jsoup.select.Elements;

public class OfferScraper {
    private static final String URL = "https://www.ica.se/butiker/kvantum/malmo/ica-kvantum-malmborgs-limhamn-1004076/";

    public static void main(String[] args) throws IOException {
        fetchOffers(URL);
    }

    public static void fetchOffers(String url) throws IOException {
        Document doc = Jsoup.connect(url).get();
        // Search the document for elements containing the Swedish word for offers: "erbjud"
        Elements elements = doc.getAllElements().select("*:matchesOwn((?i)erbjud)");
        if (elements.isEmpty()) {
            System.out.println("No offers found. The page layout may have changed.");
            return;
        }
        System.out.println("Offers found:");
        for (Element el : elements) {
            String text = el.text().trim();
            if (!text.isEmpty()) {
                System.out.println("- " + text);
            }
        }
    }
}
