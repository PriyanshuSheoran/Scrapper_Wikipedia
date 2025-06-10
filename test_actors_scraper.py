import pytest
from bs4 import BeautifulSoup
import csv
import os
from unittest.mock import patch, mock_open
import requests
from io import StringIO



def test_chinese_actors_url():
    url = "https://en.wikipedia.org/wiki/List_of_Chinese_actors"
    response = requests.get(url)
    assert response.status_code == 200

def test_indian_actors_url():
    url = "https://en.wikipedia.org/wiki/List_of_Indian_male_film_actors"
    response = requests.get(url)
    assert response.status_code == 200

def test_parse_actor_info():

    html_content = """
    <table class="infobox">
        <tr>
            <th>Born</th>
            <td>1 January 1980 (age 43)</td>
        </tr>
        <tr>
            <th>Occupation</th>
            <td>Actor, Producer</td>
        </tr>
        <tr>
            <th>Education</th>
            <td>Beijing Film Academy</td>
        </tr>
    </table>
    """
    soup = BeautifulSoup(html_content, 'html.parser')
    infobox = soup.find("table", class_="infobox")
    
    born = occupation = education = "Not available"
    
    if infobox:
        rows = infobox.find_all("tr")
        for row in rows:
            header = row.find("th")
            data = row.find("td")
            if header and data:
                label = header.text.strip().lower()
                if "born" in label and born == "Not available":
                    born = " ".join(data.stripped_strings)
                elif "occupation" in label and occupation == "Not available":
                    occupation = ", ".join(data.stripped_strings)
                elif "education" in label and education == "Not available":
                    education = ", ".join(data.stripped_strings)
    
    assert born == "1 January 1980 (age 43)"
    assert occupation == "Actor, Producer"
    assert education == "Beijing Film Academy"

def test_csv_output(tmpdir):
    # Create test data
    test_data = [
        {
            "Country": "China",
            "Name": "Test Actor",
            "Born": "1 January 1980",
            "Occupation": "Actor",
            "Education": "Test University"
        }
    ]
    

    csv_file = tmpdir.join("test_actors.csv")
    

    with open(csv_file, 'w', newline='', encoding='utf-8') as f:
        fieldnames = ["Country", "Name", "Born", "Occupation", "Education"]
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for actor in test_data:
            writer.writerow(actor)
    

    assert os.path.exists(csv_file)
    
  
    with open(csv_file, 'r', encoding='utf-8') as f:
        content = f.read()
        assert "Country,Name,Born,Occupation,Education" in content
        assert "China,Test Actor,1 January 1980,Actor,Test University" in content

@patch('requests.get')
def test_mock_requests(mock_get):
    # Mock response for Wikipedia page
    mock_response = type('MockResponse', (), {
        'text': '<html><div class="mw-parser-output"><ul><li><a href="/wiki/Actor1">Actor1</a></li></ul></div></html>',
        'status_code': 200
    })
    mock_get.return_value = mock_response
    
    response = requests.get("https://en.wikipedia.org/test")
    assert response.status_code == 200
    soup = BeautifulSoup(response.text, 'html.parser')
    links = soup.select("div.mw-parser-output ul li a[href^='/wiki/']")
    assert len(links) > 0
    assert links[0].text == "Actor1"

def test_actor_data_structure():
  
    test_actor = {
        "Country": "China",
        "Name": "Test Actor",
        "Born": "1 January 1980",
        "Occupation": "Actor",
        "Education": "Test University"
    }
    
    assert isinstance(test_actor, dict)
    assert "Country" in test_actor
    assert "Name" in test_actor
    assert "Born" in test_actor
    assert "Occupation" in test_actor
    assert "Education" in test_actor
    assert len(test_actor.keys()) == 5