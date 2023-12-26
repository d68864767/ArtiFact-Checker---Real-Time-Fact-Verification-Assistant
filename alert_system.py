```python
# Import necessary libraries
import requests
import json

class AlertSystem:
    def __init__(self):
        # Initialize the alert system
        self.alerts = {}

    def set_alert(self, topic):
        # Set an alert for a specific topic
        self.alerts[topic] = True

    def check_alerts(self):
        # Check all alerts and send notifications if necessary
        for topic in self.alerts:
            if self.alerts[topic]:
                self.send_notification(topic)

    def send_notification(self, topic):
        # Send a notification about a specific topic
        # This is a placeholder function. In a real-world application, you would use
        # a service like Twilio, SendGrid, or a custom email server to send the notification.
        print(f'Notification sent for topic: {topic}')

    def remove_alert(self, topic):
        # Remove an alert for a specific topic
        if topic in self.alerts:
            del self.alerts[topic]
```
