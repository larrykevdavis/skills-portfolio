const express = require('express');
const crypto = require('crypto');
const path = require('path');
const app = express();

app.use(express.json());

// Serving the Passkey registration page
app.use(express.static(path.join(__dirname, 'public'), {
    index: 'register.html'
}));

// Register the paskey
app.get('/register-passkey', (req, res) => {

    const challenge = crypto.randomBytes(32);

    const userId = crypto.randomBytes(16);

    const username =  req.query.username;


    res.json({
        challenge: challenge.toString('base64'),
        rp: { name: "FIDO Sample" },

        user: {
            id: userId.toString('base64'),
            name: username,
            displayName: username
        },

        attestation: 'direct',

        pubKeyCredParams: [
            { type: 'public-key', alg: -7 },   // ES256
            { type: 'public-key', alg: -257 }  // RS256
        ]
    });
});

//processing the pass key
app.get('/process:username', (req, res) => {
    res.sendFile(path.join(__dirname, 'public', 'process_passkey.html'));
})


// Serving the Passkey registration page on login
app.get('/login', (req, res) => {
    res.sendFile(path.join(__dirname, 'public', 'login.html'));
})

// Verify the passkey to authenticate
app.post('/authenticate', (req, res) => {

    const { id, rawId, username } = req.body;

    console.log('Received credential:', req.body);
    return res.json({ success: true });
});

app.listen(3000, () => console.log('Server running on http://localhost:3000'));