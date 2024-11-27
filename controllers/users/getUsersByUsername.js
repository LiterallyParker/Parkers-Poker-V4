const { Op } = require('sequelize');
const { User } = require("../../models");
const {
    errorResponse,
    successResponse,
    errorMessages,
    successMessages,
} = require("../../util");

const getUsersByUsername = async (req, res) => {
    const { username } = req.query;
    const { limit, offset } = req.pagination;

    try {

        const users = await User.findAll({
            where: {
                username: {
                    [Op.iLike]: `${username}%`, // Case-insensitive partial match
                }
            },
            attributes: {
                exclude: [
                    'hash',
                    'email',
                    'verificationToken',
                    'verificationTokenExpiry'
                ]
            },
            limit,
            offset,
            collate: 'utf8_bin'
        });

        if (!users || users.length < 1) {
            return res.status(404).json(
                errorResponse({
                    name: "GetUsersByUsername",
                    message: errorMessages.usersNotFound
                })
            );
        };

        const returnObject = {
            message: successMessages.getUsersByUsername,
            data: users,
        };

        return res.status(200).json(successResponse(returnObject));

    } catch (error) {
        console.error(error)
        return us(500).json(
            errorResponse({
                name: "GetUsersByUsername",
                message: errorMessages.getUsersByUsername
            })
        );
    };
};

module.exports = getUsersByUsername;