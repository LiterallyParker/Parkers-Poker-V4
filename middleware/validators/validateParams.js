const {
    errorResponse,
    errorMessages
} = require("../../util");
const validateType = require("../../util/validateType");

// Pass in the key/value pair of the param/type
const validateParams = (requiredParams) => async (req, res, next) => {

    // Initialize invalid param arrays
    const invalidParams = [];

    // Iterate over required params
    for (const [param, type] of Object.entries(requiredParams)) {
        // If the param wasn't supplied
        if (!req.params.hasOwnProperty(param)) {
            // Add it to missing params
            invalidParams.push(param);
            // No need to check type
            continue;
        };

        // Check if the param supplied is the type required
        const isValid = validateType(req.params[param], type);
        
        // If it isn't
        if (!isValid) {
            // Add it to invalid params
            invalidParams.push(param);
        };
    };

    // If there are missing or invalid params
    if (invalidParams.length > 0) {
        // Error out
        return res.status(400).json(
            errorResponse({
                name: "ValidateParams",
                message: errorMessages.validateParams(invalidParams),
            })
        );
    };
    // Pass
    next();
};

module.exports = validateParams;