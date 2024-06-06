import React, { useState } from "react";
import axios from "axios";

import "bootstrap/dist/css/bootstrap.min.css";

const Login = () => {
  const backendUrl = process.env.REACT_APP_BACKEND_URL;
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");

  const handleSubmit = async (event) => {
    event.preventDefault();
    setError("");

    try {
      const response = await axios.post(`${backendUrl}/api/accounts/login/`, {
        email,
        password,
      });
      localStorage.setItem("access_token", response.data.tokens.access);
      localStorage.setItem("refresh_token", response.data.tokens.refresh);
      history.push("/dashboard"); // Redirect to a protected route
    } catch (error) {
      setError("Invalid email or password");
    }
  };

  return (
    <div
      className="container d-flex align-items-center justify-content-center"
      style={{ minHeight: "100vh" }}
    >
      <div className="row w-100">
        <div className="col-md-6 offset-md-3">
          <h2 className="text-center mb-4">Login</h2>
          <form onSubmit={handleSubmit}>
            <div className="mb-3">
              <label htmlFor="email" className="form-label">
                Email
              </label>
              <input
                type="email"
                className="form-control"
                id="email"
                value={email}
                onChange={(e) => setEmail(e.target.value)}
                required
              />
            </div>
            <div className="mb-3">
              <label htmlFor="password" className="form-label">
                Password
              </label>
              <input
                type="password"
                className="form-control"
                id="password"
                value={password}
                onChange={(e) => setPassword(e.target.value)}
                required
              />
            </div>
            {error && <div className="alert alert-danger mt-3">{error}</div>}
            <button type="submit" className="btn btn-primary w-100 mt-4">
              Login
            </button>
          </form>
        </div>
      </div>
    </div>
  );
};

export default Login;
