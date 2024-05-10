import io
import matplotlib.pyplot as plt
from PIL import Image
from PyQt5.QtGui import QImage, QPixmap

def Priority_rm(Tache):
    for i in range(len(Tache) - 1):
        if Tache[i]['Period'] > Tache[i + 1]['Period']:
            temp = Tache[i]
            Tache[i] = Tache[i + 1]
            Tache[i + 1] = temp
    return  Tache
def Priority_dm(Tache):
    for i in range(len(Tache) - 1):
        if Tache[i]['Dead line'] > Tache[i + 1]['Dead line']:
            temp = Tache[i]
            Tache[i] = Tache[i + 1]
            Tache[i + 1] = temp
    return  Tache

def Draw(Tache, XY, LCM, GCD, length, title):
    fig = plt.figure(figsize=(10, 6))

    j = 0
    width = length + 1
    for T in Tache:
        for k in range(T['Period'], LCM + 1, T['Period']):
            x = [k, k]
            y = [0, 4]
            plt.plot(x, y, linewidth=str(width), linestyle=':', color=T['color'])
        width -= 1

        x = XY[j][0]
        y = [T['y'], T['y']]
        plt.plot(x, y, linewidth="5", color=T['color'], label=T['name'])

        for i in range(1, len(XY[j])):
            x = XY[j][i]
            plt.plot(x, y, linewidth="5", color=T['color'])
        j += 1

    x = range(0, LCM + GCD, GCD)
    y = range(0, length + 1)
    plt.xticks(x)
    plt.yticks(y)
    plt.xlim(0, max(x) + 1)
    plt.ylim(0, max(y) + 1)
    plt.grid()
    plt.title(title)
    plt.legend()

    # Save the plot to a buffer
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)

    # Convert the buffer to a QImage
    image = Image.open(buffer)
    qimage = QImage(image.tobytes(), image.width, image.height, QImage.Format_RGBA8888)

    return qimage
