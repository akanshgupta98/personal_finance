// components/RegisterForm.js

import React, { useState } from 'react';
import { TextField, Button, Box } from '@mui/material';
import { register } from '../services/authService';

const RegisterForm = () => {
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
    const [email, setEmail] = useState('');

    const handleRegister = async (e) => {
        e.preventDefault();
        try {
            await register(username, password, email);
            alert('Registration successful!');
            // Optionally redirect to login page after successful registration
        } catch (error) {
            alert('Registration failed.');
        }
    };

    return (
        <Box>
            <form onSubmit={handleRegister}>
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
                <TextField
                    id="email"
                    label="Email"
                    type="email"
                    value={email}
                    onChange={(e) => setEmail(e.target.value)}
                    fullWidth
                />
                <Button type="submit" variant="contained" color="primary">
                    Register
                </Button>
            </form>
        </Box>
    );
};

export default RegisterForm;
