const express = require("express");
const accountRoutes = express.Router();
const m = require("../middleware")
const { accountController } = require("../controllers")

accountRoutes.get("/",

    m.users.requireUser,
    accountController.getAccount

);

accountRoutes.patch("/name",

    m.users.requireUser,
    m.account.validateName,
    accountController.updateName,

);

accountRoutes.patch("/username",

    m.users.requireUser,
    m.validators.validateBody({
        username: String,
        password: String,
    }),

    m.password.verifyPassword,
    m.account.validateUsername,
    accountController.updateUsername,

);

accountRoutes.patch("/email",

    m.users.requireUser,
    m.validators.validateBody({
        requestedEmail: String,
        confirmedEmail: String,
        password: String,
    }),

    m.password.verifyPassword,
    m.account.validateEmail,
    accountController.updateEmail,

);

module.exports = accountRoutes;