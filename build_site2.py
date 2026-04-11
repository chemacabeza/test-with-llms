import os
from build_site import HTML_TEMPLATE, CHAPTER_TEMPLATE

chapters2 = [
    {
        "id": 6,
        "phase": "Phase 2: Making LLMs Useful",
        "title": "Teaching Old Models New Tricks",
        "simple_explanation": "<p>Imagine someone who has read the whole internet but has never been a doctor. You wouldn't trust them with your health. But what if you locked them in a room with only medical textbooks for a week? They'd become amazing at medical questions. Fine-tuning takes a general-purpose brain and gives it specialized training, making it an expert at a specific job like coding or writing legal contracts.</p>",
        "going_deeper": "<p><strong>Supervised Fine-Tuning (SFT)</strong> takes a pretrained model and trains it further on high-quality input-output pairs. Because training all parameters is expensive, engineers often use <strong>LoRA (Low-Rank Adaptation)</strong>, which freezes the original weights and only trains small 'adapter' layers, allowing fine-tuning on a single GPU.</p>",
        "aha_moment": "Pretraining gives the model raw intelligence; Fine-Tuning gives the model a profession.",
        "real_world": "<p>When a hospital uses a medical AI that safely summarizes patient records without hallucinating, it's using a model specifically fine-tuned on medical documents.</p>",
        "references": "<em>Build a Large Language Model (From Scratch)</em> (Raschka); <em>LLM Engineer's Handbook</em> (Iusztin & Labonne); <em>Building LLMs for Production</em> (Bouchard)"
    },
    {
        "id": 7,
        "phase": "Phase 2: Making LLMs Useful",
        "title": "Learning From Humans",
        "simple_explanation": "<p>Let's say a chef learns a thousand recipes (Pretraining), but doesn't know what customers actually <em>like</em>. So, the chef cooks two versions of a dish and asks a customer, 'Which is better?' Over time, the chef learns exactly how to please the crowd. This feedback loop makes the chef polite, helpful, and safe. For AI, we call this RLHF (Reinforcement Learning from Human Feedback).</p>",
        "going_deeper": "<p><strong>RLHF</strong> uses a separate 'Reward Model' trained on human preferences. The main model generates multiple answers, the reward model scores them, and the main model updates its policy using algorithms like PPO (Proximal Policy Optimization) to maximize the reward. Newer methods like DPO (Direct Preference Optimization) simplify this by skipping the reward model entirely.</p>",
        "aha_moment": "An LLM naturally wants to complete the internet's text (including toxic parts). RLHF aligns the model to act like a helpful assistant instead of an unhinged autocomplete.",
        "real_world": "<p>The biggest difference between GPT-3 (impressive but hard to use) and ChatGPT (a helpful assistant everyone loves) was the introduction of massive-scale RLHF.</p>",
        "references": "<em>Build a Large Language Model (From Scratch)</em> (Raschka); <em>Large Language Models</em> (Raaijmakers)"
    },
    {
        "id": 8,
        "phase": "Phase 2: Making LLMs Useful",
        "title": "The Art of Asking",
        "simple_explanation": "<p>Talking to an LLM is like giving instructions to an incredibly smart alien who takes everything literally. If you say, 'Tell me about dogs', they might write a 10-page essay or a 3-word poem. Prompt Engineering is the art of giving the alien perfect instructions: 'You are a vet (Role). In 3 bullet points (Format), explain what dogs eat (Task), using simple words (Tone).'</p>",
        "going_deeper": "<p>Effective prompting relies on providing context and constraints. <strong>Zero-shot</strong> prompting gives no examples. <strong>Few-shot</strong> prompting provides examples within the prompt to set the pattern. You can also adjust sampling controls: <strong>Temperature</strong> (how creative/random the output is), and <strong>Top-K / Top-P</strong> parameter tuning to control token selection probability.</p>",
        "aha_moment": "The model's output is only as good as your input. Programming with natural language requires just as much precision as programming in Python or C++.",
        "real_world": "<p>When companies build AI customer service bots, they write massive 'System Prompts' hidden from the user that dictate exactly how the bot should behave and what it shouldn't say.</p>",
        "references": "<em>Google Prompt Engineering</em> (Boonstra); <em>Creating Custom GPT with OpenAI GPT Builder</em> (Russell etc.)"
    },
    {
        "id": 9,
        "phase": "Phase 2: Making LLMs Useful",
        "title": "Thinking Step by Step",
        "simple_explanation": "<p>If I ask you 'What is 342 times 18?', you can't just blurt out the answer instantly. You need scratchpad paper to do the math step-by-step. LLMs normally try to blurt out answers instantly too, which leads to mistakes in logic. By explicitly telling the LLM to 'think step by step', you force it to use its generated output as a scratchpad, magically improving its reasoning abilities.</p>",
        "going_deeper": "<p>This is called <strong>Chain of Thought (CoT)</strong> prompting. Advanced versions include <strong>Tree of Thoughts (ToT)</strong>, where the model explores multiple paths simultaneously and discards bad ones, or <strong>Self-Consistency</strong>, where the model generates 10 different reasoning paths and takes the majority vote.</p>",
        "aha_moment": "Because an LLM's 'thinking' happens while it writes tokens, forcing it to write more tokens between the question and the answer literally gives it more compute time to think.",
        "real_world": "<p>Newer reasoning models (like OpenAI's o1 series) have this step-by-step thinking built directly into their architecture, hiding the 'scratchpad' from the user.</p>",
        "references": "<em>Google Prompt Engineering</em> (Boonstra); <em>Building LLMs for Production</em> (Bouchard)"
    },
    {
        "id": 10,
        "phase": "Phase 2: Making LLMs Useful",
        "title": "Giving LLMs a Library Card",
        "simple_explanation": "<p>Imagine a very smart but forgetful student taking an open-book test. They can't remember the exact dates or facts, but if you hand them the exact textbook chapter, they can write a perfect essay. RAG (Retrieval-Augmented Generation) is precisely this. Instead of expecting the LLM to memorize your company's data, you search your documents, hand the relevant paragraphs to the LLM, and say 'Answer the user using only this text.'</p>",
        "going_deeper": "<p>A RAG pipeline involves taking your documents, cutting them into small 'chunks', creating <strong>embeddings</strong> for them, and storing them in a <strong>Vector Database</strong>. When a user asks a question, the system converts the question to an embedding, finds the most mathematically similar chunks in the DB, and injects them into the prompt window before sending to the LLM.</p>",
        "aha_moment": "RAG completely solves the 'brain drain' problem. To update the model's knowledge, you don't need to retrain it; you just upload a new file to the database.",
        "real_world": "<p>Almost every enterprise 'Chat with our Docs' application or internal company wiki bot is built using RAG architecture to prevent hallucinations and keep data current.</p>",
        "references": "<em>LLM Engineer's Handbook</em> (Iusztin & Labonne); <em>Learning LangChain</em> (Oshin & Campos)"
    }
]

def append_html():
    with open('index.html', 'r') as f:
        html = f.read()
    
    # Split by closing ul to inject nav
    parts_nav = html.split('        </ul>')
    nav_injection = ""
    for ch in chapters2:
        nav_injection += f'            <li><a href="#ch{ch["id"]}">Ch {ch["id"]}: {ch["title"]}</a></li>\n'
    html = parts_nav[0] + nav_injection + '        </ul>' + parts_nav[1]
    
    # Split by closing main to inject content
    parts_content = html.split('    </main>')
    content_injection = ""
    for ch in chapters2:
        content_injection += CHAPTER_TEMPLATE.format(**ch)
    html = parts_content[0] + content_injection + '    </main>' + parts_content[1]
    
    with open('index.html', 'w') as f:
        f.write(html)
    print("Site updated with chapters 6-10 successfully!")

if __name__ == "__main__":
    append_html()
