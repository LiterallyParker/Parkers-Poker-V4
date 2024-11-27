const sendEmail = require("../sendEmail");

const sendVerificationEmail = async (email, token) => {
    const verificationLink = `${process.env.APP_LINK}/api/users/verify?token=${token}`;

    const textContent = "Email verification";
    const htmlContent = `
    <div>
        <h2>Please verify your email by clicking <a href="${verificationLink}">here.</a></h2>
        <p>Thank you for joining! Tell your grandma about us.</p>
    </div>
    `;

    try {
        await sendEmail(email, 'Email Verification', textContent, htmlContent);
    } catch (error) {
        console.error(error);
        throw new Error('Error sending verification email.');
    };
};

module.exports = sendVerificationEmail;