```python
# Import necessary libraries
import json
import datetime

class ReportGenerator:
    def __init__(self):
        pass

    def generate_report(self, fact_check_result, bias_detection_result, source_validation_result):
        # Create a dictionary to store the report data
        report_data = {
            'fact_check_result': fact_check_result,
            'bias_detection_result': bias_detection_result,
            'source_validation_result': source_validation_result,
            'timestamp': datetime.datetime.now().isoformat()
        }

        # Convert the dictionary to a JSON string
        report_json = json.dumps(report_data, indent=4)

        # Return the JSON string
        return report_json

    def save_report(self, report_json, filename):
        # Open a file in write mode
        with open(filename, 'w') as file:
            # Write the JSON string to the file
            file.write(report_json)

        # Return a success message
        return f'Report saved to {filename}'
```
