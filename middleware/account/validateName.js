const { errorResponse, errorMessages } = require("../../util");

const validateName = async (req, res, next) => {
    if (req?.user) {
        const { firstname, lastname } = req.body;
        const errors = [];

        if (firstname && firstname === req.user.firstname) {
            errors.push(errorMessages.sameFirstname);
        };
        if (lastname && lastname === req.user.lastname) {
            errors.push(errorMessages.sameLastname);
        };
        if (errors.length > 0) {
            return res.status(400).json(
                errorResponse({
                    name: "UpdateName",
                    message: errors.join("; ")
                })
            );
        };
    }
    return next();
};

module.exports = validateName;