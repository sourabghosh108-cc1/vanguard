import os
import zipfile

base_dir = r"c:\Users\ACER\Desktop\design\TeamVanguard_"
zip_path = r"c:\Users\ACER\Desktop\design\TeamVanguard_.zip"

required_files = [
    os.path.join("01_Style_Guide", "Brand_Style_Guide.pdf"),
    os.path.join("01_Style_Guide", "Logo_Primary.svg"),
    os.path.join("01_Style_Guide", "Logo_Secondary.svg"),
    os.path.join("01_Style_Guide", "Symbol_Mark.svg"),
    os.path.join("01_Style_Guide", "Compact_Lockup.svg"),
    os.path.join("02_Packaging_and_Merch", "Packaging_Design.png"),
    os.path.join("02_Packaging_and_Merch", "Merch_Mockups.png"),
    os.path.join("03_Digital_UI", "UI_LandingPage.png"),
    os.path.join("03_Digital_UI", "UI_AcousticCraft.png"),
    os.path.join("03_Digital_UI", "index.html"),
    os.path.join("03_Digital_UI", "acoustic.html"),
    os.path.join("03_Digital_UI", "styles.css"),
    os.path.join("03_Digital_UI", "app.js"),
    os.path.join("04_Product_Collateral", "Headphone_Earcup_Pattern.svg"),
    os.path.join("04_Product_Collateral", "Headphone_Earcup_Pattern.png"),
    os.path.join("04_Product_Collateral", "Retail_Display.png"),
    os.path.join("05_Campaign_Poster", "Poster_A2.png"),
    os.path.join("05_Campaign_Poster", "Poster_Print.pdf"),
    os.path.join("06_Presentation", "Concept_Presentation.pdf"),
]

missing = []
for rel in required_files:
    full = os.path.join(base_dir, rel)
    if not os.path.exists(full):
        missing.append(rel)
    else:
        print(f"[OK] Found {rel} ({os.path.getsize(full)} bytes)")

if missing:
    print(f"ERROR: Missing files: {missing}")
else:
    print("All required deliverable files are present and verified!")

# Zip compression
print(f"Creating zip archive: {zip_path}...")
with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
    for root, dirs, files in os.walk(base_dir):
        for file in files:
            full_path = os.path.join(root, file)
            arcname = os.path.relpath(full_path, os.path.dirname(base_dir))
            zipf.write(full_path, arcname)

print(f"ZIP Archive successfully created! Size: {os.path.getsize(zip_path)} bytes.")
