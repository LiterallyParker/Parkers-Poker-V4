const express = require("express");
const usersRoutes = express.Router();
const m = require("../middleware");
const { usersController } = require("../controllers");

usersRoutes.post("/register",

    m.rateLimiters.registerLimiter,

    m.validators.validateBody({
        username: String,
        requestedEmail: String,
        requestedPassword: String,
        confirmedEmail: String,
        confirmedPassword: String,
    }),

    m.account.validateUsername,
    m.account.validateEmail,
    m.password.validatePassword,
    m.password.hashPassword,

    usersController.registerUser,

);

usersRoutes.post("/login",

    m.validators.validateBody({
        identifier: String,
        password: String
    }),
    usersController.loginUser

);

usersRoutes.get('/verify',

    m.validators.validateQuery({
        token: String
    }),
    usersController.verifyEmail

);

usersRoutes.get("/search",

    m.validators.validateQuery({
        username: String,
    }),
    m.util.usePagination(),
    usersController.getUsersByUsername

);

usersRoutes.get("/:uId",

    m.validators.validateParams({
        uId: String
    }),
    usersController.getUserById,

);

module.exports = usersRoutes;