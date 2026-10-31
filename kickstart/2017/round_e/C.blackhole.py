# first thought: binary search for answer

# for small set, just find the furthest pair, and divide by 6

# for large set, three points are on one plane
# actually binary search for answer

# For Type I possibilities, how can we determine whether a radius R is valid? Let K be the center of circle B. Then:
# 
# The distance between K and the point in circle B must be no greater than R, or else the point would not be in B.
# The distance between K and the point in circle A must be no greater than 3R, or else circles A and B would not be connected.
# The distance between K and the point in circle C must be no greater than 3R, or else circles B and C would not be connected.
# It is equivalent to check that point K is in all three of these circles:
# 
# A circle of radius R centered at the point in circle B
# A circle of radius 3R centered at the point in circle A
# A circle of radius 3R centered at the point in circle C
# So, if those three circles have any common intersection, then we know that radius R is valid, without having to choose a specific point K.

