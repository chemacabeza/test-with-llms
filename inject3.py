import os
import shutil

brain_dir = "/home/chemacabeza/.gemini/antigravity/brain/cc074362-e9b4-4c46-a207-59606b86028f"
dest_image_dir = "/home/chemacabeza/Repositories/test-with-llms.git/images"

# Ensure dir exists
os.makedirs(dest_image_dir, exist_ok=True)

images_to_copy = [
    "ch11_feynman_car_1775889649114.png",
    "ch11_deepdive_lcel_1775889665920.png",
    "ch11_realworld_ticket_1775889683122.png",
    "ch12_feynman_robot_1775889699687.png",
    "ch12_deepdive_agent_1775889715733.png",
    "ch12_realworld_devin_1775889732160.png",
    "ch13_feynman_goldfish_1775889750621.png",
    "ch13_deepdive_memory_1775889768306.png",
    "ch13_realworld_chat_1775889783599.png",
    "ch14_feynman_scissors_1775889801354.png",
    "ch14_deepdive_chunk_1775889817305.png",
    "ch14_realworld_legal_1775889836525.png",
    "ch15_feynman_twin_1775889851969.png",
    "ch15_deepdive_finetune_1775889869041.png",
    "ch15_realworld_influ_1775889888299.png"
]

injections = {
    11: ["ch11_feynman_car_1775889649114.png", "ch11_deepdive_lcel_1775889665920.png", "ch11_realworld_ticket_1775889683122.png"],
    12: ["ch12_feynman_robot_1775889699687.png", "ch12_deepdive_agent_1775889715733.png", "ch12_realworld_devin_1775889732160.png"],
    13: ["ch13_feynman_goldfish_1775889750621.png", "ch13_deepdive_memory_1775889768306.png", "ch13_realworld_chat_1775889783599.png"],
    14: ["ch14_feynman_scissors_1775889801354.png", "ch14_deepdive_chunk_1775889817305.png", "ch14_realworld_legal_1775889836525.png"],
    15: ["ch15_feynman_twin_1775889851969.png", "ch15_deepdive_finetune_1775889869041.png", "ch15_realworld_influ_1775889888299.png"]
}

# 1. Copy images
for img in images_to_copy:
    src = os.path.join(brain_dir, img)
    dst = os.path.join(dest_image_dir, img)
    if os.path.exists(src):
        shutil.copy(src, dst)
        print(f"Copied {img}")
    else:
        print(f"WARNING: {src} not found")

# 2. Inject into markdown files
chapters_dir = "/home/chemacabeza/Repositories/test-with-llms.git/chapters"

for ch_num, images in injections.items():
    ch_path = os.path.join(chapters_dir, f"chapter_{ch_num}.md")
    
    if os.path.exists(ch_path):
        with open(ch_path, 'r') as f:
            content = f.read()
            
        # Perform replacements
        replacements = [
            ("### 💡 The Simple Explanation\n", f"### 💡 The Simple Explanation\n\n<p align=\"center\">\n  <img src=\"../images/{images[0]}\" width=\"80%\">\n</p>\n"),
            ("### 🔍 Going Deeper: The Technical Reality\n", f"### 🔍 Going Deeper: The Technical Reality\n\n<p align=\"center\">\n  <img src=\"../images/{images[1]}\" width=\"80%\">\n</p>\n"),
            ("### 🌐 Real-World Connection\n", f"### 🌐 Real-World Connection\n\n<p align=\"center\">\n  <img src=\"../images/{images[2]}\" width=\"80%\">\n</p>\n")
        ]
        
        for old, new in replacements:
            if old in content:
                content = content.replace(old, new)
        
        with open(ch_path, 'w') as f:
            f.write(content)
        print(f"Injected images into chapter_{ch_num}.md")
    else:
        print(f"WARNING: {ch_path} not found")
