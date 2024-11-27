// Init
require('dotenv').config();
const express = require('express');
const app = express();
const db = require('./models');

const {
    errorResponse,
    errorMessages
} = require('./util');

// Security
const helmet = require('helmet');
app.use(helmet());
const cors = require('cors');
app.use(cors());

// Global Rate Limit
const { globalLimiter } = require("./middleware/rate_limiters");
app.use(globalLimiter);

// Formatting
app.use(express.json());

// Authentication
const { setUser } = require('./middleware/users');
app.use(setUser);

// Api
const apiRoutes = require('./routes');
app.use('/api', apiRoutes);

// False route handling
app.use('*', (req, res) => {
    return res.status(404).json(
        errorResponse({
            name: "Server",
            message: errorMessages.unknownRoute
        })
    );
});

// Error handling
app.use((error, req, res, next) => {
    console.error(error);
    return res.status(500).json(
        errorResponse({
            name: "Server",
            message: errorMessages.server
        })
    );
});

// Start
const PORT = process.env.PORT || 8080;
db.sequelize.sync().then(() => {
    app.listen(PORT, () => {
        console.log(`Server is running on port ${PORT}`);
    });
}).catch((error) => {
    console.error("Error starting server:", error);
});
