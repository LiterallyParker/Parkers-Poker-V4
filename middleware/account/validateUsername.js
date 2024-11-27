const { Op } = require("sequelize")
const { User } = require("../../models");
const {
    errorResponse,
    errorMessages,
    isProfane
} = require("../../util");

const validateUsername = async (req, res, next) => {
    const { username, ...rest } = req.body;

    // If user, and same name
    if (req?.user && req.user.username === username) {
        return res.status(400).json(
            errorResponse({
                name: "ValidateUsername",
                message: errorMessages.sameUsername
            })
        );
    };

    // Username Restrictions - A-Z, a-z, 0-9, _, -
    const usernameRegex = /^[A-Za-z0-9._-]+$/;
    if (!usernameRegex.test(username)) {
        return res.status(400).json(
            errorResponse({
                name: "ValidateUsername",
                message: errorMessages.invalidUsername
            })
        );
    };

    // Username Length - 8 < username < 15
    if (username.length < 8 || username.length > 15) {
        return res.status(400).json(
            errorResponse({
                name: "ValidateUsername",
                message: errorMessages.usernameLength
            })
        );
    };

    // Username Profanity
    if (isProfane(username)) {
        return res.status(400).json(
            errorResponse({
                name: "ValidateUsername",
                message: errorMessages.usernameNotAllowed
            })
        );
    };

    try {
        const existingUser = await User.findOne({
            where: {
                username,
                id: { [Op.ne]: req?.user ? req.user.id : null }
            },
            attributes: ['id', 'username']
        });

        if (existingUser) {
            return res.status(400).json(
                errorResponse({
                    name: "ValidateUsername",
                    message: errorMessages.usernameInUse
                })
            );
        };
        req.body = { username, ...rest };

        next();
    } catch (error) {
        console.error(error);
        return res.status(500).json(
            errorResponse({
                name: "ValidateUsername",
                message: errorMessages.validateUsername
            })
        );
    };
};

module.exports = validateUsername;