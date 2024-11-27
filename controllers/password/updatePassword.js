const { User } = require("../../models");
const {
    errorResponse,
    errorMessages,
    successResponse,
    successMessages
} = require("../../util");

const updatePassword = async (req, res) => {
    const { hash } = req.body;
    const { id: userId } = req.user;

    try {
        const user = await User.findByPk(userId);
        user.hash = hash;
        await user.save();
        return res.status(200).json(
            successResponse({
                message: successMessages.updatePassword
            })
        );
    } catch (error) {
        console.error(error);
        return res.status(500).json(
            errorResponse({
                name: "UpdatePassword",
                message: errorMessages.server,
            })
        );
    };
};

module.exports = updatePassword;
