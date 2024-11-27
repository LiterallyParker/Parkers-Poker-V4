const rateLimit = require('express-rate-limit');
const { errorMessages } = require('../../util');

const globalLimiter = rateLimit({
    windowMs: 15 * 60 * 1000, // 15 minutes
    max: 100, // 100 requests
    keyGenerator: (req) => req.user ? req.user.id : req.ip, // Base on user if logged in, IP if not.
    message: errorMessages.tooManyRequests,
    standardHeaders: true, // Return rate limit info in the `RateLimit-*`
    legacyHeaders: false, // Disable `X-RateLimit-*` headers
});

module.exports = globalLimiter;