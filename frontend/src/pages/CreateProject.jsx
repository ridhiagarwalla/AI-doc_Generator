import { useState } from "react";
import { useNavigate } from "react-router-dom";
import API from "../api/axios";
import Navbar from "../components/Navbar";

export default function CreateProject() {
    const navigate = useNavigate();
    const [step, setStep] = useState(1);
    const [form, setForm] = useState({
        title: "",
        description: "",
        doc_type: "",
        topic: "",
        outline: [],
    });
    const [sectionTitle, setSectionTitle] = useState("");
    const [numSlides, setNumSlides] = useState(5);
    const [slideTitles, setSlideTitles] = useState([]);
    const [loading, setLoading] = useState(false);

    const handleSubmit = async (e) => {
        e.preventDefault();
        if (step === 1) {
            if (!form.title || !form.doc_type) {
                alert("Please fill in all required fields");
                return;
            }
            setStep(2);
        } else if (step === 2) {
            if (!form.topic) {
                alert("Please enter a topic");
                return;
            }
            setStep(3);
        } else if (step === 3) {
            // Create project
            setLoading(true);
            try {
                const projectData = {
                    title: form.title,
                    description: form.description,
                    doc_type: form.doc_type,
                    topic: form.topic,
                    outline: form.outline,
                };
                const res = await API.post("/projects", projectData);
                navigate(`/project/${res.data.id}/edit`);
            } catch (err) {
                alert("Error creating project: " + (err.response?.data?.detail || err.message));
            } finally {
                setLoading(false);
            }
        }
    };

    const addSection = () => {
        if (!sectionTitle.trim()) return;
        const newSection = {
            id: `section_${form.outline.length + 1}`,
            title: sectionTitle,
            order: form.outline.length + 1,
        };
        setForm({ ...form, outline: [...form.outline, newSection] });
        setSectionTitle("");
    };

    const removeSection = (index) => {
        const newOutline = form.outline.filter((_, i) => i !== index);
        setForm({ ...form, outline: newOutline });
    };

    const generateAIOutline = async () => {
        if (!form.topic) {
            alert("Please enter a topic first");
            return;
        }
        if (!form.title) {
            alert("Please enter a project title first");
            return;
        }
        if (!form.doc_type) {
            alert("Please select a document type first");
            return;
        }
        setLoading(true);
        try {
            // First create project with basic info
            const projectData = {
                title: form.title,
                description: form.description,
                doc_type: form.doc_type,
                topic: form.topic,
                outline: [],
            };
            const res = await API.post("/projects", projectData);
            const projectId = res.data.id;

            // Generate AI outline
            const outlineRes = await API.post(`/projects/${projectId}/ai-outline`, {
                topic: form.topic,
                doc_type: form.doc_type,
            });
            setForm({ ...form, outline: outlineRes.data.outline });
            setStep(3);
        } catch (err) {
            alert("Error generating outline: " + (err.response?.data?.detail || err.message));
        } finally {
            setLoading(false);
        }
    };

    const setupSlides = () => {
        const slides = [];
        for (let i = 0; i < numSlides; i++) {
            slides.push({
                id: `slide_${i + 1}`,
                title: slideTitles[i] || `Slide ${i + 1}`,
                order: i + 1,
            });
        }
        setForm({ ...form, outline: slides });
    };

    return (
        <div className="min-h-screen bg-gray-50">
            <Navbar />
            <div className="container mx-auto px-4 py-8 max-w-4xl">
                <div className="bg-white rounded-lg shadow-md p-8">
                    <div className="mb-6">
                        <div className="flex items-center justify-between mb-4">
                            <h2 className="text-2xl font-bold text-gray-800">Create New Project</h2>
                            <span className="text-sm text-gray-500">Step {step} of 3</span>
                        </div>
                        <div className="w-full bg-gray-200 rounded-full h-2">
                            <div
                                className="bg-blue-600 h-2 rounded-full transition-all"
                                style={{ width: `${(step / 3) * 100}%` }}
                            ></div>
                        </div>
                    </div>

            <form onSubmit={handleSubmit}>
                        {/* Step 1: Basic Info */}
                        {step === 1 && (
                            <div className="space-y-4">
                                <div>
                                    <label className="block text-sm font-medium text-gray-700 mb-2">
                                        Project Title *
                                    </label>
                                    <input
                                        type="text"
                                        value={form.title}
                                        onChange={(e) => setForm({ ...form, title: e.target.value })}
                                        className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
                                        placeholder="e.g., Market Analysis Report"
                                        required
                                    />
                                </div>

                                <div>
                                    <label className="block text-sm font-medium text-gray-700 mb-2">
                                        Description
                                    </label>
                                    <textarea
                                        value={form.description}
                                        onChange={(e) => setForm({ ...form, description: e.target.value })}
                                        className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
                                        rows="3"
                                        placeholder="Optional description"
                                    />
                                </div>

                                <div>
                                    <label className="block text-sm font-medium text-gray-700 mb-2">
                                        Document Type *
                                    </label>
                                    <div className="grid grid-cols-2 gap-4">
                                        <button
                                            type="button"
                                            onClick={() => setForm({ ...form, doc_type: "docx" })}
                                            className={`p-4 border-2 rounded-lg transition ${
                                                form.doc_type === "docx"
                                                    ? "border-blue-600 bg-blue-50"
                                                    : "border-gray-300 hover:border-gray-400"
                                            }`}
                                        >
                                            <div className="text-2xl mb-2">📄</div>
                                            <div className="font-semibold">Word Document</div>
                                            <div className="text-sm text-gray-600">.docx</div>
                                        </button>
                                        <button
                                            type="button"
                                            onClick={() => setForm({ ...form, doc_type: "pptx" })}
                                            className={`p-4 border-2 rounded-lg transition ${
                                                form.doc_type === "pptx"
                                                    ? "border-blue-600 bg-blue-50"
                                                    : "border-gray-300 hover:border-gray-400"
                                            }`}
                                        >
                                            <div className="text-2xl mb-2">📊</div>
                                            <div className="font-semibold">PowerPoint</div>
                                            <div className="text-sm text-gray-600">.pptx</div>
                                        </button>
                                    </div>
                                </div>
                            </div>
                        )}

                        {/* Step 2: Topic */}
                        {step === 2 && (
                            <div className="space-y-4">
                                <div>
                                    <label className="block text-sm font-medium text-gray-700 mb-2">
                                        Main Topic / Prompt *
                                    </label>
                                    <textarea
                                        value={form.topic}
                                        onChange={(e) => setForm({ ...form, topic: e.target.value })}
                                        className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
                                        rows="4"
                                        placeholder="e.g., A market analysis of the EV industry in 2025"
                                        required
                                    />
                                </div>
                            </div>
                        )}

                        {/* Step 3: Outline */}
                        {step === 3 && (
                            <div className="space-y-4">
                                {form.doc_type === "docx" ? (
                                    <div>
                                        <div className="flex justify-between items-center mb-4">
                                            <label className="block text-sm font-medium text-gray-700">
                                                Document Sections
                                            </label>
                                            <button
                                                type="button"
                                                onClick={generateAIOutline}
                                                className="text-sm bg-purple-600 text-white px-4 py-2 rounded hover:bg-purple-700 transition"
                                                disabled={loading}
                                            >
                                                {loading ? "Generating..." : "✨ AI Suggest Outline"}
                                            </button>
                                        </div>

                                        <div className="flex gap-2 mb-4">
                                            <input
                                                type="text"
                                                value={sectionTitle}
                                                onChange={(e) => setSectionTitle(e.target.value)}
                                                onKeyPress={(e) => e.key === "Enter" && (e.preventDefault(), addSection())}
                                                className="flex-1 px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
                                                placeholder="Enter section title"
                                            />
                                            <button
                                                type="button"
                                                onClick={addSection}
                                                className="bg-blue-600 text-white px-6 py-2 rounded-lg hover:bg-blue-700 transition"
                                            >
                                                Add Section
                                            </button>
                                        </div>

                                        <div className="space-y-2">
                                            {form.outline.map((section, index) => (
                                                <div
                                                    key={index}
                                                    className="flex items-center justify-between p-3 bg-gray-50 rounded-lg"
                                                >
                                                    <span className="font-medium">{section.title}</span>
                                                    <button
                                                        type="button"
                                                        onClick={() => removeSection(index)}
                                                        className="text-red-600 hover:text-red-800"
                                                    >
                                                        Remove
                                                    </button>
                                                </div>
                                            ))}
                                        </div>
                                    </div>
                                ) : (
                                    <div>
                                        <label className="block text-sm font-medium text-gray-700 mb-2">
                                            Number of Slides
                                        </label>
                                        <input
                                            type="number"
                                            min="1"
                                            max="20"
                                            value={numSlides}
                                            onChange={(e) => {
                                                const num = parseInt(e.target.value) || 5;
                                                setNumSlides(num);
                                                const newTitles = Array(num).fill("").map((_, i) => slideTitles[i] || `Slide ${i + 1}`);
                                                setSlideTitles(newTitles);
                                            }}
                                            className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent mb-4"
                                        />

                                        <div className="space-y-2 mb-4">
                                            {Array(numSlides)
                                                .fill(0)
                                                .map((_, i) => (
                                                    <input
                                                        key={i}
                                                        type="text"
                                                        value={slideTitles[i] || `Slide ${i + 1}`}
                                                        onChange={(e) => {
                                                            const newTitles = [...slideTitles];
                                                            newTitles[i] = e.target.value;
                                                            setSlideTitles(newTitles);
                                                        }}
                                                        className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
                                                        placeholder={`Slide ${i + 1} title`}
                                                    />
                                                ))}
                                        </div>

                                        <button
                                            type="button"
                                            onClick={setupSlides}
                                            className="w-full bg-blue-600 text-white px-6 py-2 rounded-lg hover:bg-blue-700 transition mb-4"
                                        >
                                            Confirm Slides
                                        </button>

                                        {form.outline.length > 0 && (
                                            <div className="space-y-2">
                                                {form.outline.map((slide, index) => (
                                                    <div
                                                        key={index}
                                                        className="p-3 bg-gray-50 rounded-lg"
                                                    >
                                                        {slide.title}
                                                    </div>
                                                ))}
                                            </div>
                                        )}
                                    </div>
                                )}
                            </div>
                        )}

                        <div className="flex justify-between mt-8">
                            {step > 1 && (
                                <button
                                    type="button"
                                    onClick={() => setStep(step - 1)}
                                    className="px-6 py-2 border border-gray-300 rounded-lg hover:bg-gray-50 transition"
                                >
                                    Previous
                                </button>
                            )}
                            <div className="ml-auto">
                                {step < 3 ? (
                                    <button
                                        type="submit"
                                        className="px-6 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700 transition"
                                    >
                                        Next
                                    </button>
                                ) : (
                                    <button
                                        type="submit"
                                        disabled={loading || form.outline.length === 0}
                                        className="px-6 py-2 bg-green-600 text-white rounded-lg hover:bg-green-700 transition disabled:bg-gray-400"
                                    >
                                        {loading ? "Creating..." : "Create Project"}
                                    </button>
                                )}
                            </div>
                        </div>
            </form>
                </div>
            </div>
        </div>
    );
}
