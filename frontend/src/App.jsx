import { BrowserRouter, Routes, Route } from "react-router-dom";
import Login from "./pages/login";
import Register from "./pages/Register";
import Dashboard from "./pages/Dashboard";
import CreateProject from "./pages/CreateProject";
import ProjectEditor from "./pages/ProjectEditor";

function App() {
    return (
        <BrowserRouter>
            <Routes>
                <Route path="/" element={<Login />} />
                <Route path="/login" element={<Login />} />
                <Route path="/register" element={<Register />} />
                <Route path="/projects" element={<Dashboard />} />
                <Route path="/create" element={<CreateProject />} />
                <Route path="/project/:id/edit" element={<ProjectEditor />} />
            </Routes>
        </BrowserRouter>
    );
}

export default App;
