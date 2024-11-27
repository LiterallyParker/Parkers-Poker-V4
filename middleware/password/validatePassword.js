const {
    errorResponse,
    errorMessages
} = require("../../util");

const validatePassword = async (req, res, next) => {
    const {
        requestedPassword,
        confirmedPassword
    } = req.body;
    delete req.body.confirmedPassword;

    // Password Match
    if (requestedPassword !== confirmedPassword) {
        return res.status(400).json(
            errorResponse({
                name: "ValidatePassword",
                message: errorMessages.passwordMismatch,
            })
        );
    };

    // Password Strength Checks
    if (requestedPassword.length < 8) {
        return res.status(400).json(
            errorResponse({
                name: "ValidatePassword",
                message: errorMessages.passwordLength,
            })
        );
    };

    const hasCapital = /[A-Z]/.test(requestedPassword);
    const hasNumber = /\d/.test(requestedPassword);
    const hasSpecial = /[!@#$%_]/.test(requestedPassword);

    if (!hasCapital || !hasNumber || !hasSpecial) {
        return res.status(400).json(
            errorResponse({
                name: "ValidatePassword",
                message: errorMessages.passwordRequirements,
            })
        );
    };
    
    return next();
};

module.exports = validatePassword;
