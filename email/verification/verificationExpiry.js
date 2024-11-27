const verificationExpiry = new Date(Date.now() + 24 * 60 * 60 * 1000) // Email verification - Valid for 24 hours

module.exports = verificationExpiry;