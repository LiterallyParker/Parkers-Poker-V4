const { verifyJWT } = require('../../auth');
const { User } = require('../../models');
const {
    errorResponse,
    errorMessages,
} = require("../../util");

const setUser = async (req, res, next) => {
    // Initialize Bearer prefix
    const prefix = 'Bearer ';
    // Grab authorization header
    const auth = req.header('Authorization');
    // If no auth header is present
    if (!auth) {
        // Pass
        return next();
    };
    // If it's a Bearer token
    if (auth.startsWith(prefix)) {
        // Slice off "Bearer "
        const token = auth.slice(prefix.length);

        // If blank
        if (!token) {
            // Pass
            return next();
        };

        try {

            // Verify token
            const verifiedToken = verifyJWT(token);

            // If it's real
            if (verifiedToken) {
                // Attach 'em
                req.user = await User.findByPk(verifiedToken.id, {
                    attributes: {
                        exclude: ['hash']
                    }
                });
            };
            // Pass
            return next();

        } catch (error) {
            console.error("Error Attaching user to request:", error);
            return res.status(500).json(
                errorResponse({
                    name: "SetUser",
                    message: errorMessages.setUser
                })
            );
        };

    };

    // Uh oh! no bears!
    return res.status(401).json(
        errorResponse({
            name: "SetUser",
            message: errorMessages.authToken(prefix)
        })
    );

};

module.exports = setUser;