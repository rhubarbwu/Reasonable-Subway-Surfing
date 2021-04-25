from matplotlib import pyplot as plt
from PIL import Image, ImageDraw, ImageFont
import os
import matplotlib.animation as animation

dic = {
    'Vaughan Metropolitan Centre': (307.02094100873285, 52.079219390482876),
    'Highway 407': (308.03086199726727, 92.47605893185982),
    'Pioneer Village': (353.4773064813164, 117.72408364522062),
    'York University': (404.9832768965722, 148.02171330125338),
    'Finch West': (450.42972138062134, 173.26973801461395),
    'Downsview Park': (497.89600784173945, 198.51776272797474),
    'Sheppard West': (545.3622943028574, 227.8054713954732),
    'Wilson': (545.3622943028574, 260.1229430285748),
    'Yorkdale': (546.3722152913919, 287.3908097190043),
    'Lawrence West': (545.3622943028574, 312.638834432365),
    'Glencairn': (546.3722152913919, 336.87693815719115),
    'Eglinton West': (545.3622943028574, 360.105120893483),
    'St. Clair West': (646.3543931563001, 417.6706172399453),
    'Dupont': (696.8504425830214, 446.95832590744374),
    'Spadina (1)': (697.8603635715558, 498.4642963226995),
    'St. George (1)': (769.5647537575001, 516.6428741163191),
    'Museum': (772.5945167231034, 565.1190815659717),
    "Queen's Park": (772.5945167231034, 593.3968692449356),
    'St. Patrick': (772.5945167231034, 621.6746569238995),
    'Osgoode': (771.5845957345689, 650.9623655913979),
    'St. Andrew': (770.5746747460346, 681.2599952474307),
    'Union': (823.0905661498248, 732.7659656626864),
    'King': (874.5965365650804, 680.2500742588962),
    'Queen': (874.5965365650804, 652.9822075684667),
    'Dundas': (874.5965365650804, 620.6647359353651),
    'College': (872.5766945880116, 593.3968692449356),
    'Wellesley': (872.5766945880116, 560.0694766232995),
    'Bloor-Yonge (1)': (873.5866155765461, 515.6329531277847),
    'Rosedale': (875.606457553615, 473.21627160933883),
    'Summerhill': (875.606457553615, 444.9384839303748),
    'St. Clair': (875.606457553615, 418.6805382284798),
    'Davisville': (875.606457553615, 384.34322461830925),
    'Eglinton': (875.606457553615, 359.0951999049486),
    'Lawrence': (875.606457553615, 311.62891344383047),
    'York Mills': (875.606457553615, 265.1725479712468),
    'Sheppard-Yonge (1)': (875.606457553615, 228.8153923840075),
    'North York Centre': (874.5965365650804, 186.3987108655615),
    'Finch': (872.5766945880116, 154.0812392324599),
    'Kipling': (157.55263470563773, 519.6726370819224),
    'Islington': (194.91971128141148, 518.662716093388),
    'Royal York': (233.2967088457197, 516.6428741163191),
    'Old Mill': (269.65386443295904, 514.6230321392503),
    'Jane': (310.0507039743361, 514.6230321392503),
    'Runnymede': (345.3979385730411, 516.6428741163191),
    'High Park': (382.76501514881477, 514.6230321392503),
    'Keele': (420.1320917245886, 514.6230321392503),
    'Dundas West': (461.53885225450006, 516.6428741163191),
    'Lansdowne': (496.88608685320503, 518.662716093388),
    'Dufferin': (537.2829263945821, 518.662716093388),
    'Ossington': (571.6202400047525, 518.662716093388),
    'Christie': (611.0071585575952, 516.6428741163191),
    'Bathurst': (649.3841561219034, 517.6527951048536),
    'Spadina (2)': (702.909968514228, 520.6825580704568),
    'St. George (2)': (772.5945167231034, 520.6825580704568),
    'Bay': (823.0905661498248, 518.662716093388),
    'Bloor-Yonge (2)': (872.5766945880116, 518.662716093388),
    'Sherbourne': (947.3108477395592, 517.6527951048536),
    'Castle Frank': (1007.9061070516248, 516.6428741163191),
    'Broadview': (1050.3227885700708, 517.6527951048536),
    'Chester': (1082.6402602031724, 517.6527951048536),
    'Pape': (1125.0569417216182, 517.6527951048536),
    'Donlands': (1157.37441335472, 517.6527951048536),
    'Greenwood': (1199.7910948731658, 517.6527951048536),
    'Coxwell': (1236.1482504604053, 517.6527951048536),
    'Woodbine': (1270.4855640705757, 517.6527951048536),
    'Main Street': (1312.9022455890215, 516.6428741163191),
    'Victoria Park': (1364.4082160042774, 465.1369037010634),
    'Warden': (1417.934028396602, 410.60117032020435),
    'Kennedy (2)': (1469.4399988118578, 361.1150418820174),
    'Kennedy (3)': (1469.4399988118578, 361.1150418820174),
    'Lawrence East': (1470.449919800392, 313.6487554208994),
    'Ellesmere': (1469.4399988118578, 271.2320739024535),
    'Midland': (1495.6979445137529, 245.98404918909273),
    'Scarborough Centre': (1532.0551001009921, 245.98404918909273),
    'McCowan': (1571.4420186538348, 242.9542862234896),
    'Sheppard-Yonge (4)': (873.5866155765461, 226.79555040693867),
    'Bayview': (957.4100576249034, 226.79555040693867),
    'Bessarion': (1033.1541317649856, 228.8153923840075),
    'Leslie': (1116.9775738133428, 228.8153923840075),
    'Don Mills': (1197.771252896097, 227.8054713954732)
}


