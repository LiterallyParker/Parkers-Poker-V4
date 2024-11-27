require('dotenv').config();
const {
    successResponse,
    successMessages,
} = require('../../util');

const getAccount = async (req, res) => {

    const returnObject = {
        message: successMessages.getAccount,
        data: {
            id: req.user.id,
            firstname: req.user.firstname,
            lastname: req.user.lastname,
            username: req.user.username,
            email: req.user.email,
            emailVerified: req.user.emailVerified,
            createdAt: req.user.createdAt,
            updatedAt: req.user.updatedAt
        },
    };
    return res.status(200).json(successResponse(returnObject));

};

module.exports = getAccount;