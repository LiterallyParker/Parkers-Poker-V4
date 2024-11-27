const rateLimit = require('express-rate-limit');
const { errorMessages } = require('../../util');

const registerLimiter = rateLimit({
    windowMs: 15 * 60 * 1000, // 15 minutes
    max: 10, // 10 requests
    keyGenerator: (req) => req.ip,
    message: errorMessages.tooManyRequests,
    standardHeaders: true,
    legacyHeaders: false,
});

module.exports = registerLimiter