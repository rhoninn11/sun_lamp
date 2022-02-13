import pattern_generation as pagen
import svg_const as svgc
import util


hexagonal_prameters = {
    "x_limit": 297.0,
    "y_limit": 420.0,
    "x_section_count": 5,
    "y_section_count": 1,
    "start_hexagon_size": 3,
    "end_hexagon_size": 0.256,
    "start_hexagon_spacing": 0.86,
    "end_hexagon_spacing": 0.1,
    "secion_padding": 10,
    "shrinkage_factor": 0,
    "padding_procent": 0.05,
    "x_start": 0.0,
    "y_start": 0.0,
    "add_holes": True,
    "hole_offest": 10,
    "hole_size": 3,
    "predefined_size_and_spacing": True,
    "size_array": [[2.13, 1.84, 1.55, 1.26, 0.97]],
    "spacing_array": [[0.86, 0.86, 0.86, 0.75, 0.68]],
    "add_border": False,
    "border_offset": 3
}

x_space = 297.0
y_space = 420.0

x_meta_sections = 1
y_meta_sections = 6

per_x_meta_space = x_space/x_meta_sections
per_y_meta_space = y_space/y_meta_sections

hexagonal_prameters["x_limit"] = per_x_meta_space
hexagonal_prameters["y_limit"] = per_y_meta_space

svg = []
svg.append(svgc.svg_header())
for x_meta_section in range(x_meta_sections):
    for y_meta_section in range(y_meta_sections):
        hexagonal_prameters["x_start"] = per_x_meta_space*x_meta_section
        hexagonal_prameters["y_start"] = per_y_meta_space*y_meta_section
        elo = pagen.generate_hexagonal_patern_paths;
        svg.append("".join(pagen.generate_hexagonal_patern_paths(hexagonal_prameters)))


svg.append(svgc.svg_tail())

result_svg = "".join(svg);

with open('result.svg', 'w') as file:
    file.write(result_svg)

# fractal_len = util.calculate_path_length(fractal_points)
print(f'Fractal lines total length {fractal_len}')

