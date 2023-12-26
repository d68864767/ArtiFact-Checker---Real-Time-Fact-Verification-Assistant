const express = require('express');
const bodyParser = require('body-parser');
const cors = require('cors');
const axios = require('axios');

const FactCheckerComponent = require('./FactCheckerComponent');
const BiasDetectorComponent = require('./BiasDetectorComponent');
const SourceValidatorComponent = require('./SourceValidatorComponent');
const AlertSystemComponent = require('./AlertSystemComponent');
const ReportGeneratorComponent = require('./ReportGeneratorComponent');

const app = express();

app.use(cors());
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));

app.post('/fact-check', async (req, res) => {
  const factCheckResult = await FactCheckerComponent.checkFact(req.body.text);
  res.json(factCheckResult);
});

app.post('/detect-bias', async (req, res) => {
  const biasDetectionResult = await BiasDetectorComponent.detectBias(req.body.text);
  res.json(biasDetectionResult);
});

app.post('/validate-source', async (req, res) => {
  const sourceValidationResult = await SourceValidatorComponent.validateSource(req.body.source);
  res.json(sourceValidationResult);
});

app.post('/generate-alert', async (req, res) => {
  const alertGenerationResult = await AlertSystemComponent.generateAlert(req.body.topic);
  res.json(alertGenerationResult);
});

app.post('/generate-report', async (req, res) => {
  const reportGenerationResult = await ReportGeneratorComponent.generateReport(req.body.text);
  res.json(reportGenerationResult);
});

const PORT = process.env.PORT || 5000;

app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});

module.exports = app;
