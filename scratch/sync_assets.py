import os
import shutil

src_root = r"c:\Users\user\Desktop\全日本弓道連盟\kyudo\www.kyudo.jp"
dst_root = r"c:\Users\user\Desktop\ホームページ素材\site-complete"

folders_to_sync = ['pdf', 'img', 'documents']

for folder in folders_to_sync:
    s_folder = os.path.join(src_root, folder)
    d_folder = os.path.join(dst_root, folder)
    if not os.path.exists(s_folder):
        print(f"Source folder {s_folder} not found!")
        continue
    
    count = 0
    for root, dirs, files in os.walk(s_folder):
        rel = os.path.relpath(root, s_folder)
        target_dir = os.path.join(d_folder, rel) if rel != '.' else d_folder
        os.makedirs(target_dir, exist_ok=True)
        for f in files:
            src_file = os.path.join(root, f)
            dst_file = os.path.join(target_dir, f)
            if not os.path.exists(dst_file):
                shutil.copy2(src_file, dst_file)
                count += 1
    print(f"Copied {count} files to {d_folder}")

print("Sync completed!")
