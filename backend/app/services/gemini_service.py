import os
import requests
from ..config import OPENROUTER_API_KEY

# Check if OpenRouter API key is configured
_configured = False
if OPENROUTER_API_KEY:
    _configured = True
    print("✅ OpenRouter API configured")
else:
    print("⚠️  Warning: OPENROUTER_API_KEY not set. AI features will not work.")

def _call_openrouter(prompt: str) -> str:
    """
    Call OpenRouter API to generate text
    """
    if not OPENROUTER_API_KEY or not _configured:
        raise Exception("OPENROUTER_API_KEY not configured")
    
    url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json",
        "HTTP-Referer": "http://localhost:8000",  # Optional: for analytics
        "X-Title": "AI Document Generator"  # Optional: for analytics
    }
    
    data = {
        "model": "google/gemini-flash-1.5",  # FREE model via OpenRouter
        "messages": [{"role": "user", "content": prompt}]
    }
    
    try:
        response = requests.post(url, headers=headers, json=data, timeout=60)
        response.raise_for_status()
        result = response.json()
        return result["choices"][0]["message"]["content"]
    except requests.exceptions.RequestException as e:
        raise Exception(f"OpenRouter API error: {str(e)}")
    except (KeyError, IndexError) as e:
        raise Exception(f"Invalid response from OpenRouter API: {str(e)}")

def generate_content(topic: str, section_title: str, doc_type: str, existing_content: str = None) -> str:
    """
    Generate content for a section or slide using OpenRouter API
    """
    if not OPENROUTER_API_KEY or not _configured:
        return f"[Error: OPENROUTER_API_KEY not configured. Please set your OpenRouter API key in the .env file.]\n\nSection: {section_title}\nTopic: {topic}\n\nThis is placeholder content. Please configure your OPENROUTER_API_KEY to generate real content."
    
    try:
        if doc_type == "docx":
            prompt = f"""You are a professional document writer. Write a comprehensive section for a document.

Topic: {topic}
Section Title: {section_title}

Write detailed, well-structured content for this section. Include:
- Clear introduction to the section
- Main points and explanations
- Supporting details
- Conclusion or transition to next section

Write approximately 300-500 words. Make it professional and informative."""
        else:  # pptx
            prompt = f"""You are a professional presentation writer. Write content for a PowerPoint slide.

Topic: {topic}
Slide Title: {section_title}

Write concise, engaging content for this slide. Include:
- Key points (3-5 bullet points)
- Brief explanations
- Actionable insights

Keep it concise (100-200 words) suitable for a presentation slide."""
        
        if existing_content:
            prompt += f"\n\nCurrent content:\n{existing_content}\n\nRefine and improve this content based on the above requirements."
        
        return _call_openrouter(prompt)
    except Exception as e:
        # Fallback if API fails
        error_msg = str(e)
        return f"[Error generating content: {error_msg}]\n\nSection: {section_title}\nTopic: {topic}\n\nPlease check your OPENROUTER_API_KEY and API quota."

def refine_content(original_content: str, refinement_prompt: str, topic: str, section_title: str) -> str:
    """
    Refine existing content based on user prompt using OpenRouter API
    """
    if not OPENROUTER_API_KEY or not _configured:
        return f"[Error: OPENROUTER_API_KEY not configured.]\n\n{original_content}"
    
    try:
        prompt = f"""You are a professional document editor. Refine the following content based on the user's request.

Topic: {topic}
Section Title: {section_title}
Original Content:
{original_content}

User's Refinement Request: {refinement_prompt}

Please refine the content according to the user's request while maintaining the core message and professional tone."""
        
        return _call_openrouter(prompt)
    except Exception as e:
        error_msg = str(e)
        return f"[Error refining content: {error_msg}]\n\nOriginal content:\n{original_content}"

def generate_outline(topic: str, doc_type: str) -> list:
    """
    Generate outline (sections or slides) using OpenRouter API
    """
    if not OPENROUTER_API_KEY or not _configured:
        # Return default outline if API key not configured
        if doc_type == "docx":
            return ["Introduction", "Background", "Main Content", "Analysis", "Conclusion"]
        else:
            return ["Introduction", "Overview", "Key Points", "Details", "Conclusion"]
    
    try:
        if doc_type == "docx":
            prompt = f"""Generate a comprehensive document outline for the following topic.

Topic: {topic}

Provide 5-7 section headers that would make a complete document. Return ONLY a JSON array of strings, each string being a section title. Example format: ["Introduction", "Background", "Analysis", "Findings", "Conclusion"]

Do not include any other text, only the JSON array."""
        else:  # pptx
            prompt = f"""Generate a presentation outline for the following topic.

Topic: {topic}

Provide 8-12 slide titles that would make a complete presentation. Return ONLY a JSON array of strings, each string being a slide title. Example format: ["Introduction", "Overview", "Key Points", "Analysis", "Conclusion"]

Do not include any other text, only the JSON array."""
        
        text = _call_openrouter(prompt).strip()
        
        # Try to extract JSON from response
        import json
        import re
        
        # Find JSON array in response
        json_match = re.search(r'\[.*\]', text, re.DOTALL)
        if json_match:
            outline = json.loads(json_match.group())
            return outline
        
        # Fallback: split by lines and clean
        lines = [line.strip().strip('"').strip("'") for line in text.split('\n') if line.strip()]
        return lines[:12] if doc_type == "pptx" else lines[:7]
        
    except Exception as e:
        # Return default outline
        if doc_type == "docx":
            return ["Introduction", "Background", "Main Content", "Analysis", "Conclusion"]
        else:
            return ["Introduction", "Overview", "Key Points", "Details", "Conclusion"]

