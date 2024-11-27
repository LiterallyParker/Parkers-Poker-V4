const express = require("express");
const apiRoutes = express.Router();

const usersRoutes = require("./users");
apiRoutes.use("/users", usersRoutes);

const accountRoutes = require("./account");
apiRoutes.use("/account", accountRoutes);

const passwordRoutes = require("./password");
apiRoutes.use("/password", passwordRoutes);

module.exports = apiRoutes;