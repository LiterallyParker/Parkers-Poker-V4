const {
    errorResponse,
    errorMessages
} = require("../../util");
const validateType = require("../../util/validateType");

// Pass in the key/value pair of the query/type
const validateQuery = (requiredQueries) => async (req, res, next) => {

    // Initialize invalid query arrays
    const invalidQueries = [];

    // Iterate over required queries
    for (const [query, type] of Object.entries(requiredQueries)) {
        // If the query wasn't supplied
        if (!req.query.hasOwnProperty(query)) {
            // Add it to missing queries
            invalidQueries.push(query);
            // No need to check type
            continue;
        };

        // Check if the query supplied is the type required
        const isValid = validateType(req.query[query], type);

        // If it isn't
        if (!isValid) {
            // Add it to invalid queries
            invalidQueries.push(query);
        };
    };

    // If there are missing or invalid queries
    if (invalidQueries.length > 0) {
        // Error out
        return res.status(400).json(
            errorResponse({
                name: "ValidateQuery",
                message: errorMessages.validateQuery(invalidQueries),
            })
        );
    };
    // Pass
    next();
};

module.exports = validateQuery;