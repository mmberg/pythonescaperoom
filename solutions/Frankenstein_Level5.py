def run(task_messages):
    picture_lines = task_messages[0:10]
    aligned_picture_lines = []
    date_from_picture = list(map(int, str(picture_lines[9])))
    
    for i, elem in enumerate(picture_lines[0:8]):
        picture_line = list(picture_lines[i])
        del picture_line[:date_from_picture[i]]
        picture_line = ''.join(picture_line)    
        aligned_picture_lines.append(str(picture_line))
    
    return aligned_picture_lines