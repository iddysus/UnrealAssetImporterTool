
import unreal

# Define the folder where your assets are located
asset_folder_path = "C:/Path/To/Your/Assets"

# Define the destination path in the Unreal Engine project
destination_path = "/Game/ImportedAssets"

# Get a reference to the asset tools helper
asset_tools = unreal.AssetToolsHelpers.get_asset_tools()

# Import all assets in the specified folder
def import_assets():
    # Specify the files to import (all .fbx files as an example)
    import_options = unreal.FbxImportUI()
    import_options.import_as_skeletal = False  # Set if importing static meshes or skeletal meshes
    
    task = unreal.AssetImportTask()
    task.filename = asset_folder_path  # Path to the asset folder
    task.destination_path = destination_path  # Where in the content browser to import the assets
    task.automated = True
    task.save = True  # Automatically save after import
    task.options = import_options
    
    # Execute the import
    asset_tools.import_asset_tasks([task])

# Organizing Imported Assets into Folders
def organize_assets():
    asset_registry = unreal.AssetRegistryHelpers.get_asset_registry()
    
    # Get all assets in the destination folder
    assets = asset_registry.get_assets_by_path(destination_path, recursive=True)
    
    for asset_data in assets:
        asset = asset_data.get_asset()
        
        # Organize based on asset type
        if isinstance(asset, unreal.StaticMesh):
            unreal.EditorAssetLibrary.rename_asset(asset_data.object_path, f"{destination_path}/Meshes/{asset_data.asset_name}")
        elif isinstance(asset, unreal.Texture):
            unreal.EditorAssetLibrary.rename_asset(asset_data.object_path, f"{destination_path}/Textures/{asset_data.asset_name}")
        # Add more cases for different asset types

# Generating LODs for Imported Meshes
def generate_lods():
    static_meshes = unreal.EditorUtilityLibrary.get_selected_assets()  # Get all selected static meshes
    
    for mesh in static_meshes:
        if isinstance(mesh, unreal.StaticMesh):
            unreal.EditorStaticMeshLibrary.generate_lods_for_mesh(mesh)
            mesh.mark_package_dirty()  # Ensure the changes are saved

# Call the functions
if __name__ == "__main__":
    import_assets()
    organize_assets()
    generate_lods()
