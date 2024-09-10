def hex_to_float_rgb(hex_color):
    # Remove the '#' if present
    hex_color = hex_color.lstrip('#')

    # Convert hex to integer values for R, G, B
    r = int(hex_color[0:2], 16) / 255.0
    g = int(hex_color[2:4], 16) / 255.0
    b = int(hex_color[4:6], 16) / 255.0

    # Return as tuple of floats
    return (r, g, b, 1.0)
