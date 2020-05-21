from PIL import Image
import os

# размеры для вставки
size_right = (800, 800)
size_top = (1500, 1500)
size_center = (1900, 1900)
size_web = (1200, 1200)
# координаты для вставки
box_right = (2000, 700)
box_top = (1200, 800)
box_center = (1100, 1200)

# making dirs
if not(os.path.exists('format')):
    os.mkdir('format')


def paste_image(name, tshort, pasting_file, pasting_size, box):
    # making new_filename
    tshort_name = os.path.splitext(tshort)[0]
    pasting_file_name = os.path.splitext(pasting_file)[0]
    new_filename = str(tshort_name + '_' + pasting_file_name + '_' + name + '.jpg')
    test_path = str('format/{}/{}'.format(pasting_file_name, new_filename))

    if not(os.path.exists(test_path)):

        # open images
        tshort_img = Image.open('./tshorts/' + tshort)
        pasting_image = Image.open('./pasting_images/' + pasting_file)
        # paste images
        pasting_image.thumbnail(pasting_size) # changing size
        tshort_img.paste(pasting_image, box, pasting_image) # paste

        # try make new dir
        if not(os.path.exists('format/{}'.format(pasting_file_name))):
            os.mkdir('format/{}'.format(pasting_file_name))
            print('Make new dir: ' + 'format/{}'.format(pasting_file_name))

        # saving image
        tshort_img.thumbnail(size_web) # make size for web
        tshort_img.save('format/{}/{}'.format(pasting_file_name, new_filename))
        print('Made new one picture: ' + new_filename)


# main program
for tshort in os.listdir('./tshorts'):
    if tshort.endswith('.jpg') or tshort.endswith('.png'):

        for file in os.listdir('./pasting_images'):
            if file.endswith('.jpg') or file.endswith('.png'):

                paste_image('right', tshort, file, size_right, box_right)
                paste_image('top', tshort, file, size_top, box_top)
                paste_image('center', tshort, file, size_center, box_center)

print("done")

exit()