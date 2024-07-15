// App.js

import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Login from './pages/Login';
import Register from './pages/Register';
import ChangePassword from './pages/ChangePassword';
import ResetPassword from './pages/ResetPassword';
import Index from './pages/IndexPage'

const App = () => {
    return (
        <Router>
            <Routes>
                <Route exact path="/login" element={ <Login/> } />
                <Route exact path="/register" element={<Register/>} />
                <Route exact path="/change-password" element={<ChangePassword/>} />
                <Route exact path="/reset-password" element={<ResetPassword/>} />
                <Route exact path="/" element={<Index/>} />
                {/* Add more routes as needed */}
            </Routes>
        </Router>
    );
};

export default App;
