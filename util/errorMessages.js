const errorMessages = {
    tooManyRequests: "Too many requests, try again later",
    server: "Server Error",
    unknownRoute: "Unknown Route",
    
    registerUser: "Error while registering user",
    userNotFound: "User not found",
    usersNotFound: "Users not found.",
    notLoggedIn: "User must be logged in to perform this action",
    authToken: (prefix) => `Authorization header must be a ${prefix}token`,
    setUser: "Error while setting request user",
    usernameInUse: "Username is already in use",
    emailInUse: "Email is already in use",
    supplyName: "Supply either a first or last name",
    sameFirstname: "Firstname must be different from previous",
    sameLastname: "Lastname must be different from previous",
    sameUsername: "Username must be different from previous",
    sameEmail: "Email must be different from previous",

    incorrectPassword: "Incorrect password",
    comparePassword: "Error while comparing password",
    samePassword: "New password must be different",
    wrongPassword: "Password is incorrect",
    updatePassword: "Error while updating password",
    passwordRequirements: "Password must contain 1+ capital letter, 1+ number, and 1+ special character: !, @, #, $, %, _",
    passwordLength: "Password must be longer than 8 characters",
    passwordMismatch: "Passwords do not match",
    passwordRequired: "Password is required to perform this action.",

    validateBody: (invalidFields) => `Missing or invalid fields: ${invalidFields.join(", ")}`,
    validateQuery: (invalidQueries) => `Missing or invalid fields: ${invalidQueries.join(", ")}`,
    validateParams: (invalidParams) => `Missing or invalid fields: ${invalidParams.join(", ")}`,
};

module.exports = errorMessages;