import os
from build_site import HTML_TEMPLATE, CHAPTER_TEMPLATE

chapters3 = [
    {
        "id": 11,
        "phase": "Phase 3: Building Real Applications",
        "title": "Your First LLM App",
        "simple_explanation": "<p>Using an LLM by itself is like having a powerful engine sitting on your driveway. To go anywhere, you need a steering wheel, pedals, and a chassis. LangChain is that chassis. It's a framework that lets you snap together different parts—like a Prompt Template (steering wheel), the LLM (engine), and an Output Parser (dashboard)—into a single 'Chain' that runs automatically.</p>",
        "going_deeper": "<p>A basic <strong>LangChain</strong> app involves defining a PromptTemplate (with variables like `{topic}`), binding it to a model (like OpenAI or Llama), and chaining them using the `|` syntax (LCEL - LangChain Expression Language). You can build <strong>Sequential Chains</strong> where the output of Chain 1 (e.g., write a play) becomes the input for Chain 2 (e.g., write a review of that play).</p>",
        "aha_moment": "LangChain turns LLMs from passive chatbot interfaces into automated, programmable pipelines.",
        "real_world": "<p>When a marketing company has an app that takes a URL, reads the article, and outputs 5 distinct Twitter posts, it's just a 3-step LangChain running in the background.</p>",
        "references": "<em>Learning LangChain</em> (Oshin & Campos); <em>LangChain Crash Course</em> (Lim)"
    },
    {
        "id": 12,
        "phase": "Phase 3: Building Real Applications",
        "title": "Smart Assistants",
        "simple_explanation": "<p>An LLM is just a brain in a jar. It can think, but it has no hands. If you ask it to 'book a flight', it can't click the website. A <strong>Tool</strong> is like giving the brain a robotic hand. An <strong>Agent</strong> is giving the brain the intelligence to look at its tools, decide which one to hold, and actually use it to affect the real world.</p>",
        "going_deeper": "<p>In agentic frameworks like LangGraph, the LLM is given a description of available tools (e.g., `execute_sql()`, `search_web()`). Using paradigms like ReAct (Reason + Act), the model outputs a 'Thought', then an 'Action' (calling the tool with specific JSON arguments). The system runs the tool, returns the 'Observation' to the LLM, and the LLM decides if it needs to act again.</p>",
        "aha_moment": "Agents transform LLMs from <em>readers and writers</em> of text into <em>doers</em> of actions.",
        "real_world": "<p>Devin, the famous AI Software Engineer, is an agent. It doesn't just write code; it runs a terminal tool, tries tests, sees the error, and iterates.</p>",
        "references": "<em>Learning LangChain</em> (Oshin & Campos); <em>Creating Custom GPT with OpenAI GPT Builder</em> (Russell etc.)"
    },
    {
        "id": 13,
        "phase": "Phase 3: Building Real Applications",
        "title": "Conversations That Remember",
        "simple_explanation": "<p>LLMs have the memory of a goldfish. Every time you send a message, it completely forgets the previous one. To have a conversation, you have to attach the entire history of the chat to every single new message you send. It's like having to remind your friend of your entire life story every time you say 'hello'.</p>",
        "going_deeper": "<p>Memory in LLM apps is handled outside the model. Systems use a <strong>ConversationBufferMemory</strong> to simply append all past messages. When this gets too long and exceeds the 'context window' (the max tokens the model can read at once), we use <strong>ConversationSummaryMemory</strong> to compress old messages into a short summary, keeping the token count low while preserving context.</p>",
        "aha_moment": "Memory isn't stored inside the LLM computing core; it's just a growing text file of history injected into the prompt right before you hit 'send'.",
        "real_world": "<p>ChatGPT's sidebar of past conversations is exactly this. When you click an old chat, OpenAI just loads that history file and drops it into the invisible prompt window.</p>",
        "references": "<em>LangChain Crash Course</em> (Lim); <em>Learning LangChain</em> (Oshin & Campos)"
    },
    {
        "id": 14,
        "phase": "Phase 3: Building Real Applications",
        "title": "Chat With Your Documents",
        "simple_explanation": "<p>How do you make an AI read a 500-page PDF and answer questions about it? You can't paste 500 pages into the chat box; it's too big. Instead, you put the PDF through a shredder, keeping paragraph-sized chunks. You file these chunks in a special mathematical filing cabinet. When you ask a question, a librarian finds the 3 chunks that match your question best, and hands only those to the AI.</p>",
        "going_deeper": "<p>This is the practical implementation of RAG. You use Document Loaders (for PDFs, CSVs, or YouTube transcripts), use TextSplitters to chunk the data with slight overlap, embed them, and load them into a VectorStore (like Pinecone or Chroma). The chain retrieves the top-K similar chunks and formats them into a prompt template: `Context: {retrieved_chunks}. Question: {question}`.</p>",
        "aha_moment": "The AI isn't reading the whole document when you ask a question. It's only reading the top 3 paragraphs that a keyword-search algorithm found first.",
        "real_world": "<p>Applications like ChatPDF or specialized legal AI assistants rely entirely on intelligent chunking and vector retrieval to handle documents that exceed context windows.</p>",
        "references": "<em>LangChain Crash Course</em> (Lim); <em>Building LLMs for Production</em> (Bouchard)"
    },
    {
        "id": 15,
        "phase": "Phase 3: Building Real Applications",
        "title": "The LLM Twin",
        "simple_explanation": "<p>Imagine having a perfectly identical robot copy of yourself that writes emails exactly how you write them, uses your favorite phrases, and knows everything you've ever posted online. This is an 'LLM Twin'. Instead of an AI that sounds like a generic robot perfectly polite assistant, it sounds uniquely and identically like <em>you</em>.</p>",
        "going_deeper": "<p>Creating a true LLM Twin requires an advanced pipeline combining all previous techniques. You scrape an individual's digital exhaust (Substack, Twitter, LinkedIn). You use <strong>Supervised Fine-Tuning</strong> to capture their specific grammatical quirks and tone. Finally, you layer a personal <strong>RAG</strong> database on top, ensuring the Twin accesses the individual's exact past statements and facts before generating new content.</p>",
        "aha_moment": "Identity in the AI age can be digitized. A person's 'voice' is just a statistical distribution of tokens that can be mimicked perfectly with enough data.",
        "real_world": "<p>Influencers and authors are beginning to fine-tune personal twins to draft their newsletters, scaling their personal brand without losing their authentic voice.</p>",
        "references": "<em>LLM Engineer's Handbook</em> (Iusztin & Labonne)"
    }
]

def append_html_3():
    with open('index.html', 'r') as f:
        html = f.read()
    
    parts_nav = html.split('        </ul>')
    nav_injection = ""
    for ch in chapters3:
        nav_injection += f'            <li><a href="#ch{ch["id"]}">Ch {ch["id"]}: {ch["title"]}</a></li>\n'
    html = parts_nav[0] + nav_injection + '        </ul>' + parts_nav[1]
    
    parts_content = html.split('    </main>')
    content_injection = ""
    for ch in chapters3:
        content_injection += CHAPTER_TEMPLATE.format(**ch)
    html = parts_content[0] + content_injection + '    </main>' + parts_content[1]
    
    with open('index.html', 'w') as f:
        f.write(html)
    print("Site updated with chapters 11-15 successfully!")

if __name__ == "__main__":
    append_html_3()
