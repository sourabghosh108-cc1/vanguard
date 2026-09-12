import os
import shutil
from PIL import Image

brain_dir = r"C:\Users\ACER\.gemini\antigravity-ide\brain\202e0b5b-f952-45a2-8f2e-fbfcb8ac2205"
dest_base = r"c:\Users\ACER\Desktop\design\TeamVanguard_"

# Find generated images by pattern or timestamp
files = os.listdir(brain_dir)

def find_latest_img(prefix):
    matching = [f for f in files if f.startswith(prefix) and (f.endswith('.jpg') or f.endswith('.png'))]
    if not matching:
        raise FileNotFoundError(f"No file matching {prefix}")
    matching.sort(key=lambda x: os.path.getmtime(os.path.join(brain_dir, x)), reverse=True)
    return os.path.join(brain_dir, matching[0])

pkg_img = find_latest_img("vanguard_packaging_mockup")
merch_img = find_latest_img("vanguard_merch_mockup")
earcup_img = find_latest_img("vanguard_earcup_macro")
retail_img = find_latest_img("vanguard_retail_display")
poster_img = find_latest_img("vanguard_event_poster")

# Copy & convert to PNG with high quality
def convert_and_save(src_path, dst_path):
    img = Image.open(src_path)
    img.save(dst_path, "PNG", quality=100)
    print(f"Saved: {dst_path}")

convert_and_save(pkg_img, os.path.join(dest_base, "02_Packaging_and_Merch", "Packaging_Design.png"))
convert_and_save(merch_img, os.path.join(dest_base, "02_Packaging_and_Merch", "Merch_Mockups.png"))
convert_and_save(earcup_img, os.path.join(dest_base, "04_Product_Collateral", "Headphone_Earcup_Pattern.png"))
convert_and_save(retail_img, os.path.join(dest_base, "04_Product_Collateral", "Retail_Display.png"))
convert_and_save(poster_img, os.path.join(dest_base, "05_Campaign_Poster", "Poster_A2.png"))

# Also save editable raw source files in respective subdirectories
shutil.copy(pkg_img, os.path.join(dest_base, "02_Packaging_and_Merch", "Editable_Sources", "Packaging_Design_Raw.jpg"))
shutil.copy(merch_img, os.path.join(dest_base, "02_Packaging_and_Merch", "Editable_Sources", "Merch_Mockups_Raw.jpg"))
shutil.copy(earcup_img, os.path.join(dest_base, "04_Product_Collateral", "Editable_Sources", "Earcup_Macro_Raw.jpg"))
shutil.copy(retail_img, os.path.join(dest_base, "04_Product_Collateral", "Editable_Sources", "Retail_Display_Raw.jpg"))
shutil.copy(poster_img, os.path.join(dest_base, "05_Campaign_Poster", "Editable_Sources", "Poster_A2_Raw.jpg"))

print("All visual assets copied and converted to PNG successfully!")
