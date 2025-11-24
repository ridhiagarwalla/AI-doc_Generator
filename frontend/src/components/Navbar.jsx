import { Link, useNavigate, useLocation } from "react-router-dom";
import { useEffect, useState } from "react";
import API from "../api/axios";

export default function Navbar() {
    const navigate = useNavigate();
    const location = useLocation();
    const [user, setUser] = useState(null);

    useEffect(() => {
        // Only load user if not on login/register pages
        const isAuthPage = location.pathname === "/login" || location.pathname === "/register" || location.pathname === "/";
        if (!isAuthPage) {
            loadUser();
        } else {
            // Check if user is already logged in (has token)
            const token = localStorage.getItem("token");
            if (token) {
                loadUser();
            }
        }
    }, [location.pathname]);

    const loadUser = async () => {
        try {
            const token = localStorage.getItem("token");
            if (!token) {
                setUser(null);
                return;
            }
            const res = await API.get("/auth/me");
            setUser(res.data);
        } catch (err) {
            // Not logged in or token invalid
            setUser(null);
        }
    };

    const handleLogout = () => {
        localStorage.removeItem("token");
        navigate("/login");
    };

    return (
        <nav className="bg-white shadow-md">
            <div className="container mx-auto px-4">
                <div className="flex justify-between items-center py-4">
                    <Link to="/projects" className="text-2xl font-bold text-blue-600">
                        AI Doc Generator
                    </Link>
                    <div className="flex items-center gap-4">
                        {user ? (
                            <>
                                <span className="text-gray-700">Hello, {user.full_name}</span>
                                <Link
                                    to="/projects"
                                    className="text-gray-700 hover:text-blue-600 transition"
                                >
                                    Projects
                                </Link>
                                <button
                                    onClick={handleLogout}
                                    className="bg-red-600 text-white px-4 py-2 rounded hover:bg-red-700 transition"
                                >
                                    Logout
                                </button>
                            </>
                        ) : (
                            <>
                                <Link
                                    to="/login"
                                    className="text-gray-700 hover:text-blue-600 transition"
                                >
                                    Login
                                </Link>
                                <Link
                                    to="/register"
                                    className="bg-blue-600 text-white px-4 py-2 rounded hover:bg-blue-700 transition"
                                >
                                    Register
                                </Link>
                            </>
                        )}
                    </div>
                </div>
            </div>
        </nav>
    );
}

