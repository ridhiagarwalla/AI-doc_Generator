import { useEffect, useState } from "react";
import { useParams, useNavigate, Link } from "react-router-dom";
import API from "../api/axios";
import Navbar from "../components/Navbar";

export default function ProjectEditor() {
    const { id } = useParams();
    const navigate = useNavigate();
    const [project, setProject] = useState(null);
    const [loading, setLoading] = useState(true);
    const [generating, setGenerating] = useState(false);
    const [refining, setRefining] = useState({});
    const [refinementPrompts, setRefinementPrompts] = useState({});
    const [comments, setComments] = useState({});
    const [feedback, setFeedback] = useState({});

    useEffect(() => {
        loadProject();
    }, [id]);

    const loadProject = async () => {
        try {
            const res = await API.get(`/projects/${id}`);
            setProject(res.data);
            
            // Initialize feedback and comments from project data
            if (res.data.feedback) {
                setFeedback(res.data.feedback);
            }
        } catch (err) {
            alert("Error loading project");
            navigate("/projects");
        } finally {
            setLoading(false);
        }
    };

    const generateContent = async () => {
        setGenerating(true);
        try {
            await API.post(`/projects/${id}/generate`);
            await loadProject();
            alert("Content generated successfully!");
        } catch (err) {
            alert("Error generating content: " + (err.response?.data?.detail || err.message));
        } finally {
            setGenerating(false);
        }
    };

    const refineSection = async (sectionId) => {
        if (!refinementPrompts[sectionId]?.trim()) {
            alert("Please enter a refinement prompt");
            return;
        }
        setRefining({ ...refining, [sectionId]: true });
        try {
            await API.post(`/projects/${id}/refine`, {
                section_id: sectionId,
                refinement_prompt: refinementPrompts[sectionId],
            });
            await loadProject();
            setRefinementPrompts({ ...refinementPrompts, [sectionId]: "" });
            alert("Content refined successfully!");
        } catch (err) {
            alert("Error refining content: " + (err.response?.data?.detail || err.message));
        } finally {
            setRefining({ ...refining, [sectionId]: false });
        }
    };

    const submitFeedback = async (sectionId, like) => {
        try {
            await API.post(`/projects/${id}/feedback`, {
                section_id: sectionId,
                like: like,
            });
            setFeedback({ ...feedback, [sectionId]: { ...feedback[sectionId], like } });
        } catch (err) {
            console.error("Error submitting feedback:", err);
        }
    };

    const submitComment = async (sectionId) => {
        if (!comments[sectionId]?.trim()) return;
        try {
            await API.post(`/projects/${id}/feedback`, {
                section_id: sectionId,
                comment: comments[sectionId],
            });
            await loadProject();
            setComments({ ...comments, [sectionId]: "" });
        } catch (err) {
            alert("Error submitting comment");
        }
    };

    const exportDocument = async (format) => {
        try {
            const res = await API.get(`/projects/${id}/export/${format}`, {
                responseType: "blob",
            });
            
            const url = window.URL.createObjectURL(new Blob([res.data]));
            const link = document.createElement("a");
            link.href = url;
            link.setAttribute("download", `${project.title}.${format}`);
            document.body.appendChild(link);
            link.click();
            link.remove();
        } catch (err) {
            alert("Error exporting document: " + (err.response?.data?.detail || err.message));
        }
    };

    if (loading) {
        return (
            <div className="min-h-screen bg-gray-50">
                <Navbar />
                <div className="container mx-auto px-4 py-8">
                    <p>Loading project...</p>
                </div>
            </div>
        );
    }

    if (!project) {
        return null;
    }

    return (
        <div className="min-h-screen bg-gray-50">
            <Navbar />
            <div className="container mx-auto px-4 py-8 max-w-6xl">
                <div className="mb-6 flex justify-between items-center">
                    <div>
                        <h1 className="text-3xl font-bold text-gray-800">{project.title}</h1>
                        {project.topic && (
                            <p className="text-gray-600 mt-2">{project.topic}</p>
                        )}
                    </div>
                    <div className="flex gap-2">
                        <button
                            onClick={() => exportDocument(project.doc_type)}
                            className="bg-green-600 text-white px-6 py-2 rounded-lg hover:bg-green-700 transition"
                        >
                            Export {project.doc_type?.toUpperCase()}
                        </button>
                        <Link
                            to="/projects"
                            className="bg-gray-600 text-white px-6 py-2 rounded-lg hover:bg-gray-700 transition"
                        >
                            Back to Projects
                        </Link>
                    </div>
                </div>

                {!project.content || Object.keys(project.content).length === 0 ? (
                    <div className="bg-white rounded-lg shadow-md p-8 text-center">
                        <p className="text-gray-600 mb-4">
                            No content generated yet. Click the button below to generate content for all sections.
                        </p>
                        <button
                            onClick={generateContent}
                            disabled={generating}
                            className="bg-blue-600 text-white px-6 py-2 rounded-lg hover:bg-blue-700 transition disabled:bg-gray-400"
                        >
                            {generating ? "Generating..." : "Generate Content"}
                        </button>
                    </div>
                ) : (
                    <div className="space-y-6">
                        {project.outline.map((item, index) => {
                            const sectionId = item.id || item.title?.toLowerCase().replace(" ", "_");
                            const sectionContent = project.content[sectionId];
                            
                            return (
                                <div key={index} className="bg-white rounded-lg shadow-md p-6">
                                    <h2 className="text-2xl font-semibold text-gray-800 mb-4">
                                        {item.title || item.name}
                                    </h2>

                                    {sectionContent ? (
                                        <>
                                            <div className="mb-4 p-4 bg-gray-50 rounded-lg">
                                                <div className="whitespace-pre-wrap text-gray-700">
                                                    {sectionContent.content}
                                                </div>
                                            </div>

                                            {/* Refinement Section */}
                                            <div className="border-t pt-4 mt-4">
                                                <label className="block text-sm font-medium text-gray-700 mb-2">
                                                    Refine with AI
                                                </label>
                                                <div className="flex gap-2 mb-4">
                                                    <input
                                                        type="text"
                                                        value={refinementPrompts[sectionId] || ""}
                                                        onChange={(e) =>
                                                            setRefinementPrompts({
                                                                ...refinementPrompts,
                                                                [sectionId]: e.target.value,
                                                            })
                                                        }
                                                        className="flex-1 px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
                                                        placeholder="e.g., Make this more formal, Convert to bullet points, Shorten to 100 words"
                                                    />
                                                    <button
                                                        onClick={() => refineSection(sectionId)}
                                                        disabled={refining[sectionId]}
                                                        className="bg-purple-600 text-white px-6 py-2 rounded-lg hover:bg-purple-700 transition disabled:bg-gray-400"
                                                    >
                                                        {refining[sectionId] ? "Refining..." : "Refine"}
                                                    </button>
                                                </div>

                                                {/* Feedback Section */}
                                                <div className="flex items-center gap-4 mb-4">
                                                    <span className="text-sm font-medium text-gray-700">Feedback:</span>
                                                    <button
                                                        onClick={() => submitFeedback(sectionId, true)}
                                                        className={`px-4 py-2 rounded ${
                                                            feedback[sectionId]?.like === true
                                                                ? "bg-green-600 text-white"
                                                                : "bg-gray-200 text-gray-700 hover:bg-gray-300"
                                                        }`}
                                                    >
                                                        👍 Like
                                                    </button>
                                                    <button
                                                        onClick={() => submitFeedback(sectionId, false)}
                                                        className={`px-4 py-2 rounded ${
                                                            feedback[sectionId]?.like === false
                                                                ? "bg-red-600 text-white"
                                                                : "bg-gray-200 text-gray-700 hover:bg-gray-300"
                                                        }`}
                                                    >
                                                        👎 Dislike
                                                    </button>
                                                </div>

                                                {/* Comments Section */}
                                                <div>
                                                    <label className="block text-sm font-medium text-gray-700 mb-2">
                                                        Add Comment
                                                    </label>
                                                    <div className="flex gap-2">
                                                        <input
                                                            type="text"
                                                            value={comments[sectionId] || ""}
                                                            onChange={(e) =>
                                                                setComments({
                                                                    ...comments,
                                                                    [sectionId]: e.target.value,
                                                                })
                                                            }
                                                            onKeyPress={(e) => {
                                                                if (e.key === "Enter") {
                                                                    submitComment(sectionId);
                                                                }
                                                            }}
                                                            className="flex-1 px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
                                                            placeholder="Enter your comment..."
                                                        />
                                                        <button
                                                            onClick={() => submitComment(sectionId)}
                                                            className="bg-blue-600 text-white px-6 py-2 rounded-lg hover:bg-blue-700 transition"
                                                        >
                                                            Add
                                                        </button>
                                                    </div>
                                                    {feedback[sectionId]?.comments && (
                                                        <div className="mt-2 space-y-1">
                                                            {feedback[sectionId].comments.map((comment, idx) => (
                                                                <div key={idx} className="text-sm text-gray-600 bg-gray-50 p-2 rounded">
                                                                    {comment.comment}
                                                                </div>
                                                            ))}
                                                        </div>
                                                    )}
                                                </div>
                                            </div>
                                        </>
                                    ) : (
                                        <div className="text-gray-500 italic">Content not generated yet</div>
                                    )}
                                </div>
                            );
                        })}

                        <div className="bg-white rounded-lg shadow-md p-6">
                            <button
                                onClick={generateContent}
                                disabled={generating}
                                className="bg-blue-600 text-white px-6 py-2 rounded-lg hover:bg-blue-700 transition disabled:bg-gray-400"
                            >
                                {generating ? "Regenerating..." : "Regenerate All Content"}
                            </button>
                        </div>
                    </div>
                )}
            </div>
        </div>
    );
}

