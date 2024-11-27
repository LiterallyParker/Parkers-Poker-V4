const bcrypt = require("bcrypt");
const { errorResponse } = require("../../util");

const hashPassword = async (req, res, next) => {
    const { requestedPassword } = req.body;
    delete req.body.requestedPassword;
    try {
        const saltRounds = parseInt(process.env.SALT_ROUNDS) || 10;
        req.body.hash = await bcrypt.hash(requestedPassword, saltRounds);
        return next();
    } catch (error) {
        console.error("Hashing Error:", error);
        return res.status(500).json(
            errorResponse({
                name: "PasswordHashing",
                message: "Error hashing the password",
            })
        );
    }
};

module.exports = hashPassword;
