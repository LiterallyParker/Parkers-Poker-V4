function validateType(value, expectedType) {

    if (expectedType === Number) {
        return !isNaN(value);
    };

    if (expectedType === String) {
        return typeof value === 'string';
    };

    if (expectedType === Boolean) {
        return typeof value === 'boolean';
    };

    if (expectedType === Array) {
        return Array.isArray(value);
    };

    return false;

};

module.exports = validateType;