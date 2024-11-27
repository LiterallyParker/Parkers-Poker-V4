const crypto = require("crypto");

const generateEmailToken = () => {
    return crypto.randomBytes(32).toString('hex');
};

module.exports = generateEmailToken;