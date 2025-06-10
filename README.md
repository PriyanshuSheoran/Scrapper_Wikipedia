Actor Scraper Project
This project scrapes information about Chinese and Indian actors from Wikipedia and saves the data to a CSV file.

Project Overview
The script:

Accesses Wikipedia pages listing Chinese and Indian actors

Extracts information about the first 5 actors from each list

Gathers details including birth information, occupation, and education

Stores the collected data in a structured CSV file

Features
Web scraping using BeautifulSoup and requests

Data extraction from Wikipedia infoboxes

CSV output generation

Handling of missing data fields

Requirements
Python 3.x

Required packages:

requests

beautifulsoup4

pytest (for testing)

Installation
Clone the repository:

bash
git clone https://github.com/yourusername/actor-scraper.git
cd actor-scraper
Install the required packages:

bash
pip install -r requirements.txt
Usage
Run the main script:

bash
python actors_scraper.py
This will:

Scrape actor data from Wikipedia

Display the collected information in the console

Save the data to actors_data.csv

File Structure
text
actor-scraper/
├── scraper1.py       # Main scraping script
├── test_actors_scraper.py  # Test script
├── actors_data.csv         # Output file (generated after running)
├── README.md               # This file

Testing
To run the tests:

bash
pytest test_actors_scraper.py -v
The test suite includes:

URL accessibility checks

HTML parsing tests

CSV output validation

Data structure verification

Mocked request tests

Output Example
The CSV file will contain data in this format:

csv
Country,Name,Born,Occupation,Education
China,Jackie Chan,7 April 1954 (age 69),Actor, martial artist, film producer...,Not available
India,Amitabh Bachchan,11 October 1942 (age 80),Actor, film producer, television host...,Not available
Limitations
The script only scrapes the first 5 actors from each list

Some information might be missing ("Not available") if not present in Wikipedia infobox

Wikipedia's structure might change, requiring updates to the scraping logic

Contributing
Contributions are welcome! Please open an issue or submit a pull request for any improvements.

License
This project is licensed under the MIT License.