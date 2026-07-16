import re

with open('profile-3d-contrib/profile-night-green.svg', 'r', encoding='utf-8') as f:
    data = f.read()

# 1. Background transparent
data = data.replace('fill="#00000f"', 'fill="transparent"')

# 2. Move pie chart to the right side
# The pie chart is in a group: <g transform="translate(40, 520)">
# Let's change the X offset from 40 to 860
data = data.replace('transform="translate(40, 520)"', 'transform="translate(860, 520)"')

# 3. Hide stats that are 0 in score (Stars, Forks)
# The star icon group and text
data = re.sub(r'<g transform="translate\(608, 802\), scale\(2\)"><path[^>]*></path></g><text[^>]*>0<title>0</title></text>', '', data)
# The fork icon group and text
data = re.sub(r'<g transform="translate\(736, 802\), scale\(2\)"><path[^>]*></path></g><text[^>]*>0<title>0</title></text>', '', data)

# 4. Hide radar chart axes that have 0
# Non-greedy match for a single axis with 0 title
data = re.sub(r'<g class="axis">.*?<title>0</title></text></g>', '', data)

# 5. Hide the '0' values from the contribution numbers themselves?
# The user said "dont show stats that are 0 in score". This means ANY stat with 0.
# The radar and the stars/forks are the only ones with 0.

with open('profile-3d-contrib/test_output.svg', 'w', encoding='utf-8') as f:
    f.write(data)
