const { User } = require("../../models");

const {
    verificationExpiry,
    generateEmailToken,
    sendVerificationEmail,
} = require("../../email/verification");

const {
    errorResponse,
    successResponse,
    errorMessages,
    successMessages,
} = require("../../util");

const { generateJWT } = require("../../auth");

const registerUser = async (req, res) => {
    // Grab fields
    const {
        firstname,
        lastname,
        username,
        email,
        hash
    } = req.body;
    const verificationToken = generateEmailToken();
    
    try {
        // Create
        const user = await User.create({
            firstname,
            lastname,
            username,
            email,
            hash,
            verificationToken,
            verificationExpiry
        });

        // Verify Creation
        if (!user) {
            return res.status(500).json(
                errorResponse({
                    name: "RegisterUser",
                    message: errorMessages.registerUser
                })
            );
        };

        // Send verification email, async
        // sendVerificationEmail(email, verificationToken).catch(error => console.error(error));

        const JSONtoken = generateJWT({ id: user.id })
        // Return user and a Token
        const returnObject = {
            message: successMessages.registerUser,
            data: {
                user: {
                    id: user.id,
                    firstname: user.firstname,
                    lastname: user.lastname,
                    username: user.username,
                    email: user.email,
                    emailVerified: user.emailVerified,
                    createdAt: user.createdAt,
                    updatedAt: user.updatedAt,
                },
                token: JSONtoken,
            },
        };
        return res.status(200).json(successResponse(returnObject));

    } catch (error) {
        console.error(error);
        return res.status(500).json(
            errorResponse({
                name: "RegisterUser",
                message: errorMessages.registerUser
            })
        );
    };
};

module.exports = registerUser;