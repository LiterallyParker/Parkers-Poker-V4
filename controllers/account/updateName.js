const {
    errorResponse,
    successResponse,
    errorMessages,
    successMessages,
} = require('../../util');

const updateName = async (req, res) => {
    const { firstname, lastname } = req.body;
    if (!firstname && !lastname) {
        return res.status(400).json(
            errorResponse({
                name: "UpdateName",
                message: errorMessages.supplyName
            })
        );
    };
    try {
        // Change either if provided
        if (firstname) {
            req.user.firstname = firstname;
        };
        if (lastname) {
            req.user.lastname = lastname;
        };

        // Save to DB
        await req.user.save();

        const returnObject = {
            message: successMessages.updateName,
            data: {
                id: req.user.id,
                firstname,
                lastname,
                username: req.user.username,
                email: req.user.email,
                emailVerified: req.user.emailVerified,
                createdAt: req.user.createdAt,
                updatedAt: req.user.updatedAt
            },
        }

        return res.status(200).json(successResponse(returnObject));

    } catch (error) {
        console.error("Error updating name:", error);
        return res.status(500).json(
            errorResponse({
                name: "UpdateName",
                message: errorMessages.updateName
            })
        );
    };
};

module.exports = updateName;