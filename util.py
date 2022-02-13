import math

# all in svg context


def points_loop(points, xy):
    d = []
    x = xy[0];
    y = xy[1];
    for point in points:
        if(len(d) == 0):
            d.append(f'M {point[x]} {point[y]} ')
        else:
            d.append(f'L {point[x]} {point[y]} ')

    d.append("Z ")
    dtxt = "".join(d)
    return dtxt

def generatePathDescription(points_w_md):
# transform
    points = []
    for point_w_md in points_w_md:
        points.append(point_w_md["point"])

    return points_loop(points, ["x", "y"])

def pointsToD(data_list):
    d = []

    for point_list in data_list:
        d.append(points_loop(point_list, ["x", "y"]))

    
    return "".join(d)

def md_points_2_path(points_w_md):
    path_value = "<path\n"
    path_value = path_value + "style=\"fill:none;stroke:#000000;stroke-width:0.033mm;stroke-linecap:butt;stroke-linejoin:miter;stroke-opacity:1\"\n"
    path_value = path_value + "d=\"" + generatePathDescription(points_w_md) + "\" />\n"

    return path_value

def path_svg(path_decription):
    path_value = "<path\n"
    path_value = path_value + "style=\"fill:none;stroke:#000000;stroke-width:0.033mm;stroke-linecap:butt;stroke-linejoin:miter;stroke-opacity:1\"\n"
    path_value = path_value + "d=\"" + path_decription + "\" />\n"

    return path_value

def points_2_path(points):
    path_value = "<path\n"
    path_value = path_value + "style=\"fill:none;stroke:#000000;stroke-width:0.033mm;stroke-linecap:butt;stroke-linejoin:miter;stroke-opacity:1\"\n"
    path_value = path_value + "d=\"" + pointsToD(points) + "\" />\n"

    return path_value

def calc_point_dist(p1,p2):
    xd = p1["x"] - p2["x"]
    yd = p1["y"] - p2["y"]

    if xd == 0:
        return abs(yd)

    if yd == 0:
        return abs(xd)

    return math.sqrt(xd*xd + yd*yd)

def calculate_path_length(points):
    
    total_d = 0
    for index in range(len(points) - 1):
        p1 = points[index]
        p2 = points[index + 1]
        total_d += calc_point_dist(p1,p2)
    
    return total_d

