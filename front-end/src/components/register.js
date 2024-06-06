import React, { useState } from "react";
import axios from "axios";
import "bootstrap/dist/css/bootstrap.min.css"; // Include Bootstrap CSS
import { FaEye, FaEyeSlash } from "react-icons/fa"; // Import eye icons from react-icons

const Register = () => {
  const backendUrl = process.env.REACT_APP_BACKEND_URL;
  const [formData, setFormData] = useState({
    username: "",
    email: "",
    password: "",
    password2: "",
  });

  const [showPassword, setShowPassword] = useState({
    password: false,
    password2: false,
  });

  const handleChange = (event) => {
    setFormData({ ...formData, [event.target.name]: event.target.value });
  };

  const handleTogglePasswordVisibility = (field) => {
    setShowPassword({ ...showPassword, [field]: !showPassword[field] });
  };

  const getFilteredFormData = (formData) => {
    const { password2, ...filteredData } = formData; // Destructuring assignment
    return filteredData;
  };

  const handleSubmit = async (event) => {
    event.preventDefault();

    if (formData.password !== formData.password2) {
      alert("Passwords do not match!");
      return;
    }

    try {
      if (!backendUrl) {
        throw new Error("Backend URL is not set in the environment variables.");
      }

      const filteredData = getFilteredFormData(formData);

      const response = await axios.post(
        `${backendUrl}/api/accounts/register/`,
        formData,
        {
          headers: {
            "Content-Type": "application/json",
          },
        }
      );

      if (response.status === 201) {
        console.log("User created successfully!", response.data);
        // Handle successful registration (e.g., navigate to login page)
      } else {
        console.error("Unexpected response status:", response.status);
        // Handle unexpected response status (e.g., display error message)
      }
    } catch (error) {
      if (error.response) {
        // The request was made and the server responded with a status code outside the range of 2xx
        console.error("Error creating user:", error.response.data);
        // Handle registration errors (e.g., display error message)
      } else if (error.request) {
        // The request was made but no response was received
        console.error("No response received:", error.request);
        // Handle network errors or server not responding
      } else {
        // Something happened in setting up the request that triggered an error
        console.error("Error setting up request:", error.message);
      }
    }
  };

  return (
    <div className="register-form container">
      <h1>Register</h1>
      <form onSubmit={handleSubmit}>
        <div className="form-group mb-3">
          <label htmlFor="username" className="form-label">
            Username:
          </label>
          <input
            type="text"
            id="username"
            name="username"
            value={formData.username}
            onChange={handleChange}
            required
            className="form-control"
          />
        </div>
        <div className="form-group mb-3">
          <label htmlFor="email" className="form-label">
            Email:
          </label>
          <input
            type="email"
            id="email"
            name="email"
            value={formData.email}
            onChange={handleChange}
            required
            className="form-control"
          />
        </div>
        <div className="form-group mb-3 position-relative">
          <label htmlFor="password" className="form-label">
            Password:
          </label>
          <input
            type={showPassword.password ? "text" : "password"}
            id="password"
            name="password"
            value={formData.password}
            onChange={handleChange}
            required
            className="form-control"
          />
          <button
            type="button"
            className="btn btn-link position-absolute top-50 end-0 translate-middle-y"
            onClick={() => handleTogglePasswordVisibility("password")}
          >
            {showPassword.password ? <FaEyeSlash /> : <FaEye />}
          </button>
        </div>
        <div className="form-group mb-3 position-relative">
          <label htmlFor="password2" className="form-label">
            Confirm Password:
          </label>
          <input
            type={showPassword.password2 ? "text" : "password"}
            id="password2"
            name="password2"
            value={formData.password2}
            onChange={handleChange}
            required
            className="form-control"
          />
          <button
            type="button"
            className="btn btn-link position-absolute top-50 end-0 translate-middle-y"
            onClick={() => handleTogglePasswordVisibility("password2")}
          >
            {showPassword.password2 ? <FaEyeSlash /> : <FaEye />}
          </button>
        </div>
        <button type="submit" className="btn btn-primary">
          Register
        </button>
      </form>
    </div>
  );
};

export default Register;
