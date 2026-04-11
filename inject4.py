import os
import shutil

brain_dir = "/home/chemacabeza/.gemini/antigravity/brain/cc074362-e9b4-4c46-a207-59606b86028f"
dest_image_dir = "/home/chemacabeza/Repositories/test-with-llms.git/images"

# Ensure dir exists
os.makedirs(dest_image_dir, exist_ok=True)

images_to_copy = [
    "ch16_feynman_factory_1775890057352.png",
    "ch16_deepdive_orchestrator_1775890074169.png",
    "ch16_realworld_ci_1775890091393.png",
    "ch17_feynman_racecar_1775890107610.png",
    "ch17_deepdive_quantization_1775890128062.png",
    "ch17_realworld_mobile_1775890145938.png",
    "ch18_feynman_judge_1775890163216.png",
    "ch18_deepdive_eval_1775890180585.png",
    "ch18_realworld_dashboard_1775890198911.png",
    "ch19_feynman_shield_1775890221281.png",
    "ch19_deepdive_nemo_1775890236385.png",
    "ch19_realworld_bank_1775890253282.png",
    "ch20_feynman_horizon_1775890268854.png",
    "ch20_deepdive_scale_1775890289175.png",
    "ch20_realworld_agi_1775890311374.png"
]

injections = {
    16: ["ch16_feynman_factory_1775890057352.png", "ch16_deepdive_orchestrator_1775890074169.png", "ch16_realworld_ci_1775890091393.png"],
    17: ["ch17_feynman_racecar_1775890107610.png", "ch17_deepdive_quantization_1775890128062.png", "ch17_realworld_mobile_1775890145938.png"],
    18: ["ch18_feynman_judge_1775890163216.png", "ch18_deepdive_eval_1775890180585.png", "ch18_realworld_dashboard_1775890198911.png"],
    19: ["ch19_feynman_shield_1775890221281.png", "ch19_deepdive_nemo_1775890236385.png", "ch19_realworld_bank_1775890253282.png"],
    20: ["ch20_feynman_horizon_1775890268854.png", "ch20_deepdive_scale_1775890289175.png", "ch20_realworld_agi_1775890311374.png"]
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
