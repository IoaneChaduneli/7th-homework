import os, sys
from PIL import Image, ImageOps

def define_argument(arguments):
    if len(arguments) > 3:
        sys.exit('too much argument')
    if len(arguments) < 3:
        sys.exit('too few argument')

    allowed_extension = ['jpg', 'jpeg', 'png']

    if arguments[1].split('.')[-1] not in allowed_extension:
        sys.exit('Invalid extension')
    if arguments[2].split('.')[-1] not in allowed_extension:
        sys.exit('invalid extension')
    
    t_shirt_path = 'C:\\Users\\DELL\\Desktop\\Front-end Course\\python\\bitcamp\\7th homework\\CS50\\shirt'
    student_path =  'C:\\Users\\DELL\\Desktop\\Front-end Course\\python\\bitcamp\\7th homework\\CS50\\students'

    return t_shirt_path, student_path

def main(arguments):
    t_shirt_path, student_path = define_argument(arguments)
    try:
        input_img = Image.open(os.path.join(t_shirt_path,arguments[1])).convert('RGBA')
        input_img2 = Image.open(os.path.join(student_path, arguments[2]))
    except FileNotFoundError as e:
        sys.exit(f'{e} is not exist')
    else:
        output_img = ImageOps.fit(input_img2, input_img.size)
        output_img.paste(input_img, (0,0), input_img)
        name = arguments[2].split('.')[0] + '.png'
        output_img.save(f'{student_path}\\{name}')



if __name__ == '__main__':
    main(sys.argv)