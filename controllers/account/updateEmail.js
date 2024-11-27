const {
    verificationTokenExpiry,
    generateEmailToken,
    sendVerificationEmail
} = require('../../email/verification');
const { User } = require("../../models");
const {
    errorResponse,
    successResponse,
    errorMessages,
    successMessages,
} = require('../../util');

const updateEmail = async (req, res) => {

    // Grab email and userId
    const { email } = req.body;
    const { id: uId } = req.user;

    // Verifiy different email
    if (email === req.user.email) {
        return res.status(400).json(
            errorResponse({
                name: "UpdateEmail",
                message: errorMessages.sameEmail
            })
        );
    };

    try {

        // Generate a token
        const verificationToken = generateEmailToken();

        // Update the user
        const user = await User.update(
            {
                email,
                emailVerified: false,
                verificationToken,
                verificationTokenExpiry
            },
            {
                where: { id: uId }
            }
        );

        // Send verification email, async
        // sendVerificationEmail(email, verificationToken).catch(error => console.error(error));

        // Return
        const returnObject = {
            message: successMessages.updateEmail,
            data: {
                id: req.user.id,
                firstname: req.user.firstname,
                lastname: req.user.lastname,
                username: req.user.username,
                email,
                emailVerified: req.user.emailVerified,
                createdAt: req.user.createdAt,
                updatedAt: req.user.updatedAt
            },
        };
        return res.status(200).json(successResponse(returnObject));

    } catch (error) {
        console.error("Error updating email:", error);
        return res.status(500).json(
            errorResponse({
                name: "UpdateEmail",
                message: errorMessages.updateEmail
            })
        );
    };
};

module.exports = updateEmail;