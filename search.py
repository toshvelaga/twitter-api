import requests
import constants

# Possible approach to search for tweets: use twitter search API, scrape twitter data, or use twitter streams 
# and then use the data to send DMs

keywords = "sales outreach"
access_token = ""
headers = {"Authorization": f"Bearer {access_token}"}

results = requests.get(constants.SEARCH_BASE_URL + keywords + "&max_results=100", headers=headers)

print(results.text)


