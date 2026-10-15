import os

def check_pdf():
    print("Does site-complete/pdf exist?", os.path.exists("site-complete/pdf"))
    print("Does pdf exist at root?", os.path.exists("pdf"))
    # list directories in site-complete
    print("site-complete top-level:", os.listdir("site-complete"))
    # list directories in root
    print("root top-level:", [d for d in os.listdir(".") if os.path.isdir(d)])

if __name__ == "__main__":
    check_pdf()
