const express = require('express');
const app = express();

app.get('/', (req, res) => {
    res.send('Hello, World!');
});

app.get('/api/v1/stats', (req, res) => {
    res.json({ status: 'success', data: 'Here are your stats' });
});

app.listen(5000, '0.0.0.0', () => {
    console.log('Server is running on http://0.0.0.0:5000');
});
