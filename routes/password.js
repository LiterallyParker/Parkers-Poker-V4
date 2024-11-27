const express = require("express");
const passwordRoutes = express.Router();
const m = require("../middleware")
const { passwordController } = require("../controllers")

passwordRoutes.post('/',

    m.users.requireUser,
    m.validators.validateBody({
        requestedPassword: String,
        confirmedPassword: String,
        password: String,
    }),

    m.password.verifyPassword,

    m.password.validatePassword,
    m.password.comparePassword,
    m.password.hashPassword,

    passwordController.updatePassword

);

module.exports = passwordRoutes