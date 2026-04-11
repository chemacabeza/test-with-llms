import os

# HTML Layout Template
HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>LLM Mastery Course</title>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <nav class="sidebar">
        <h2>LLM Mastery</h2>
        <ul>
{nav_links}
        </ul>
    </nav>
    <main class="main-content">
{content}
    </main>
    <script src="script.js"></script>
</body>
</html>
"""

CHAPTER_TEMPLATE = """
        <section id="ch{id}" class="chapter">
            <div class="chapter-header">
                <span class="chapter-phase">{phase}</span>
                <h1>Chapter {id}: {title}</h1>
            </div>
            <img src="images/ch{id}.png" alt="Chapter {id} Infographic" class="chapter-img">
            
            <div class="section">
                <h3><span class="icon">💡</span> The Simple Explanation</h3>
                {simple_explanation}
            </div>
            
            <div class="section">
                <h3><span class="icon">🔍</span> Going Deeper</h3>
                {going_deeper}
            </div>
            
            <div class="concept-box">
                <p><strong>The "Aha!" Moment:</strong> {aha_moment}</p>
            </div>
            
            <div class="section">
                <h3><span class="icon">🌐</span> Real-World Connection</h3>
                {real_world}
            </div>
            
            <div class="reference">
                <span class="ref-icon">📚</span>
                <span><strong>References:</strong> {references}</span>
            </div>
        </section>
