const { Op } = require('sequelize');
const { User } = require("../../models");
const {
    errorResponse,
    successResponse,
    errorMessages,
    successMessages,
} = require("../../util");

const getUserById = async (req, res) => {
    const { uId } = req.params;

    try {
        const user = await User.findByPk(uId, {
            attributes: {
                exclude: [
                    'hash',
                    'verificationToken',
                    'verificationTokenExpiry'
                ]
            }
        });

        if (!user) {
            return res.status(404).json(
                errorResponse({
                    name: "GetUserById",
                    message: errorMessages.userNotFound
                })
            );
        };

        const returnObject = {
            message: successMessages.getUserById,
            data: user,
        };

        return res.status(200).json(successResponse(returnObject));
    } catch (error) {
        console.error(error);
        return res.status(500).json(
            errorResponse({
                name: "GetUserById",
                message: errorMessages.getUserById(uId)
            })
        );
    };
};

module.exports = getUserById;