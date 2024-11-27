const { User } = require('../../models');
const {
    errorResponse,
    successResponse,
    errorMessages,
    successMessages,
} = require('../../util');

const deleteAccount = async (req, res) => {
    const { id: uId } = req.user;

    try {
        // Attempt to delete the user
        const result = await User.destroy({
            where: { id: uId }
        });

        // Make sure there was a user to delete
        if (result === 0) {
            return res.status(400).json(
                errorResponse({
                    name: "DeleteAccount",
                    message: errorMessages.userNotFound(uId),
                })
            );
        };

        const returnObject = { message: successMessages.deleteAccount };

        return res.status(200).json(successResponse(returnObject));

    } catch (error) {
        console.error(error);
        return res.status(500).json(
            errorResponse({
                name: "DeleteAccount",
                message: errorMessages.deleteAccount
            })
        );
    };
};

module.exports = deleteAccount;