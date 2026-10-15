import os
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

site_root = r"site-complete"

def check_local_dirs():
    # check category/taikai
    cat_taikai = os.path.join(site_root, "category", "taikai")
    print(f"{cat_taikai} exists: {os.path.exists(cat_taikai)}")
    if os.path.exists(cat_taikai):
        for r, ds, fs in os.walk(cat_taikai):
            print("  Cat taikai dir:", r, ds, fs)
            
    # check schedule/taikai
    sched_taikai = os.path.join(site_root, "schedule", "taikai")
    print(f"\n{sched_taikai} exists: {os.path.exists(sched_taikai)}")
    if os.path.exists(sched_taikai):
        for r, ds, fs in os.walk(sched_taikai):
            print("  Sched taikai:", r, ds, fs)

    # check other category folders
    cat_dir = os.path.join(site_root, "category")
    if os.path.exists(cat_dir):
        print(f"\ncategory subdirs: {os.listdir(cat_dir)}")

if __name__ == "__main__":
    check_local_dirs()
