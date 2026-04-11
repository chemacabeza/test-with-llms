import os
import shutil

brain_dir = "/home/chemacabeza/.gemini/antigravity/brain/cc074362-e9b4-4c46-a207-59606b86028f"
dest_image_dir = "/home/chemacabeza/Repositories/test-with-llms.git/images"

# Ensure dir exists
os.makedirs(dest_image_dir, exist_ok=True)

images_to_copy = [
    "ch6_feynman_doctor_1775889196630.png",
    "ch6_deepdive_lora_1775889214083.png",
    "ch6_realworld_lawyer_1775889233582.png",
    "ch7_feynman_chef_1775889251269.png",
    "ch7_deepdive_rlhf_1775889266177.png",
    "ch7_realworld_chat_1775889286707.png",
    "ch8_feynman_alien_1775889304275.png",
    "ch8_deepdive_prompt_1775889324058.png",
    "ch8_realworld_system_1775889343379.png",
    "ch9_feynman_math_1775889365355.png",
    "ch9_deepdive_cot_1775889386520.png",
    "ch9_realworld_o1_1775889400628.png",
    "ch10_feynman_exam_1775889414729.png",
    "ch10_deepdive_rag_1775889437450.png",
    "ch10_realworld_enterprise_1775889454983.png"
]

injections = {
    6: ["ch6_feynman_doctor_1775889196630.png", "ch6_deepdive_lora_1775889214083.png", "ch6_realworld_lawyer_1775889233582.png"],
    7: ["ch7_feynman_chef_1775889251269.png", "ch7_deepdive_rlhf_1775889266177.png", "ch7_realworld_chat_1775889286707.png"],
    8: ["ch8_feynman_alien_1775889304275.png", "ch8_deepdive_prompt_1775889324058.png", "ch8_realworld_system_1775889343379.png"],
    9: ["ch9_feynman_math_1775889365355.png", "ch9_deepdive_cot_1775889386520.png", "ch9_realworld_o1_1775889400628.png"],
    10: ["ch10_feynman_exam_1775889414729.png", "ch10_deepdive_rag_1775889437450.png", "ch10_realworld_enterprise_1775889454983.png"]
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

