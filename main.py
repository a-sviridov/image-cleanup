import sys
import docker
import json
import datetime
from datetime import timedelta

def main():

    minutes_delete = int(sys.argv[1])
    save_lates_images = int(sys.argv[2])


    client = docker.from_env()
    img_list = client.images.list()

    img_count=0

    for img in img_list:
        img_count += 1

        im_atr_u=img.attrs

        print(img_count, im_atr_u["Id"], im_atr_u["Created"])

        parsed_time = im_atr_u["Created"].split('.')[0].lstrip().split(' ')[0]
        parsed_time = datetime.datetime.strptime(parsed_time, '%Y-%m-%dT%X')

        if img_count > save_lates_images:
            if parsed_time < (datetime.datetime.now() - datetime.timedelta(minutes=minutes_delete)) :
                 client.images.remove(im_atr_u["Id"],force=True)


if __name__ == '__main__':
    main()
