const { User } = require("../../models");
const { errorResponse, errorMessages, successResponse, successMessages } = require("../../util");

const verifyEmail = async (req, res, next) => {
    const { token } = req.query;

    try {
        const user = await User.findOne({ where: { verificationToken: token } } );

        if (!user) {
            return res.status(404).json(
                errorResponse({
                    name: "VerifyEmail",
                    message: errorMessages.invalidToken
                })
            );
        };

        const now = new Date();
        const isExpired = user.verificationToken && now > new Date(user.verificationTokenExpiry);

        if (isExpired) {
            return res.status(400).json(
                errorResponse({
                    name: "VerifyEmail",
                    message: errorMessages.expiredToken
                })
            );
        };

        user.emailVerified = true;
        user.verificationToken = null;
        user.verificationTokenExpiry = null;
        await user.save();

        return res.status(200).json(
            successResponse({
                message: successMessages.verifyEmail
            })
        );
        
    } catch (error) {
        console.error(error);
        return res.status(500).json(
            errorResponse({
                name: "VerifyEmail",
                message: errorMessages.verifyEmail
            })
        );
    };
};

module.exports = verifyEmail;