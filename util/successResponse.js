const successResponse = ({

    message = "Success.",
    data = null,
    
}) => {

    const response = {
        error: false,
        message
    };
    if (data) response.data = data;

    return response;

};

module.exports = successResponse;