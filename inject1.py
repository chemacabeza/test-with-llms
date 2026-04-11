import os
import shutil

brain_dir = "/home/chemacabeza/.gemini/antigravity/brain/cc074362-e9b4-4c46-a207-59606b86028f"
dest_image_dir = "/home/chemacabeza/Repositories/test-with-llms.git/images"

# Ensure dir exists
os.makedirs(dest_image_dir, exist_ok=True)

images_to_copy = [
    "ch1_feynman_magician_1775888782688.png",
    "ch1_deepdive_softmax_1775888801505.png",
    "ch1_realworld_phone_1775888818124.png",
    "ch2_feynman_citymap_1775888834276.png",
    "ch2_deepdive_vectors_1775888849493.png",
    "ch2_realworld_shoes_1775888869403.png",
    "ch3_feynman_detective_1775888887189.png",
    "ch3_deepdive_qkv_1775888905774.png",
    "ch3_realworld_translate_1775888923077.png",
    "ch4_feynman_factory_1775888971749.png",
    "ch4_deepdive_stack_1775888990531.png",
    "ch4_realworld_server_1775889008742.png",
    "ch5_feynman_library_1775889028357.png",
    "ch5_deepdive_gradient_1775889044889.png",
    "ch5_realworld_h100_1775889062664.png"
]

injections = {
    1: ["ch1_feynman_magician_1775888782688.png", "ch1_deepdive_softmax_1775888801505.png", "ch1_realworld_phone_1775888818124.png"],
    2: ["ch2_feynman_citymap_1775888834276.png", "ch2_deepdive_vectors_1775888849493.png", "ch2_realworld_shoes_1775888869403.png"],
    3: ["ch3_feynman_detective_1775888887189.png", "ch3_deepdive_qkv_1775888905774.png", "ch3_realworld_translate_1775888923077.png"],
    4: ["ch4_feynman_factory_1775888971749.png", "ch4_deepdive_stack_1775888990531.png", "ch4_realworld_server_1775889008742.png"],
    5: ["ch5_feynman_library_1775889028357.png", "ch5_deepdive_gradient_1775889044889.png", "ch5_realworld_h100_1775889062664.png"]
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

