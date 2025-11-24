import axios from "axios";

const API = axios.create({
    baseURL: import.meta.env.VITE_API_URL || "http://127.0.0.1:8000",
});

// Inject JWT token automatically
API.interceptors.request.use((config) => {
    const token = localStorage.getItem("token");
    if (token) {
        config.headers.Authorization = `Bearer ${token}`;
    }
    return config;
});

// Handle 401 errors (unauthorized)
API.interceptors.response.use(
    (response) => response,
    (error) => {
        if (error.response?.status === 401) {
            localStorage.removeItem("token");
            // Only redirect if not already on login or register page
            const currentPath = window.location.pathname;
            if (currentPath !== "/login" && currentPath !== "/register" && currentPath !== "/") {
                window.location.href = "/login";
            }
        }
        return Promise.reject(error);
    }
);

export default API;
