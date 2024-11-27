const {
    errorResponse,
    errorMessages
} = require("../../util");

const requireUser = async (req, res, next) => {
    // If the user isn't attached to the request
    if (!req.user) {
        // Error out
        return res.status(401).json(
            errorResponse({
                name: "RequireUser",
                message: errorMessages.notLoggedIn
            })
        );
    };
    // Pass
    next();
};

module.exports = requireUser;