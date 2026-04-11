import os
from build_site import HTML_TEMPLATE, CHAPTER_TEMPLATE

chapters4 = [
    {
        "id": 16,
        "phase": "Phase 4: Production & Beyond",
        "title": "The LLM Factory",
        "simple_explanation": "<p>Building a cool AI space station in your garage is fun, but launching it into orbit so 10,000 people can use it at once is a completely different challenge. MLOps (or LLMOps) is the factory you build around your model. It involves automated conveyor belts (Data Pipelines), quality checks (Evaluation), and delivery trucks (Deployment) to ensure the AI doesn't crash when real users touch it.</p>",
        "going_deeper": "<p>LLMOps encompasses tracking experiments (e.g., Weights & Biases), managing datasets, versioning prompts, and CI/CD for machine learning. Because LLMs are so massive, deploying them requires managing GPU orchestration (using Kubernetes or specialized platforms like Ray). The pipeline also monitors for 'data drift', where the model's accuracy degrades as real-world input changes over time.</p>",
        "aha_moment": "The model is only 10% of the work. 90% is the infrastructure required to feed data into it and serve it to users reliably and at scale.",
        "real_world": "<p>When ChatGPT handles 100 million active users flawlessly, it's not because the model is magically stable; it's because OpenAI has world-class LLMOps distributing load across server farms.</p>",
        "references": "<em>LLM Engineer's Handbook</em> (Iusztin & Labonne); <em>LLMs in Production</em> (Brousseau & Sharp)"
    },
    {
        "id": 17,
        "phase": "Phase 4: Production & Beyond",
        "title": "Making It Fast",
        "simple_explanation": "<p>Imagine trying to squeeze a massive 18-wheeler truck (an LLM) onto a tiny one-lane farm road (a computer's memory). It won't fit. But if you carefully compress the cargo and use clever shortcuts, you can make the delivery. Inference optimization is the science of making these gigantic models run lightning-fast, sometimes even squeezing them onto a laptop or Raspberry Pi.</p>",
        "going_deeper": "<p>Two primary techniques dominate: <strong>Quantization</strong> and <strong>KV Caching</strong>. Quantization reduces the precision of the model's weights (e.g., from 32-bit floats to 4-bit integers), drastically shrinking memory usage with minimal accuracy loss. KV (Key-Value) Caching prevents the model from re-calculating the entire attention matrix for previously written tokens during generation, massively speeding up the output.</p>",
        "aha_moment": "You don't always need a $40,000 GPU server. With aggressive quantization, state-of-the-art models can run completely offline on a smartphone.",
        "real_world": "<p>Open-source models like Llama 3 are commonly quantized using formats like GGUF, enabling millions of developers to run them locally on MacBooks using tools like Ollama.</p>",
        "references": "<em>LLMs in Production</em> (Brousseau & Sharp); <em>Build a Large Language Model (From Scratch)</em> (Raschka); <em>LLM Engineer's Handbook</em> (Iusztin & Labonne)"
    },
    {
        "id": 18,
        "phase": "Phase 4: Production & Beyond",
        "title": "Is It Any Good?",
        "simple_explanation": "<p>If you build a calculator, it's easy to test: 2+2 is always 4. But how do you grade an AI that writes poetry, summarizes meetings, or tells jokes? There is no single 'correct' answer. Evaluating LLMs requires a mix of clever automated tests and a panel of human judges giving thumbs up or thumbs down to figure out if the AI is actually helpful or just hallucinating.</p>",
        "going_deeper": "<p>Evaluation uses metrics ranging from statistical to human-driven. <strong>Perplexity</strong> measures how 'surprised' a model is by standard text (lower is better). <strong>BLEU</strong> and <strong>ROUGE</strong> compare AI output to human reference texts. The modern gold standard, however, is 'LLM-as-a-Judge', where a stronger, more expensive model (like GPT-4) is prompted to grade the output of a cheaper model based on a rubric.</p>",
        "aha_moment": "Because deterministic math can't judge art or reasoning, the most effective way to grade an AI today is to use an even smarter AI as the teacher.",
        "real_world": "<p>The Hugging Face 'Open LLM Leaderboard' evaluates thousands of models on standardized tests (like MMLU, which tests high school and college level knowledge) to rank the best open source models.</p>",
        "references": "<em>Building LLMs for Production</em> (Bouchard); <em>LLMs in Production</em> (Brousseau & Sharp)"
    },
    {
        "id": 19,
        "phase": "Phase 4: Production & Beyond",
        "title": "The Guardrails",
        "simple_explanation": "<p>If you give an AI the entire internet to read, it will learn the best of humanity, but also the worst—toxicity, bias, and dangerous instructions. Putting 'Guardrails' on an AI is like putting bowling bumpers on the lane. No matter what the user types to try and trick the AI (a 'jailbreak'), the guardrails force the AI to bounce back and provide a safe, ethical, and polite refusal.</p>",
        "going_deeper": "<p>Safety involves multiple layers. <strong>Alignment</strong> is done during RLHF training to make the model inherently safer. <strong>Input/Output Guardrails</strong> are secondary, specialized models (like Llama Guard) sitting between the user and the LLM. They classify the user's prompt or the LLM's response for toxicity, PII (Personally Identifiable Information), or prompt-injections, blocking the transaction if rules are violated.</p>",
        "aha_moment": "Security in AI is a cat-and-mouse game. As models get smarter, the prompts designed to break their rules (jailbreaks) also become incredibly complex algorithmic puzzles.",
        "real_world": "<p>When you ask an AI for malicious code and it responds, 'I'm sorry, but I cannot fulfill this request,' a safety classifier successfully caught the violation and triggered a canned refusal.</p>",
        "references": "<em>Large Language Models</em> (Raaijmakers); <em>Creating Custom GPT with OpenAI GPT Builder</em> (Russell etc.)"
    },
    {
        "id": 20,
        "phase": "Phase 4: Production & Beyond",
        "title": "What's Next?",
        "simple_explanation": "<p>Right now, LLMs are incredible text-processing engines. But the world isn't just text. The future is an AI that can see a live video feed, hear your voice, control a robotic arm, and reason about a problem for three days before giving you a brilliant answer. The ultimate target is AGI (Artificial General Intelligence)—a system that can do any intellectual task a human can do.</p>",
        "going_deeper": "<p>The frontier is largely focused on two areas: <strong>Multimodality</strong> (models natively understanding text, audio, images, and video simultaneously without separate models) and <strong>System 2 Thinking/Agents</strong> (giving models the architecture to stop, search, plan, and verify recursively). The debate continues on whether scaling current Transformer architectures will achieve AGI, or if a completely new paradigm is needed.</p>",
        "aha_moment": "We are teaching rocks to not just talk, but to see, hear, and build their own tools. We are orchestrating the fastest technological evolution in human history.",
        "real_world": "<p>When an AI can autonomously review a codebase, open a pull request, test it, and deploy it to production while fixing its own bugs—all while you sleep—that is the agentic future currently being built.</p>",
        "references": "<em>Large Language Models</em> (Raaijmakers); <em>LLMs in Production</em> (Brousseau & Sharp); <em>Creating Custom GPT with OpenAI GPT Builder</em> (Russell etc.)"
    }
]

def append_html_4():
    with open('index.html', 'r') as f:
        html = f.read()
    
    parts_nav = html.split('        </ul>')
    nav_injection = ""
    for ch in chapters4:
        nav_injection += f'            <li><a href="#ch{ch["id"]}">Ch {ch["id"]}: {ch["title"]}</a></li>\n'
    html = parts_nav[0] + nav_injection + '        </ul>' + parts_nav[1]
    
    parts_content = html.split('    </main>')
    content_injection = ""
    for ch in chapters4:
        content_injection += CHAPTER_TEMPLATE.format(**ch)
    html = parts_content[0] + content_injection + '    </main>' + parts_content[1]
    
    with open('index.html', 'w') as f:
        f.write(html)
    print("Site updated with chapters 16-20 successfully!")

if __name__ == "__main__":
    append_html_4()
