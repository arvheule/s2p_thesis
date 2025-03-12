import os
import open3d as o3d

def find_ply_files(directory):
    """Recursively finds all .ply files in the given directory and subdirectories."""
    ply_files = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.lower().endswith(".ply"):
                ply_files.append(os.path.join(root, file))
    return ply_files


def create_big_ply_file(directory):
    ply_files = find_ply_files(directory)

	# Load all point clouds
    point_clouds = [o3d.io.read_point_cloud(f) for f in ply_files]

	# Merge point clouds
    merged_pcd = point_clouds[0]
    for pcd in point_clouds[1:]:
        merged_pcd += pcd  # Add points to the first cloud

    o3d.io.write_point_cloud(f"{directory}/general_point_cloud.ply", merged_pcd)