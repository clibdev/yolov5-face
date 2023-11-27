from scipy.io import loadmat

filename = 'wider_face_val_gt.txt'

easy = loadmat('ground_truth/wider_easy_val.mat')
medium = loadmat('ground_truth/wider_medium_val.mat')
hard = loadmat('ground_truth/wider_hard_val.mat')

gt_list = [easy['gt_list'], medium['gt_list'], hard['gt_list']]

data = ''
for i in range(len(easy['event_list'])):
    for j in range(len(easy['file_list'][i][0])):
        data += easy['event_list'][i][0][0] + '/' + easy['file_list'][i][0][j][0][0] + '.jpg\n'
        for gt in gt_list:
            data += ' '.join([str(val[0]) for val in gt[i][0][j][0]]) + '\n'

with open(filename, 'w') as file:
    file.write(data)
