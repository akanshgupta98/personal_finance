// components/LoginForm.js

import React, { useState } from 'react';
import { TextField, Button, Box } from '@mui/material';
import { login } from '../services/authService';

const LoginForm = () => {
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');

    const handleLogin = async (e) => {
        e.preventDefault();
        try {
            await login(username, password);
            alert('Login successful!');
            // Redirect to dashboard or desired page after successful login
        } catch (error) {
            alert('Login failed. Please check your credentials.');
        }
    };

    return (
        <Box>
            <form onSubmit={handleLogin}>
                <TextField
                    id="username"
                    label="Username"
                    value={username}
                    onChange={(e) => setUsername(e.target.value)}
                    fullWidth
                />
                <TextField
                    id="password"
                    label="Password"
                    type="password"
                    value={password}
                    onChange={(e) => setPassword(e.target.value)}
                    fullWidth
                />
                <Button type="submit" variant="contained" color="primary">
                    Login
                </Button>
            </form>
        </Box>
    );
};

export default LoginForm;
