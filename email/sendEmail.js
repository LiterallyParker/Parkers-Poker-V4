require("dotenv").config();
const nodemailer = require('nodemailer');

const sendEmail = async (to, subject, textContent, htmlContent) => {
    const transporter = nodemailer.createTransport({
        host: process.env.EMAIL_HOST,
        port: process.env.EMAIL_PORT,
        secure: true,
        auth: {
            user: process.env.EMAIL_USER,
            pass: process.env.EMAIL_PASS,
        },
    });

    const mailOptions = {
        from: `"SITE_NAME" <no-reply@website.com>`,
        to,
        subject,
        text: textContent,
        html: htmlContent,
    };

    try {
        const sent = await transporter.sendMail(mailOptions);
        if (sent.accepted.length < 1) {
            throw new Error('Error sending email. No acceptees.')
        }
    } catch (error) {
        console.error(error);
        throw new Error('Error sending email.');
    };
};

module.exports = sendEmail