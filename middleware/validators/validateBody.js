const {
    errorResponse,
    errorMessages
} = require("../../util");
const validateType = require("../../util/validateType");

// Pass in the key/value pair of the field/type
const validateBody = (requiredFields) => async (req, res, next) => {

    // Initialize invalid field arrays
    const invalidFields = [];

    // Iterate over required fields
    for (const [field, type] of Object.entries(requiredFields)) {
        // If the field wasn't supplied
        if (!req.body.hasOwnProperty(field)) {
            // Add it to missing fields
            invalidFields.push(field);
            // No need to check type
            continue;
        };
        
        // Check if the field supplied is the type required
        const isValid = validateType(req.body[field], type);

        // If it isn't
        if (!isValid) {
            // Add it to invalid fields
            invalidFields.push(field);
        };
    };

    // If there are missing or invalid fields
    if (invalidFields.length > 0) {
        // Error out
        return res.status(400).json(
            errorResponse({
                name: "ValidateBody",
                message: errorMessages.validateBody(invalidFields)
            })
        );
    };
    // Pass
    next();
};

module.exports = validateBody;