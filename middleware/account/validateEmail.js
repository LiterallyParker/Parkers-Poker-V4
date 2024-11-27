const { User } = require('../../models');
const { emailRegex } = require("../../email/verification");
const {
    errorResponse,
    errorMessages
} = require("../../util");
const { Op } = require('sequelize');

const validateEmail = async (req, res, next) => {
    const { requestedEmail, confirmedEmail, ...rest } = req.body;

    if (requestedEmail !== confirmedEmail) {
        return res.status(400).json(
            errorResponse({
                name: "ValidateEmail",
                message: errorMessages.emailMismatch
            })
        );
    };

    if (!emailRegex(requestedEmail)) {
        return res.status(400).json(
            errorResponse({
                name: "ValidateEmail",
                message: errorMessages.invalidEmail
            })
        );
    };

    try {
        // If the user is logged in
        let id = null;
        if (req.user) {
            // Grab id
            id = req.user.id;
        };
        // Find an existring email
        const existingUser = await User.findOne({
            where: {
                email: requestedEmail,
                id: { [Op.ne]: id } // Exclude potential logged in user, this is checked later during email update process
            },
            attributes: ['id', 'email']
        });

        // If there is a user
        if (existingUser) {
            // Error out
            return res.status(400).json(
                errorResponse({
                    name: "ValidateEmail",
                    message: errorMessages.emailInUse
                })
            );
        };
        
        // Pass along
        req.body = {
            email: requestedEmail,
            ...rest
        };
        return next();

    } catch (error) {
        console.error(error);
        return res.status(500).json(
            errorResponse({
                name: "ValidateEmail",
                message: errorMessages.validateEmail
            })
        );
    };
};

module.exports = validateEmail;