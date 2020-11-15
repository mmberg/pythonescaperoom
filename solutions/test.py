import datetime

arr1 = ["*","#","nsbg","8"]
arr2 = ["*","#","nsbg","8"]

#if arr1 == arr2:
#    print("jupp")
#    print(arr1[0:3])

#for i, j in enumerate(['foo', 'bar', 'baz']):
#    print(i)

d = datetime.datetime.now()
d_num_raw = d.strftime("%d" "%m" "%Y")
d_num = list(map(int, str(d_num_raw)))

static_chars = [
    "|⁻^^⁻⁻^⁻^⁻⁻^|",
    "|*=≠≠≠==*|",
    "|" + "&nbsp" * 17 + "|",
    "|< ⊛ : ⦻ >|",
    "|⊡--" + "&nbsp" * 7 + "▫" + "&nbsp" * 8 + "--⊡|",
    "|" + "&nbsp" * 14 + "|",
    "| ▭▭▭ |",
    "|_______|",
]

task_messages_ok = [
    "·" * 6 + static_chars[0],
    "·" * 6 + static_chars[1],
    "·" * 6 + static_chars[2],
    "·" * 6 + static_chars[3],
    static_chars[4],
    "·" * 7 + static_chars[5],
    "·" * 7 + static_chars[6],
    "·" * 7 + static_chars[7],
]

task_messages = [
    "•" * d_num[0] + "·" * 6 + static_chars[0],
    "•" * d_num[1] + "·" * 6 + static_chars[1],
    "•" * d_num[2] + "·" * 6 + static_chars[2],
    "•" * d_num[3] + "·" * 6 + static_chars[3],
    "•" * d_num[4] + static_chars[4],
    "•" * d_num[5] + "·" * 7 + static_chars[5],
    "•" * d_num[6] + "·" * 7 + static_chars[6],
    "•" * d_num[7] + "·" * 7 + static_chars[7],
    "&nbsp",
    str(d_num_raw),
    "&nbsp",
    "Was ist das für ein seltsames Bild? Sieht irgendwie aus, als wäre es zeilenweise verschoben... Und was hat diese \
    Zahl in Reihe 10 zu bedeuten? Scheinbar ändert sie sich jeden Tag etwas... ",
    "Es sind 8 Zahlen und das Bild besteht aus 8 Reihen. Wie kannst Du es wieder richtig zusammensetzen?"
    ]

picture_lines = task_messages[0:10]

aligned_picture_lines = []
date_from_picture = list(map(int, str(picture_lines[9])))
for i, elem in enumerate(picture_lines[0:8]):
    picture_line = list(picture_lines[i])
    del picture_line[:date_from_picture[i]]
    picture_line = ''.join(picture_line)    
    aligned_picture_lines.append(str(picture_line))

   
if aligned_picture_lines == task_messages_ok[0:8]:
    print("ok")