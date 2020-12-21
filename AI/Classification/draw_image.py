import matplotlib.pyplot as plt
from random import randint


## 이미지 출력을 담당하는 부분입니다.
def draw_digit_images(test_X, test_y, predicted):
    number = randint(0, len(test_X))

    images_and_labels = list(zip(test_X, test_y))

    for index, (image, label) in enumerate(images_and_labels[number: number + 4]):
        plt.subplot(2, 4, index + 1)
        plt.axis('off')
        image = image.reshape(8, 8)
        plt.imshow(image, cmap=plt.cm.gray_r, interpolation='nearest')
        plt.title('Training: %i' % label)

    images_and_predictions = list(zip(test_X, predicted))
    # print(images_and_predictions)
    for index, (image, prediction) in enumerate(images_and_predictions[number: number + 4]):
        plt.subplot(2, 4, index + 5)
        plt.axis('off')
        image = image.reshape(8, 8)
        plt.imshow(image, cmap=plt.cm.gray_r, interpolation='nearest')
        plt.title('Prediction: %i' % prediction)

    plt.savefig('digit.png')
