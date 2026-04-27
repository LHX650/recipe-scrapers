from recipe_scrapers import scrape_me

url = "https://www.allrecipes.com/recipe/24074/alysias-basic-meat-lasagna/"

scraper = scrape_me(url)

print("标题:", scraper.title())
print("配料:", scraper.ingredients())
