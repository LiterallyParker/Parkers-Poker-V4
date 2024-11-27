const jwt = require("jsonwebtoken");

const verifyJWT = (token) => {
    try {
        // Verify token
        const verifiedToken = jwt.verify(
            token,
            process.env.JWT_SECRET
        );

        // If there isnt an id, token isnt verified.
        if (verifiedToken) {
            return verifiedToken;
        };
        return;

    } catch (error) {
        console.error(Error("Error while verifying JWT."));
        return;
    };
};

module.exports = verifyJWT;