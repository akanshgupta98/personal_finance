// services/authService.js

import axios from 'axios';

const BASE_URL = 'http://127.0.0.1:8000/user/api/';

const login = async (username, password) => {
    try {
        const response = await axios.post(BASE_URL + 'login/', { username, password });
        localStorage.setItem('token', response.data.access);
        return response.data;
    } catch (error) {
        throw Error('Login failed.');
    }
};

const register = async (username, password, email) => {
    try {
        const response = await axios.post(BASE_URL + 'register/', { username, password, email });
        return response.data;
    } catch (error) {
        throw Error('Registration failed.');
    }
};

const changePassword = async (oldPassword, newPassword,confirmPassword) => {
    try {
        const token = localStorage.getItem('token');
        const response = await axios.put(
            BASE_URL + 'change-password/',
            { old_password: oldPassword, new_password: newPassword , confirm_password:confirmPassword},
            { headers: { Authorization: `Bearer ${token}` } }
        );
        return response.data;
    } catch (error) {
        console.log(error)
        throw Error(String(error.response.data.error));
    }
};

const resetPassword = async (email) => {
    try {
        const response = await axios.post(BASE_URL + 'reset_password/', { email });
        return response.data;
    } catch (error) {
        throw Error('Password reset request failed.');
    }
};

export { login, register, changePassword, resetPassword };
