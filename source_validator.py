```python
# Import necessary libraries
import requests
from bs4 import BeautifulSoup

class SourceValidator:
    def __init__(self):
        # List of trusted sources
        self.trusted_sources = ['https://www.bbc.com', 'https://www.reuters.com', 'https://www.apnews.com']

    def validate(self, source):
        # Check if the source is in the list of trusted sources
        if source in self.trusted_sources:
            return {
                'source': source,
                'validity': 'Trusted'
            }
        else:
            # If the source is not in the list of trusted sources, check if it's a valid website
            try:
                response = requests.get(source)
                if response.status_code == 200:
                    return {
                        'source': source,
                        'validity': 'Unknown'
                    }
                else:
                    return {
                        'source': source,
                        'validity': 'Invalid'
                    }
            except:
                return {
                    'source': source,
                    'validity': 'Invalid'
                }

    def add_trusted_source(self, source):
        # Add a new source to the list of trusted sources
        self.trusted_sources.append(source)
```
