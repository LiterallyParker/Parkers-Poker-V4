const errorResponse = ({

    name = "",
    message = "There was an error :(",

}) => {

    return {
        error: true,
        name: `${name}Error`,
        message
    };

};

module.exports = errorResponse;