import os
import re

def split_course():
    os.makedirs('chapters', exist_ok=True)
    
    with open('llm_course.md', 'r') as f:
        content = f.read()

    # Split by Chapter headings
    # The headings are format: "### Chapter X: Title"
    parts = re.split(r'(### Chapter \d+:.*?\n)', content)
    
    current_chapter = 0
    
    for i in range(1, len(parts), 2):
        chapter_heading = parts[i].strip()
        chapter_body = parts[i+1].split('---')[0].strip() # stop at horizontal rule if exists
        
        # Extract chapter number
        match = re.search(r'Chapter (\d+):', chapter_heading)
        if match:
            chapter_num = int(match.group(1))
            
            # Format the output with the image
            md_content = f"# {chapter_heading.replace('### ', '')}\n\n"
            md_content += f'<p align="center">\n  <img src="../images/ch{chapter_num}.png" alt="Chapter {chapter_num} Infographic" width="80%">\n</p>\n\n'
            md_content += f"{chapter_body}\n"
            
            # Write to file
            with open(f'chapters/chapter_{chapter_num}.md', 'w') as out_f:
                out_f.write(md_content)
            
            print(f"Created chapters/chapter_{chapter_num}.md")

if __name__ == "__main__":
    split_course()
