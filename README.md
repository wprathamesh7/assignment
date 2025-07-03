# Getting Started

This is sample project created for demo purpose of demonstrating spring boot capcability with H2 inmemory database.
The API is exposed via Swagger.

Java 1.8 is used for project compilation

### Reference Documentation

Swagger documentation is available on
http://localhost:8080/swagger-ui.html#!/employee-controller

## ICA Offers Scraper

A simple Python script (`ica_offers_scraper.py`) is included to fetch the latest offers from the ICA Kvantum Malmborgs Limhamn store page. The script requires `requests` and `beautifulsoup4`.

Install the dependencies and run the script:

```bash
pip install requests beautifulsoup4
python ica_offers_scraper.py
```

The script will print any detected offers or discounts. If no data is printed, the page structure may have changed.

## Java Offer Scraper

You can also run a simple Java program that fetches the same ICA page using [jsoup](https://jsoup.org/).

Compile and execute using Maven:

```bash
./mvnw -q -DskipTests package
java -cp target/springboot2-jpa-crud-example-0.0.1-SNAPSHOT.jar com.example.OfferScraper
```

The output will list any text snippets containing the Swedish word for offers ("erbjud").
