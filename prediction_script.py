import argparse
from pathlib import Path
import os
import subprocess



def detection(opt):
    command = f"python detect.py --weights {opt.weights[0]} --source {opt.source} --img {opt.img} --project {opt.project}"
    # Run the command as a subprocess
    subprocess.run(command, shell=True)
        


def parse_opt():
    parser = argparse.ArgumentParser()
    parser.add_argument('--weights', nargs='+', type=str, default= ['../results_1/best.pt'], help='model path or triton URL')
    parser.add_argument('--source', type=str, default='../dataset/test/images/VID_2021_09_29_11_02_26_21_10_01_00_22_45_output_789.jpg', help='file/dir/URL/glob/screen/0(webcam)')
    parser.add_argument('--project', type = str, default= './outputs', help='save results to project/name')
    parser.add_argument('--img', nargs='+', type=int, default=640, help='inference size h,w')
    opt = parser.parse_args() 
    return opt


if __name__ == '__main__':
    opt = parse_opt()
    detection(opt)