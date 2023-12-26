```python
# Import necessary libraries
from pymongo import MongoClient

class Database:
    def __init__(self):
        # Initialize MongoDB client
        self.client = MongoClient('mongodb://localhost:27017/')
        # Create or access the database
        self.db = self.client['artifact_checker_db']
        # Create or access the collections
        self.fact_checks = self.db['fact_checks']
        self.reports = self.db['reports']

    def save_fact_check(self, fact_check_result):
        # Save the fact check result to the database
        self.fact_checks.insert_one(fact_check_result)
        return 'Fact check result saved to database'

    def get_fact_check(self, fact):
        # Retrieve a fact check result from the database
        result = self.fact_checks.find_one({'fact': fact})
        return result

    def save_report(self, report_json):
        # Save the report to the database
        self.reports.insert_one(report_json)
        return 'Report saved to database'

    def get_report(self, timestamp):
        # Retrieve a report from the database
        result = self.reports.find_one({'timestamp': timestamp})
        return result
```
