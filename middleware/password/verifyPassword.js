const { User } = require("../../models");
const { errorResponse, errorMessages } = require("../../util");
const bcrypt = require("bcrypt");

const verifyPassword = async (req, res, next) => {
    const { id: uId } = req.user;
    const { password, ...rest } = req.body;
    req.body = rest;

    try {
        const user = await User.findByPk(uId, {
            attributes: ['hash']
        });
        const isPassword = await bcrypt.compare(password, user.hash);
        if (!isPassword) {
            return res.status(401).json(
                errorResponse({
                    name: "RequirePassword",
                    message: errorMessages.incorrectPassword
                })
            );
        };
        next();

    } catch (error) {
        console.error(error);
        return res.status(500).json(
            errorResponse({
                name: "VerifyPassword",
                message: errorMessages.verifyPassword
            })
        );
    };
};

module.exports = verifyPassword;