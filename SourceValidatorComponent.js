```javascript
const axios = require('axios');

class SourceValidatorComponent {
    constructor() {
        // List of trusted sources
        this.trusted_sources = ['https://www.bbc.com', 'https://www.reuters.com', 'https://www.apnews.com'];
    }

    async validateSource(source) {
        // Check if the source is in the list of trusted sources
        if (this.trusted_sources.includes(source)) {
            return {
                'source': source,
                'validity': 'Trusted'
            };
        } else {
            // If the source is not in the list of trusted sources, check if it's a valid website
            try {
                const response = await axios.get(source);
                if (response.status === 200) {
                    return {
                        'source': source,
                        'validity': 'Unknown'
                    };
                } else {
                    return {
                        'source': source,
                        'validity': 'Invalid'
                    };
                }
            } catch (error) {
                return {
                    'source': source,
                    'validity': 'Invalid'
                };
            }
        }
    }

    addTrustedSource(source) {
        // Add a new source to the list of trusted sources
        this.trusted_sources.push(source);
    }
}

module.exports = SourceValidatorComponent;
```
