import { useState } from "react";
import API from "../api/axios";
import { useNavigate, Link } from "react-router-dom";
import Navbar from "../components/Navbar";

export default function Register() {
    const navigate = useNavigate();
    const [form, setForm] = useState({ full_name: "", email: "", password: "" });
    const [loading, setLoading] = useState(false);

    const handleSubmit = async (e) => {
        e.preventDefault();
        
        // Validate inputs
        if (!form.full_name || !form.email || !form.password) {
            alert("Please fill in all fields");
            return;
        }
        
        if (form.password.length < 6) {
            alert("Password must be at least 6 characters long");
            return;
        }
        
        setLoading(true);
        try {
            const response = await API.post("/auth/register", {
                full_name: form.full_name.trim(),
                email: form.email.trim(),
                password: form.password
            });
            
            if (response.data && response.data.message) {
                alert("Registration successful! Please login with your credentials.");
                navigate("/login");
            } else {
                alert("Registration successful! Please login.");
                navigate("/login");
            }
        } catch (err) {
            console.error("Registration error:", err);
            console.error("Error response:", err.response);
            
            let errorMessage = "Registration failed. Please try again.";
            
            if (err.response) {
                // Server responded with error
                errorMessage = err.response.data?.detail || err.response.data?.message || errorMessage;
            } else if (err.request) {
                // Request was made but no response
                errorMessage = "Cannot connect to server. Please make sure the backend is running.";
            } else {
                // Something else happened
                errorMessage = err.message || errorMessage;
            }
            
            alert(errorMessage);
        } finally {
            setLoading(false);
        }
    };

    return (
        <div className="min-h-screen bg-gray-50">
            <Navbar />
            <div className="flex items-center justify-center px-4 py-12">
                <div className="bg-white rounded-lg shadow-md p-8 w-full max-w-md">
                    <h2 className="text-3xl font-bold text-center text-gray-800 mb-6">Register</h2>
                    <form onSubmit={handleSubmit} className="space-y-4">
                        <div>
                            <label className="block text-sm font-medium text-gray-700 mb-2">
                                Full Name
                            </label>
                            <input
                                type="text"
                                placeholder="Enter your full name"
                                value={form.full_name}
                                onChange={(e) => setForm({ ...form, full_name: e.target.value })}
                                className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
                                required
                            />
                        </div>

                        <div>
                            <label className="block text-sm font-medium text-gray-700 mb-2">
                                Email
                            </label>
                            <input
                                type="email"
                                placeholder="Enter your email"
                                value={form.email}
                                onChange={(e) => setForm({ ...form, email: e.target.value })}
                                className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
                                required
                            />
                        </div>

                        <div>
                            <label className="block text-sm font-medium text-gray-700 mb-2">
                                Password
                            </label>
                            <input
                                type="password"
                                placeholder="Enter your password"
                                value={form.password}
                                onChange={(e) => setForm({ ...form, password: e.target.value })}
                                className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
                                required
                                minLength={6}
                            />
                        </div>

                        <button
                            type="submit"
                            disabled={loading}
                            className="w-full bg-blue-600 text-white px-6 py-2 rounded-lg hover:bg-blue-700 transition disabled:bg-gray-400"
                        >
                            {loading ? "Registering..." : "Register"}
                        </button>

                        <p className="text-center text-sm text-gray-600">
                            Already have an account?{" "}
                            <Link to="/login" className="text-blue-600 hover:underline">
                                Login here
                            </Link>
                        </p>
                    </form>
                </div>
            </div>
        </div>
    );
}
