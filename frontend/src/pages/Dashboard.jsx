import { useEffect, useState } from "react";
import { useNavigate, Link } from "react-router-dom";
import API from "../api/axios";
import Navbar from "../components/Navbar";

export default function Dashboard() {
    const navigate = useNavigate();
    const [projects, setProjects] = useState([]);
    const [loading, setLoading] = useState(true);

    const loadProjects = async () => {
        try {
            const res = await API.get("/projects");
            setProjects(res.data);
        } catch (err) {
            console.error("Error loading projects:", err);
        } finally {
            setLoading(false);
        }
    };

    const deleteProject = async (id) => {
        if (!window.confirm("Are you sure you want to delete this project?")) {
            return;
        }
        try {
            await API.delete(`/projects/${id}`);
            loadProjects();
        } catch (err) {
            alert("Error deleting project");
        }
    };

    useEffect(() => {
        loadProjects();
    }, []);

    if (loading) {
        return (
            <div className="min-h-screen bg-gray-50">
                <Navbar />
                <div className="container mx-auto px-4 py-8">
                    <p>Loading projects...</p>
                </div>
            </div>
        );
    }

    return (
        <div className="min-h-screen bg-gray-50">
            <Navbar />
            <div className="container mx-auto px-4 py-8">
                <div className="flex justify-between items-center mb-6">
                    <h1 className="text-3xl font-bold text-gray-800">Your Projects</h1>
                    <Link
                        to="/create"
                        className="bg-blue-600 text-white px-6 py-2 rounded-lg hover:bg-blue-700 transition"
                    >
                        + Create New Project
                    </Link>
                </div>

                {projects.length === 0 ? (
                    <div className="bg-white rounded-lg shadow p-8 text-center">
                        <p className="text-gray-600 mb-4">No projects yet. Create your first project!</p>
                        <Link
                            to="/create"
                            className="inline-block bg-blue-600 text-white px-6 py-2 rounded-lg hover:bg-blue-700 transition"
                        >
                            Create Project
                        </Link>
                    </div>
                ) : (
                    <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
                        {projects.map((project) => (
                            <div
                                key={project.id}
                                className="bg-white rounded-lg shadow-md p-6 hover:shadow-lg transition"
                            >
                                <div className="flex justify-between items-start mb-4">
                                    <h2 className="text-xl font-semibold text-gray-800">{project.title}</h2>
                                    <span className="bg-blue-100 text-blue-800 text-xs px-2 py-1 rounded">
                                        {project.doc_type?.toUpperCase() || "DOC"}
                                    </span>
                                </div>
                                
                                {project.topic && (
                                    <p className="text-gray-600 text-sm mb-4 line-clamp-2">{project.topic}</p>
                                )}
                                
                                {project.description && (
                                    <p className="text-gray-500 text-sm mb-4">{project.description}</p>
                                )}

                                <div className="flex gap-2 mt-4">
                                    <Link
                                        to={`/project/${project.id}/edit`}
                                        className="flex-1 bg-blue-600 text-white text-center px-4 py-2 rounded hover:bg-blue-700 transition"
                                    >
                                        Open
                                    </Link>
                                    <button
                                        onClick={() => deleteProject(project.id)}
                                        className="bg-red-600 text-white px-4 py-2 rounded hover:bg-red-700 transition"
                                    >
                                        Delete
                                    </button>
                                </div>
                            </div>
                        ))}
                    </div>
                )}
            </div>
        </div>
    );
}

