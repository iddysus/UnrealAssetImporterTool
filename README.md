# UnrealAssetImporterTool
A tool that automates the process of importing and organizing assets into Unreal Engine. Batch import of models, textures, and automatic organization into folders based on asset type.

# Unreal Engine Asset Importer Tool

This tool automates the batch import and organization of assets (e.g., textures, meshes) into Unreal Engine projects using Python scripting.

## Features:
- Batch import assets from a folder.
- Organize assets into appropriate folders (e.g., meshes, textures).
- Automatically generate Level of Detail (LOD) models for imported meshes.

## Setup:
1. Enable the **Python Editor Script Plugin** in Unreal Engine.
2. Place this script in the `Scripts` folder of your Unreal Engine project.

## Usage:
1. Open the **Output Log** in Unreal Engine.
2. Run the script by typing:
   ```python
   import unreal_asset_importer_tool
   unreal_asset_importer_tool.import_assets()
   unreal_asset_importer_tool.organize_assets()
   unreal_asset_importer_tool.generate_lods()