def draw_likelihood_circles_on_image(image, likelihoods, iteration, station,
                                     observation):
    assert (len(likelihoods) == len(dic))
    draw = ImageDraw.Draw(image, "RGBA")
    j = 0
    draw.rectangle((0, 640, 630, 800), fill=(255, 255, 255))
    for name, (x, y) in dic.items():
        r = likelihoods[j] * 100
        draw.ellipse((x - r, y - r, x + r, y + r),
                     fill=(255, 0, 0, 100),
                     outline=(255, 0, 0))
        j += 1

    # draws a blue circle at the actual station
    x, y = dic[station.name]
    r = 30
    draw.ellipse((x - r, y - r, x + r, y + r),
                 fill=(0, 0, 255, 100),
                 outline=(0, 0, 255))

    station_text = f"station: {station.name}"
    iteration_text = f"iteration: {iteration}"
    observation_text1 = f"idle time: {round(observation[0], 2)}s"
    observation_text2 = f"number of patrons: {round(observation[1])}"
    font = ImageFont.truetype("lib/visualization/arial.ttf", size=30)
    draw.text((70, 630), iteration_text, font=font, fill=(0, 0, 0))
    draw.text((70, 670), station_text, font=font, fill=(0, 0, 0))
    draw.text((70, 710), observation_text1, font=font, fill=(0, 0, 0))
    draw.text((70, 750), observation_text2, font=font, fill=(0, 0, 0))


def show_likelihoods(image_file,
                     likelihoods,
                     stations,
                     observations,
                     output_dir=None):
    image = Image.open(image_file)
    likelihoods = likelihoods[1:]
    n = len(likelihoods)
    images = [image.copy() for _ in range(n)]
    fig, ax = plt.subplots()
    ims = []
    for i in range(n):
        cur_image = images[i]
        draw_likelihood_circles_on_image(cur_image, likelihoods[i], i + 1,
                                         stations[i], observations[i])
        im = ax.imshow(cur_image, animated=True)
        if i == 0:
            ax.imshow(cur_image)  # not sure if this is needed
        ims.append([im])
    ani = animation.ArtistAnimation(fig,
                                    ims,
                                    interval=1000,
                                    blit=True,
                                    repeat_delay=0)
    plt.show()
    if output_dir:
        print(f"Saving the visualization to {output_dir}.")
        print("This may take a while.")
        movie_filename = os.path.join(output_dir, f"movie.mp4")
        ani.save(movie_filename)
        for i in range(n):
            output_filename = os.path.join(output_dir, f"frame{i}.png")
            images[i].save(output_filename)
