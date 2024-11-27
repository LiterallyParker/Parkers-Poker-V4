require('dotenv').config()
const jwt = require("jsonwebtoken");

const generateJWT = (payload) => {
    try {

        const token = jwt.sign(payload, process.env.JWT_SECRET, { expiresIn: '1w' });

        return token;
        
    } catch (error) {
        console.error(error);
        return null;
    };
};

module.exports = generateJWT;