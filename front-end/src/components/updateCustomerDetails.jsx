// src/components/updateCustomerDetails.js

import React, { useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";
import axios from "axios";

const CustomerUpdate = () => {
  const backendUrl = process.env.REACT_APP_BACKEND_URL;
  const [customer, setCustomer] = useState(null);
  const [profilePicture, setProfilePicture] = useState(null);

  const navigate = useNavigate();

  useEffect(() => {
    const fetchCustomerDetails = async () => {
      const access = localStorage.getItem("access");
      if (!access) {
        navigate("/login");
        return;
      }

      try {
        const response = await axios.get(`${backendUrl}/api/customer/${localStorage.userID}/`, {
          headers: {
            Authorization: `Bearer ${access}`,
          }
        });

        setCustomer(response.data);
        
      } catch (error) {
        console.error("Failed to fetch customer details", error);
      }
    };

    fetchCustomerDetails();
  }, [navigate, backendUrl]);

  const handleChange = (e) => {
    const { name, value } = e.target;
    setCustomer((prevState) => ({
      ...prevState,
      [name]: value
    }));
  };

  const handleFileChange = (e) => {
    setProfilePicture(e.target.files[0]);
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    const access = localStorage.getItem("access");

    const formData = new FormData();
    formData.append("phone_number", customer.phone_number);
    formData.append("address", customer.address);
    if (profilePicture) {
      formData.append("profile_picture", profilePicture);
    }

    Object.keys(customer).forEach((key) => {
      formData.append(key, customer[key]);
    });

    try {
      console.log(formData)
      await axios.put(`${backendUrl}/api/customer/${localStorage.userID}/`, formData, {
        headers: {
    
          "Content-Type": "multipart/form-data",
          "Authorization": `Bearer ${access}`
        }
      });
      alert('Updated Succesfully')
    } catch (error) {
      console.error("Failed to update customer details", error);
    }
  };

  if (customer === null) {
    return <div className="container">Loading...</div>;
  }

  return (
    <div className="container mt-5">
      <h2>Update Customer Details</h2>
      <form onSubmit={handleSubmit}>
        <div className="mb-3">
          <label htmlFor="email" className="form-label">Email</label>
          <input
            type="email"
            className="form-control"
            id="email"
            name="email"
            value={customer.email || ""}
            onChange={handleChange}
            required
          />
        </div>
        <div className="mb-3">
          <label htmlFor="first_name" className="form-label">First Name</label>
          <input
            type="text"
            className="form-control"
            id="first_name"
            name="first_name"
            value={customer.first_name || ""}
            onChange={handleChange}
            required
          />
        </div>
        <div className="mb-3">
          <label htmlFor="last_name" className="form-label">Last Name</label>
          <input
            type="text"
            className="form-control"
            id="last_name"
            name="last_name"
            value={customer.last_name || ""}
            onChange={handleChange}
            required
          />
        </div>
        <div className="mb-3">
          <label htmlFor="address" className="form-label">Address</label>
          <input
            type="text"
            className="form-control"
            id="address"
            name="address"
            value={customer.address || ""}
            onChange={handleChange}
          />
        </div>
        <div className="mb-3">
          <label htmlFor="phone_number" className="form-label">Phone Number</label>
          <input
            type="number"
            className="form-control"
            id="phone_number"
            name="phone_number"
            value={customer.phone_number || ""}
            onChange={handleChange}
          />
        </div>
        <div className="mb-3">
          <label htmlFor="profile_picture" className="form-label">Profile Picture</label>
          <input
          required
            type="file"
            className="form-control"
            id="profile_picture"
            name="profile_picture"
            accept=".jpg, .jpeg, .png"
            onChange={handleFileChange}
          />
        </div>
        <button type="submit" className="btn btn-primary">Update</button>
      </form>
    </div>
  );
};

export default CustomerUpdate;
