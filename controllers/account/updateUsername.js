const {
    errorResponse,
    successResponse,
    errorMessages,
    successMessages,
} = require('../../util');

const updateUsername = async (req, res) => {
    const { username } = req.body;
    req.user.username = username;

    try {
        await req.user.save();

        const returnObject = {
            message: successMessages.updateUsername,
            data: {
                id: req.user.id,
                firstname: req.user.firstname,
                lastname: req.user.lastname,
                username,
                email: req.user.email,
                emailVerified: req.user.emailVerified,
                createdAt: req.user.createdAt,
                updatedAt: req.user.updatedAt
            },
        };

        return res.status(200).json(successResponse(returnObject));

    } catch (error) {
        console.error("Error updating username:", error);
        return res.status(500).json(
            errorResponse({
                name: "UpdateUsername",
                message: errorMessages.updateUsername
            })
        );
    };
};

module.exports = updateUsername;