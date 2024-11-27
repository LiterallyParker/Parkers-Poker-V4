const { User } = require("../../models");
const bcrypt = require("bcrypt");
const { generateJWT } = require("../../auth");
const { emailRegex } = require("../../email/verification");
const {
    errorResponse,
    successResponse,
    errorMessages,
    successMessages,
} = require("../../util");

const loginUser = async (req, res) => {
    const { identifier, password } = req.body;
    // Check if username or email
    const where = emailRegex(identifier) ? { email: identifier } : { username: identifier };

    try {
        // Get user's hash from database
        const foundUser = await User.findOne({
            where,
            attributes: {
                exclude: [
                    'verificationToken',
                    'verificationTokenExpiry',
                ]
            }
        });

        // If there isn't one
        if (!foundUser) {
            // Error out, no user with that identifier.
            return res.status(400).json(
                errorResponse({
                    name: "LoginUser",
                    message: errorMessages.invalidCredentials
                })
            );
        };

        // If the password doesn't match the hash
        const passwordMatch = await bcrypt.compare(password, foundUser.hash);

        if (!passwordMatch) {
            // Error out, invalid login.
            return res.status(400).json(
                errorResponse({
                    name: "LoginUser",
                    message: errorMessages.invalidCredentials
                })
            );
        };

        // Create a json token
        const token = generateJWT({ id: foundUser.id });

        const returnObject = {
            message: successMessages.loginUser,
            data: {
                user: {
                    id: foundUser.id,
                    firstname: foundUser.firstname,
                    lastname: foundUser.lastname,
                    username: foundUser.username,
                    email: foundUser.email,
                    emailVerified: foundUser.emailVerified,
                    createdAt: foundUser.createdAt,
                    updatedAt: foundUser.updatedAt
                },
                token
            },
        };

        return res.status(200).json(successResponse(returnObject));

    } catch (error) {
        console.error(error);
        return res.status(500).json(
            errorResponse({
                name: "LoginUser",
                message: errorMessages.loginUser
            })
        );
    };
};

module.exports = loginUser;