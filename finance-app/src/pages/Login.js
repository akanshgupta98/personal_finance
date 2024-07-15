// Login.js

import React from 'react';
import { Container, Typography, Box } from '@mui/material';
import LoginForm from '../components/LoginForm';

const Login = () => {
    return (
        <Container maxWidth="sm">
            <Box sx={{ marginTop: 8, display: 'flex', flexDirection: 'column', alignItems: 'center' }}>
                <Typography component="h1" variant="h5">
                    Sign in
                </Typography>
                <LoginForm />
            </Box>
        </Container>
    );
};

export default Login;
