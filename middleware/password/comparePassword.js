const { User } = require("../../models");
const { errorResponse, errorMessages } = require("../../util");
const bcrypt = require("bcrypt");

const comparePassword = async (req, res, next) => {
    const { id: uId } = req.user;
    const { requestedPassword } = req.body;

    try {
        const user = await User.findByPk(uId, {
            attributes: ['hash']
        });
        const isSame = await bcrypt.compare(requestedPassword, user.hash);
        if (isSame) {
            return res.status(400).json(
                errorResponse({
                    name: "ComparePassword",
                    message: errorMessages.samePassword
                })
            );
        };
        next();

    } catch (error) {
        console.error(error);
        return res.status(500).json(
            errorResponse({
                name: "ComparePassword",
                message: errorMessages.comparePassword
            })
        );
    };
};

module.exports = comparePassword;