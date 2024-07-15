// pages/IndexPage.js

import React from 'react';
import { Container, Typography, Button, Box } from '@mui/material';
import { Link } from 'react-router-dom';

const IndexPage = () => {
    return (
        <Container maxWidth="md">
            <Box sx={{ my: 4 }}>
                <Typography variant="h4" component="h1" gutterBottom>
                    Welcome to Expense Manager
                </Typography>
                <Typography variant="body1" paragraph>
                    Manage your expenses efficiently with our Expense Manager application.
                    Track incomes, categorize expenses, and stay organized with ease.
                </Typography>
                <Box sx={{ mt: 2 }}>
                    <Button variant="contained" color="primary" component={Link} to="/login">
                        Login
                    </Button>
                    <Button variant="outlined" color="primary" sx={{ ml: 2 }} component={Link} to="/register">
                        Register
                    </Button>
                </Box>
            </Box>
        </Container>
    );
};

export default IndexPage;