"""

chapters = [
    {
        "id": 1,
        "phase": "Phase 1: Foundations",
        "title": "The Magic of Prediction",
        "simple_explanation": "<p>Imagine you have a magical friend who has read almost every book in the library. If you start a sentence like 'The quick brown fox jumps over the lazy...', your friend instantly knows the next word is 'dog'. They aren't thinking or reasoning; they are just guessing what word comes next based on all the books they've seen. An LLM (Large Language Model) is exactly like this magical friend. It's a next-word prediction engine.</p>",
        "going_deeper": "<p>Under the hood, this 'guessing' is powered by a massive neural network. When you give it text, it breaks it down into small pieces called tokens. It then uses complex math to calculate the probability of what the next token should be. It predicts one token, adds it to your sentence, and then predicts the next one, looping over and over again until it forms a complete thought.</p>",
        "aha_moment": "An LLM doesn't actually 'know' facts; it just knows which words mathematically belong next to each other.",
        "real_world": "<p>When you type on your smartphone and it suggests the next word above the keyboard, that is a tiny version of the exact same technology. LLMs just do it on a massive scale with trillions of parameters.</p>",
        "references": "<em>Hands-On Large Language Models</em> (Alammar & Grootendorst); <em>Large Language Models</em> (Raaijmakers); <em>LLMs in Production</em> (Brousseau & Sharp)"
    },
    {
        "id": 2,
        "phase": "Phase 1: Foundations",
        "title": "Speaking in Numbers",
        "simple_explanation": "<p>Computers don’t understand words like 'apple' or 'jump'. They only understand math and numbers. If you want to teach a computer language, you first need to turn a dictionary into a math problem. Imagine assigning every word in the dictionary a specific GPS coordinate on a giant 3D map. Words that mean similar things (like 'dog' and 'wolf') are placed close together. This map is what we call 'Embeddings'.</p>",
        "going_deeper": "<p>Before mapping, the text is split into chunks using <strong>Tokenization</strong> (e.g., Byte Pair Encoding). Each token gets an ID, and that ID is mapped to a vector—a list of numbers representing its coordinates in a high-dimensional space (often 4,000+ dimensions). The model also adds 'positional encodings' to these vectors so it knows the order of words in a sentence.</p>",
        "aha_moment": "Embeddings turn language into geometry. The meaning of a word is just its distance and direction from other words in mathematical space.",
        "real_world": "<p>When you search for 'comfortable sneakers' on an e-commerce site, and it shows you 'running shoes' (even though the words are completely different), it's because their embeddings are very close in the math space.</p>",
        "references": "<em>Build a Large Language Model (From Scratch)</em> (Raschka); <em>Hands-On Large Language Models</em> (Alammar & Grootendorst)"
    },
    {
        "id": 3,
        "phase": "Phase 1: Foundations",
        "title": "The Attention Revolution",
        "simple_explanation": "<p>Imagine you are reading a mystery novel. When you read the word 'he' on page 50, you instantly know it refers to the detective from page 2. Your brain naturally pays 'attention' to the right context. For a long time, computers read text blindly, word-by-word. Then came 'Self-Attention'. It's a special calculation that allows every word in a sentence to look at every other word and ask, 'How strongly am I related to you?'</p>",
        "going_deeper": "<p>At the heart of the Transformer architecture is <strong>Multi-Head Self-Attention</strong>. It allows the model to process all words simultaneously rather than sequentially. For each word, it creates a Query, Key, and Value vector. By multiplying Queries and Keys, the model forms an 'attention matrix' that dictates how much focus (weight) one word should place on another.</p>",
        "aha_moment": "Self-attention gives the model a dynamic memory, letting it figure out pronouns, context, and grammar rules purely by calculating relationships between words.",
        "real_world": "<p>When translating 'The bank of the river' vs 'The bank on the corner', older translators struggled. Self-attention looks at surrounding words ('river' or 'corner') to perfectly understand which 'bank' is meant.</p>",
        "references": "<em>Build a Large Language Model (From Scratch)</em> (Raschka); <em>Hands-On Large Language Models</em> (Alammar & Grootendorst); <em>Large Language Models</em> (Raaijmakers)"
    },
    {
        "id": 4,
        "phase": "Phase 1: Foundations",
        "title": "Building a Brain",
        "simple_explanation": "<p>Think of building an LLM like assembling a multi-story factory. On the ground floor, raw text comes in and gets turned into numbers. Then it moves up through an elevator. On every single floor (called a Transformer Block), the data goes through two main machines: the 'Attention Machine' (which links related words) and the 'Thinking Machine' (which processes the data further). After passing through maybe 96 identical floors, the final output at the roof is a predicted new word.</p>",
        "going_deeper": "<p>A Generative Pre-trained Transformer (GPT) is essentially a stack of decoder blocks. Inside each block, tokens pass through <strong>Self-Attention</strong>, are added to their previous state via a <strong>Residual Connection</strong>, normalized with <strong>Layer Normalization</strong>, and passed through a <strong>Feed-Forward Network (FFN)</strong> using non-linear activations like GELU. This repeated processing is what allows complex representations to form.</p>",
        "aha_moment": "The architecture is actually quite repetitive. The model's 'intelligence' comes from running data through the same structural block over and over again, allowing deep patterns to emerge.",
        "real_world": "<p>The architecture of almost every major model today (ChatGPT, Claude, Llama) uses this exact same stacked layer approach designed by Google researchers in 2017.</p>",
        "references": "<em>Build a Large Language Model (From Scratch)</em> (Raschka); <em>LLMs in Production</em> (Brousseau & Sharp)"
    },
    {
        "id": 5,
        "phase": "Phase 1: Foundations",
        "title": "The Training Ground",
        "simple_explanation": "<p>If you build a brain, it's completely empty at first. To teach it, you need to lock it in a room with the entire internet. You hand it a sentence with the last word covered up. 'The sky is ___'. The brain guesses 'green'. You say 'No, it's blue.' The brain slightly adjusts its internal dials so next time it's more likely to guess 'blue'. You repeat this trillions of times across Wikipedia, books, and Reddit until the brain learns grammar, facts, and reasoning.</p>",
        "going_deeper": "<p>This phase is called <strong>Pretraining</strong>. It uses unsupervised learning on a massive corpus of text. The model tries to minimize its 'Loss' (the difference between its prediction and the actual next token) using an algorithm called Gradient Descent. The model updates billions of parameters (weights) across thousands of GPUs over weeks or months. By learning to predict the next word, it unintentionally learns world knowledge.</p>",
        "aha_moment": "LLMs aren't explicitly programmed with rules about grammar or history. They magically reverse-engineer these concepts just to get better at predicting the next word.",
        "real_world": "<p>Training a frontier model like Llama 3 or GPT-4 takes essentially an entire supercomputer running at full capacity for months, costing tens of millions of dollars in electricity alone.</p>",
        "references": "<em>Build a Large Language Model (From Scratch)</em> (Raschka); <em>LLMs in Production</em> (Brousseau & Sharp); <em>Large Language Models</em> (Raaijmakers)"
    }
]

def generate_html():
    nav_links = ""
    content = ""
    
    for ch in chapters:
        nav_links += f'            <li><a href="#ch{ch["id"]}">Ch {ch["id"]}: {ch["title"]}</a></li>\n'
        content += CHAPTER_TEMPLATE.format(**ch)
        
    final_html = HTML_TEMPLATE.format(nav_links=nav_links, content=content)
    with open('index.html', 'w') as f:
        f.write(final_html)
    print("Site generated successfully!")

if __name__ == "__main__":
    generate_html()
