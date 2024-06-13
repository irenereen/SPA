import { BrowserRouter, Route, Routes } from "react-router-dom";
import { StrictMode, useState, useEffect } from "react";
import Login from "./components/login";
import "bootstrap/dist/css/bootstrap.min.css";
import Register from "./components/register";
import CustomerUpdate from "./components/updateCustomerDetails";

const App = () => {
 
  const [accessToken, setAccessToken] = useState(null);
  const [refreshToken, setRefreshToken] = useState(null);

  useEffect(() => {
    // Check localStorage for tokens and update state accordingly
    const access = localStorage.getItem("access");
    const refresh = localStorage.getItem("refresh");
    if (access && refresh) {
      setAccessToken(access);
      setRefreshToken(refresh);
    
    }
  }, []);

  return (
    <StrictMode>
      <BrowserRouter>
        <Routes>
          <Route path="/login" element={<Login />} />
          <Route path="/register" element={<Register />} />
          <Route path="/CustomerUpdateProfile" element={< CustomerUpdate/>} />

        </Routes>
      </BrowserRouter>
    </StrictMode>
  );
};

export default App;
