def get_program_area(filePath):
    areas = filePath.split("\\")
    
    if len(areas) > 1:
        ret = areas[1]
    else:
        ret = 'N/A'
    return ret

def has_numbers(string):
    return any(char.isdigit() for char in string)
    

def get_department(filePath):
    areas = filePath.split("\\")
    if areas[2] == 'Archived' or has_numbers(areas[2]):
        ret = 'N/A'
    else:
        ret = areas[2]
        
    return ret
    

