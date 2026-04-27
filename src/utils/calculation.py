"""
Coordinate calculation utilities for geospatial operations.
"""

import math
import csv


def calculate_distance(lat1, lon1, lat2, lon2):
    """
    Calculate distance between two coordinates using Haversine formula.
    
    Args:
        lat1, lon1 (float): Starting coordinates
        lat2, lon2 (float): Ending coordinates
    
    Returns:
        float: Distance in meters
    """
    R = 6371000  # Earth radius in meters
    phi1 = math.radians(lat1)
    phi2 = math.radians(lat2)
    delta_phi = math.radians(lat2 - lat1)
    delta_lambda = math.radians(lon2 - lon1)

    a = (math.sin(delta_phi / 2) * math.sin(delta_phi / 2) + 
         math.cos(phi1) * math.cos(phi2) * 
         math.sin(delta_lambda / 2) * math.sin(delta_lambda / 2))
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    return R * c


def divide_space(top_left, bottom_right, square_length, square_width):
    """
    Divide geographic space into grid of squares.
    
    Args:
        top_left (tuple): (latitude, longitude) of top-left corner
        bottom_right (tuple): (latitude, longitude) of bottom-right corner
        square_length (float): Length of each square in meters
        square_width (float): Width of each square in meters
    
    Returns:
        tuple: Three lists of squares divided by thirds
    """
    squares1 = []
    squares2 = []
    squares3 = []

    lat1, lon1 = top_left
    lat2, lon2 = bottom_right

    distance_x = calculate_distance(lat1, lon1, lat1, lon2)
    distance_y = calculate_distance(lat1, lon1, lat2, lon1)

    num_squares_x = math.ceil(distance_x / square_width)
    num_squares_y = math.ceil(distance_y / square_length)

    lat_increment = (lat2 - lat1) / num_squares_y
    lon_increment = (lon2 - lon1) / num_squares_x

    for i in range(num_squares_y):
        for j in range(num_squares_x):
            square_top_left = (lat1 + i * lat_increment, lon1 + j * lon_increment)
            square_bottom_right = (lat1 + (i + 1) * lat_increment, lon1 + (j + 1) * lon_increment)
            square_center = (
                (square_top_left[0] + square_bottom_right[0]) / 2,
                (square_top_left[1] + square_bottom_right[1]) / 2
            )

            if i % 3 == 0:
                squares1.append((square_top_left, square_bottom_right, square_center))
            elif i % 3 == 1:
                squares2.append((square_top_left, square_bottom_right, square_center))
            else:
                squares3.append((square_top_left, square_bottom_right, square_center))

    return squares1, squares2, squares3
