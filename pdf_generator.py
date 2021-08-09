import numpy as np
import cv2
import sys
from fpdf import FPDF
import os

# filename without .txt
filename = 'sample'


class PDF(FPDF):
    pass


ARUCO_DICT = {
    "DICT_4X4_50": cv2.aruco.DICT_4X4_50,
    "DICT_4X4_100": cv2.aruco.DICT_4X4_100,
    "DICT_4X4_250": cv2.aruco.DICT_4X4_250,
    "DICT_4X4_1000": cv2.aruco.DICT_4X4_1000,
    "DICT_5X5_50": cv2.aruco.DICT_5X5_50,
    "DICT_5X5_100": cv2.aruco.DICT_5X5_100,
    "DICT_5X5_250": cv2.aruco.DICT_5X5_250,
    "DICT_5X5_1000": cv2.aruco.DICT_5X5_1000,
    "DICT_6X6_50": cv2.aruco.DICT_6X6_50,
    "DICT_6X6_100": cv2.aruco.DICT_6X6_100,
    "DICT_6X6_250": cv2.aruco.DICT_6X6_250,
    "DICT_6X6_1000": cv2.aruco.DICT_6X6_1000,
    "DICT_7X7_50": cv2.aruco.DICT_7X7_50,
    "DICT_7X7_100": cv2.aruco.DICT_7X7_100,
    "DICT_7X7_250": cv2.aruco.DICT_7X7_250,
    "DICT_7X7_1000": cv2.aruco.DICT_7X7_1000,
    "DICT_ARUCO_ORIGINAL": cv2.aruco.DICT_ARUCO_ORIGINAL,
    "DICT_APRILTAG_16h5": cv2.aruco.DICT_APRILTAG_16h5,
    "DICT_APRILTAG_25h9": cv2.aruco.DICT_APRILTAG_25h9,
    "DICT_APRILTAG_36h10": cv2.aruco.DICT_APRILTAG_36h10,
    "DICT_APRILTAG_36h11": cv2.aruco.DICT_APRILTAG_36h11
}


def main():
    # import settings from txt file
    script = open('./'+filename+'.txt', 'r')
    my_format = script.readline().split()[1]
    my_orientation = script.readline().split()[1][0]
    my_unit = script.readline().split()[1]
    my_library = script.readline().split()[1]
    my_pdf = PDF(orientation=my_orientation, unit=my_unit, format=my_format)

    # create directory for marker image files, if there isn't one yet
    folder_name = 'temporary_markers'
    try:
        os.makedirs(folder_name)
    except FileExistsError:
        pass

    # check if library is valid
    if ARUCO_DICT.get(my_library, None) is None:
        print("[INFO] ArUCo tag of '{}' is not supported".format(my_library))
        sys.exit(0)

    # load the ArUCo dictionary
    arucoDict = cv2.aruco.Dictionary_get(ARUCO_DICT[my_library])

    # number for file name for each markers
    num = 1

    while True:
        line = script.readline()
        # create new page
        if line == '':
            break
        elif line == '\n':
            my_pdf.add_page()
        else:
            # get info on markers
            [x, y, size, id] = line.split()
            x, y, size, id = int(x), int(y), int(size), int(id)
            # write marker image in jpg
            img_size = 500
            img_output = './'+folder_name+'/marker'+str(num)+'.jpg'
            num += 1
            tag = np.zeros((img_size, img_size, 1), dtype="uint8")
            cv2.aruco.drawMarker(arucoDict, id, 500, tag, 1)
            cv2.imwrite(img_output, tag)
            # put image in pdf
            my_pdf.image(img_output, x, y, size, size, type='', link='')

    # remove generated jpg files
    for i in range(1, num):
        img_to_delete = './'+folder_name+'/marker'+str(i)+'.jpg'
        os.remove(img_to_delete)
    os.rmdir(folder_name)

    # save pdf
    my_pdf.output('./'+filename+'.pdf', 'F')


if __name__ == '__main__':
    main()
