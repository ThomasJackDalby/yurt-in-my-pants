import math
from spatial.vector2d import Vector2D

MULT = [
  [1,  0,  0, -1, -1,  0,  0,  1],
  [0,  1, -1,  0,  0, -1,  1,  0],
  [0,  1,  1,  0,  0, -1, -1,  0],
  [1,  0,  0,  1, -1,  0,  0, -1],
]

def getVisiblePoints(vantage_point, get_allows_light, max_distance=10):
  los_cache = set()
  los_cache.add(vantage_point)
  for region in range(8):
    _cast_light(
      los_cache, get_allows_light,
      vantage_point.x, vantage_point.y, 1, 1.0, 0.0, max_distance,
      MULT[0][region], MULT[1][region],
      MULT[2][region], MULT[3][region])
  return los_cache

def _cast_light(los_cache, get_allows_light, cx, cy, row, start, end, radius, xx, xy, yx, yy):
  if start < end:
    return

  radius_squared = radius*radius

  for j in range(row, radius+1):
    dx, dy = -j-1, -j
    blocked = False
    while dx <= 0:
      dx += 1
      # Translate the dx, dy coordinates into map coordinates:
      X, Y = cx + dx * xx + dy * xy, cy + dx * yx + dy * yy
      point = Vector2D(X, Y)
      # l_slope and r_slope store the slopes of the left and right
      # extremities of the square we're considering:
      l_slope, r_slope = (dx-0.5)/(dy+0.5), (dx+0.5)/(dy-0.5)
      if start < r_slope:
        continue
      elif end > l_slope:
        break
      else:
        # Our light beam is touching this square; light it:
        if dx*dx + dy*dy < radius_squared:
          los_cache.add(point)
        if blocked:
          # we're scanning a row of blocked squares:
          if not get_allows_light(point):
            new_start = r_slope
            continue
          else:
            blocked = False
            start = new_start
        else:
          if not get_allows_light(point) and j < radius:
            # This is a blocking square, start a child scan:
            blocked = True
            _cast_light(
              los_cache, get_allows_light,
              cx, cy, j+1, start, l_slope,
              radius, xx, xy, yx, yy)
            new_start = r_slope
    # Row is scanned; do next row unless last square was blocked:
    if blocked:
        break