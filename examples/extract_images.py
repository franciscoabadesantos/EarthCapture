"""
Example: Extract satellite imagery for multiple locations

This example demonstrates how to:
1. Load coordinates from a CSV file
2. Extract current and historical imagery from Google Earth Pro
3. Download images for multiple locations in batch
"""

import time
import pandas as pd
import ast
import math
import sys
import os

# Add src to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from geo_earth_pro.gep import ImageSet
import geo_earth_pro.config as config


def main():
    """Main extraction workflow"""
    
    # Configuration
    print("Starting Satellite Image Extraction...")
    print(f"Output folder: {config.IMAGES_FOLDER}")
    
    # Create output folder if it doesn't exist
    if not os.path.exists(config.IMAGES_FOLDER):
        os.makedirs(config.IMAGES_FOLDER)
    
    # Example 1: Extract from single coordinates
    print("\n--- Single Location Extraction ---")
    single_coord = "38.77015820543463, -9.1190039734357"
    image_set = ImageSet(single_coord)
    image_set.start_downloading()
    
    # Example 2: Extract from multiple coordinates (from CSV)
    print("\n--- Batch Extraction from CSV ---")
    # Prepare coordinates
    coordinates_list = [
        "38.77015820543463, -9.1190039734357",
        "38.70311901975468, -9.418746920569667",
        "38.98489238729813, -9.202362384460136",
    ]
    
    # Process each location
    for i, coord in enumerate(coordinates_list, 1):
        print(f"\nProcessing location {i}/{len(coordinates_list)}: {coord}")
        try:
            image_set = ImageSet(coord)
            image_set.start_downloading()
            print(f"Successfully extracted images for: {coord}")
        except Exception as e:
            print(f"Error processing {coord}: {str(e)}")
    
    print("\nExtraction completed!")
    print(f"Images saved to: {config.IMAGES_FOLDER}")


if __name__ == "__main__":
    main()
