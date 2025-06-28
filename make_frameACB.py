import os

base_dir = '/home/ray/EulerMormer/datasets/train/train_vid_frames'


dirs = sorted([i for i in os.listdir(base_dir) if i.startswith('val_')])

for d in dirs:
    print(d)
    os.chdir(os.path.join(base_dir, d))
    os.mkdir('frameA')
    os.mkdir('frameC')
    files = sorted([f for f in os.listdir('.') if f.endswith('.png')], key=lambda x: int(x.split('.')[0]))
    os.system('cp ./*png frameA && cp ./*png frameC')
    os.remove(os.path.join('frameA', files[-1]))
    os.remove(os.path.join('frameC', files[0]))
    for f in sorted(os.listdir('frameC'), key=lambda x: int(x.split('.')[0])):
        f_new = os.path.join('frameC', '%06d' % (int(f.split('.')[0])-1) + '.png')
        f = os.path.join('frameC', f)
        os.rename(f, f_new)
    os.system('cp -r frameC frameB')
    os.system('rm ./*.png')
