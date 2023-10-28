import re
import matplotlib.pyplot as plt

path = 'train/yolov5l-face.txt'

with open(path) as file:
    text = file.read()
    results = re.findall(' +Epoch.+\\s.+(?:\\s +Class.+\\s.+)*', text)

    epoch = []
    memory = []
    box = []
    obj = []
    landmark = []
    total = []
    targets = []
    train_time = []
    train_iters = []
    eval_time = []
    eval_iters = []
    precision = []
    recall = []
    map_05 = []
    map_05_095 = []

    for result in results:
        lines = result.splitlines()

        data = re.search(
            '(\\d+)/\\d+ +?([\\d.]+)G +?([\\d.]+) +?([\\d.]+) +? 0 +?([\\d.]+) +?([\\d.]+) +?(\\d+) +? 800: 100%.+ 801/801 \\[(\\d+):(\\d+)<.*, +?([\\d.]+)it/s]',
            lines[1].strip()
        )

        epoch.append(data[1])
        memory.append(data[2])
        box.append(data[3])
        obj.append(data[4])
        landmark.append(data[5])
        total.append(data[6])
        targets.append(data[7])
        train_time.append(60 * int(data[8]) + int(data[9]))
        train_iters.append(data[10])

        data = re.search('\\[(\\d+):(\\d+)<.+, +([\\d.]+)it/s', '' if len(lines) == 2 else lines[2].strip())

        eval_time.append(0 if data is None else 60 * int(data[1]) + int(data[2]))
        eval_iters.append(0 if data is None else data[3])

        data = re.search(
            '\\+\\d+ +([\\d.]+) +([\\d.]+) +([\\d.]+) +([\\d.]+)',
            '' if len(lines) == 2 else lines[3].strip()
        )

        precision.append(0 if data is None else data[1])
        recall.append(0 if data is None else data[2])
        map_05.append(0 if data is None else data[3])
        map_05_095.append(0 if data is None else data[4])

    total_time = sum(train_time) + sum(eval_time)
    total_hours = total_time / 3600.0

    print('Total training time: %.2f hours' % total_hours)

    plt.plot(epoch, memory)
    plt.show()
