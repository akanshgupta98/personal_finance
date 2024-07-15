// pages/ChangePassword.js

import React, { useState } from 'react';
import { Container, Typography, TextField, Button, Box, Dialog, DialogTitle, DialogContent, DialogActions } from '@mui/material';
import { changePassword } from '../services/authService';

const ChangePassword = () => {
    const [oldPassword, setOldPassword] = useState('');
    const [newPassword, setNewPassword] = useState('');
    const [confirmPassword, setConfirmPassword] = useState('');
    const [error, setError] = useState(null);
    const [openDialog, setOpenDialog] = useState(false);

    const handleChangePassword = async (e) => {
        e.preventDefault();

        if (newPassword !== confirmPassword) {
            setError('Passwords do not match.');
            return;
        }

        try {
            await changePassword(oldPassword, newPassword, confirmPassword);
            alert('Password changed successfully!');
            // Optionally redirect or handle success scenario
        } catch (error) {
            console.log(error)
            setError(error.message);
            setOpenDialog(true);
        }
    };

    const handleCloseDialog = () => {
        setOpenDialog(false);
    };

    return (
        <Container maxWidth="sm">
            <Box sx={{ my: 4 }}>
                <Typography variant="h4" component="h1" gutterBottom>
                    Change Password
                </Typography>
                <form onSubmit={handleChangePassword}>
                    <TextField
                        id="oldPassword"
                        label="Current Password"
                        type="password"
                        value={oldPassword}
                        onChange={(e) => setOldPassword(e.target.value)}
                        fullWidth
                        required
                        margin="normal"
                    />
                    <TextField
                        id="newPassword"
                        label="New Password"
                        type="password"
                        value={newPassword}
                        onChange={(e) => setNewPassword(e.target.value)}
                        fullWidth
                        required
                        margin="normal"
                    />
                    <TextField
                        id="confirmPassword"
                        label="Confirm New Password"
                        type="password"
                        value={confirmPassword}
                        onChange={(e) => setConfirmPassword(e.target.value)}
                        fullWidth
                        required
                        margin="normal"
                    />
                    <Button type="submit" variant="contained" color="primary" sx={{ mt: 2 }}>
                        Change Password
                    </Button>
                </form>
            </Box>

            {/* Error Dialog */}
            <Dialog open={openDialog} onClose={handleCloseDialog}>
                <DialogTitle>Error</DialogTitle>
                <DialogContent>
                    <Typography variant="body1">{error}</Typography>
                </DialogContent>
                <DialogActions>
                    <Button onClick={handleCloseDialog} color="primary">
                        Close
                    </Button>
                </DialogActions>
            </Dialog>
        </Container>
    );
};

export default ChangePassword;
