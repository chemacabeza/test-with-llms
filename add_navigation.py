import os
import re

chapters_dir = "/home/chemacabeza/Repositories/test-with-llms.git/chapters"
files = sorted([f for f in os.listdir(chapters_dir) if f.startswith("chapter_") and f.endswith(".md")], key=lambda x: int(re.search(r'\d+', x).group()))

def get_nav_bar(current_idx):
    prev_link = f"[⬅️ Previous](chapter_{current_idx-1}.md)" if current_idx > 1 else None
    home_link = "[🏠 Home](../README.md)"
    next_link = f"[Next ➡️](chapter_{current_idx+1}.md)" if current_idx < 20 else None
    
    links = [home_link]
    if prev_link: links.insert(0, prev_link)
    if next_link: links.append(next_link)
    
    return "\n\n---\n" + " | ".join(links) + "\n"

for i, filename in enumerate(files, 1):
    path = os.path.join(chapters_dir, filename)
    with open(path, 'r') as f:
        content = f.read()
    
    # Remove existing nav if any (to be idempotent)
    content = re.sub(r'\n\n---\n\[⬅️ Previous\].*?\| \[🏠 Home\].*?(\[Next ➡️\].*?)?\n', '', content)
    content = re.sub(r'\n\n---\n\[🏠 Home\].*?\| \[Next ➡️\].*?\n', '', content)
    
    nav = get_nav_bar(i)
    
    # Add to top (after header) and bottom
    lines = content.split('\n')
    # Find the line after the header (usually line 2 or 3)
    header_idx = 1
    for idx, line in enumerate(lines):
        if line.startswith("# "):
            header_idx = idx + 1
            break
            
    # Inject Top
    lines.insert(header_idx, nav)
    # Inject Bottom
    new_content = '\n'.join(lines) + nav
    
    with open(path, 'w') as f:
        f.write(new_content)

print(f"Successfully injected navigation into {len(files)} chapters.")
