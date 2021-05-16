import sass
import os
# os.mkdir('css')
# os.mkdir('sass')
with open('test.scss', 'r') as fl:
    scss_data = fl.read()

with open('sass/test.scss', 'w') as example_scss:
     example_scss.write(scss_data)

sass.compile(dirname=('sass', 'css'), output_style='compressed')
with open('css/test.css') as example_css:
    print(example_css.read())