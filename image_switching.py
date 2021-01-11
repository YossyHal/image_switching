import cv2


def main(numberOfPeople):
    # 評価用画像
    test_image_path = 'image/{}nin.jpg'.format(numberOfPeople)
    test_image = cv2.imread(test_image_path)

    # 壁紙
    wall_paper = cv2.imread('image/wall_paper.jpg')

    for i in range(30):
        # 評価用画像をフルスクリーンで表示する
        cv2_imshow_fullscreen('A', test_image)

        # 5秒待機
        cv2.waitKey(5000)
        cv2.destroyAllWindows()

        # 壁紙を表示
        cv2_imshow_fullscreen('B', wall_paper)

        # 3秒待機
        cv2.waitKey(3000)
        cv2.destroyAllWindows()


def cv2_imshow_fullscreen(winname, img):
    """
    フルスクリーンで画像を表示する
    """
    cv2.namedWindow(winname, cv2.WINDOW_NORMAL)
    cv2.setWindowProperty(
        winname,
        cv2.WND_PROP_FULLSCREEN,
        cv2.WINDOW_FULLSCREEN)
    cv2.imshow(winname, img)


if __name__ == '__main__':
    numberOfPeople = 5
    main(numberOfPeople)
