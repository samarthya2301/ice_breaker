import os
import requests
import random

from dotenv import load_dotenv

load_dotenv()

def get_mock():
	mock_url_endpoint = "https://gist.githubusercontent.com/samarthya2301/039dfd60afe3854c665195b5a935edbe/raw/90201b65e20e750a296c95a7699459d92f7509f1/ice_breaker_mock_1.json"
	response = requests.get(
		url=mock_url_endpoint,
		timeout=10
	)
	try:
		return response.json()
	except requests.exceptions.JSONDecodeError:
		return "Not a valid JSON"

def get_scrapin_linkedin(linkedin_profile_url: str):
	url = "https://api.scrapin.io/v1/enrichment/profile"
	payload = {
		"linkedInUrl": linkedin_profile_url
	}
	headers = {
		"x-api-key": os.environ["SCRAPIN_API_KEY"],
		"Content-Type": "application/json"
	}
	response = requests.post(url=url, json=payload, headers=headers)
	try:
		return response.json()
	except requests.exceptions.JSONDecodeError:
		return "Not a valid JSON"

def scrap_linkedin_profile(linkedin_profile_url: str, mock: bool=True) -> dict:
	"""Scrape information from LinkedIn profiles,
	Manually scrape the information from LinkedIn profile"""

	if mock:
		scraped_data = get_mock()
	else:
		scraped_data = get_scrapin_linkedin(linkedin_profile_url)

	scraped_data = dict(scraped_data)
	scraped_data_cleaned = {
		k: v
		for k, v in scraped_data.items() if v not in [None, {}, [], ""]
	}
	print(f"Reduced characters from {len(str(scraped_data))} to {len(str(scraped_data_cleaned))}")

	return scraped_data_cleaned

if __name__ == "__main__":
	pass