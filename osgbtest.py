import pyproj

def change_initial_coordinates(osgb_file, new_coordinates):
    # Define the original coordinate system (e.g., EPSG:4326)
    original_crs = pyproj.CRS.from_epsg(4326)

    # Define the new coordinate system (e.g., EPSG:3857)
    new_crs = pyproj.CRS.from_epsg(3857)

    # Create a transformer to convert between the coordinate systems
    transformer = pyproj.Transformer.from_crs(original_crs, new_crs, always_xy=True)

    # Read the osgb file and get the original coordinates
    # Assuming the coordinates are in latitude and longitude format
    with open(osgb_file, 'r') as file:
        original_coordinates = file.read().split(',')

    # Convert the original coordinates to the new coordinate system
    new_coordinates = transformer.transform(original_coordinates[0], original_coordinates[1])

    # Update the osgb file with the new coordinates
    with open(osgb_file, 'w') as file:
        file.write(f'{new_coordinates[0]},{new_coordinates[1]}')

# Usage example
osgb_file = '/path/to/osgb/file.osgb'
new_coordinates = (40.7128, -74.0060)  # New coordinates in latitude and longitude format
change_initial_coordinates(osgb_file, new_coordinates)