const express = require('express');
const bodyParser = require('body-parser');
const cors = require('cors');
const helmet = require('helmet');
const morgan = require('morgan');
const dotenv = require('dotenv');

// Load environment variables from .env file
dotenv.config();

const app = express();

// Enhance your app security with Helmet
app.use(helmet());

// Use bodyParser to parse JSON bodies into JS objects
app.use(bodyParser.json());

// Enable all CORS requests
app.use(cors());

// Adding morgan to log HTTP requests
app.use(morgan('combined'));

// Health Check Endpoint
app.get('/health', (req, res) => {
    res.status(200).send('OK');
});

// Catch 404 and forward to error handler
app.use((req, res, next) => {
    const err = new Error('Not Found');
    err.status = 404;
    next(err);
});

// Error Handler
app.use((err, req, res, next) => {
    res.status(err.status || 500).json({
        error: {
            message: err.message || 'Internal Server Error'
        }
    });
});

// Starting the server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server running on port ${PORT}`);
});

module.exports = app;
