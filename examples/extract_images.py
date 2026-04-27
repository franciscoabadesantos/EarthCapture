"""CLI example for extracting satellite imagery with EarthCapture."""

import argparse
import csv
import os
import sys

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
SRC_ROOT = os.path.join(REPO_ROOT, "src")

# Add src to path
sys.path.insert(0, SRC_ROOT)

from geo_earth_pro.gep import ImageSet
import geo_earth_pro.config as config


def build_parser():
    """Create the CLI argument parser."""
    parser = argparse.ArgumentParser(
        description="Extract imagery from Google Earth Pro for one or more coordinates."
    )
    parser.add_argument(
        "--coordinate",
        help='Single coordinate pair in the form "latitude, longitude".',
    )
    parser.add_argument(
        "--csv",
        default=os.path.join(REPO_ROOT, "data", "sample_coordinates.csv"),
        help="CSV file with latitude and longitude columns.",
    )
    parser.add_argument(
        "--limit",
        type=int,
        default=None,
        help="Maximum number of coordinates to process from the CSV file.",
    )
    return parser


def load_coordinates_from_csv(csv_path):
    """Load coordinates from a CSV file with latitude and longitude columns."""
    coordinates = []
    with open(csv_path, newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        missing = {"latitude", "longitude"} - set(reader.fieldnames or [])
        if missing:
            missing_str = ", ".join(sorted(missing))
            raise ValueError(f"CSV file must include columns: {missing_str}")

        for row in reader:
            coordinates.append(f"{row['latitude']}, {row['longitude']}")

    return coordinates


def run_capture(coordinates):
    """Run the Google Earth Pro capture flow for each coordinate."""
    print("Starting satellite image extraction...")
    print(f"Output folder: {config.IMAGES_FOLDER}")
    os.makedirs(config.IMAGES_FOLDER, exist_ok=True)

    for index, coordinate in enumerate(coordinates, start=1):
        print(f"\n[{index}/{len(coordinates)}] Processing {coordinate}")
        image_set = ImageSet(coordinate)
        image_set.start_downloading()

    print("\nExtraction completed.")
    print(f"Images saved to: {config.IMAGES_FOLDER}")


def main():
    """Entry point for the example CLI."""
    parser = build_parser()
    args = parser.parse_args()

    if args.coordinate:
        coordinates = [args.coordinate]
    else:
        coordinates = load_coordinates_from_csv(args.csv)
        if args.limit is not None:
            coordinates = coordinates[: args.limit]

    if not coordinates:
        raise ValueError("No coordinates were provided.")

    run_capture(coordinates)


if __name__ == "__main__":
    main()
