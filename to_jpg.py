import os
import glob
import cv2

from PIL import Image


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="Resize raw images to uniformed target size."
    )
    parser.add_argument(
        "--raw-dir",
        help="Directory path to raw images.",
        default="./c/crop",
        type=str,
    )
    parser.add_argument(
        "--save-dir",
        help="Directory path to save resized images.",
        default="./c/jpg",
        type=str,
    )
    parser.add_argument(
        "--ext", help="Raw image files extension to change.", default="png", type=str
    )

    args = parser.parse_args()

    raw_dir = args.raw_dir
    save_dir = args.save_dir
    ext = args.ext
    fnames = glob.glob(os.path.join(raw_dir, "*.{}".format(ext)))
    os.makedirs(save_dir, exist_ok=True)
    print(
        "{} files to resize from directory `{}`".format(
            len(fnames), raw_dir
        )
    )
    for i, fname in enumerate(fnames):
        print(".", end="", flush=True)
        im = Image.open(fname)
        rgb_im = im.convert('RGB')
        rgb_im.save(save_dir +'/'+ str(i) + '_transforming.jpg')
        img = cv2.imread(fname)
    print(
        "\nDone transforming {} files.\nSaved to directory: `{}`".format(
            len(fnames), save_dir
        )
    )
