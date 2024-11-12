import argparse

import cv2

from apple_hdr_heic import load_as_bt2100_pq


def main() -> None:
    parser = argparse.ArgumentParser(
        prog="apple-hdr-heic-decoder",
        description=(
            "Decode an HEIC image file containing HDR gain map and other metadata (in Apple's format) to "
            "a PFM file in BT.2100 color space with PQ transfer function."
        ),
    )
    parser.add_argument("input_image", help="Input HEIC image")
    parser.add_argument("output_image", help="Output PFM image")
    args = parser.parse_args()

    assert args.input_image.lower().endswith(".heic")
    assert args.output_image.lower().endswith(".pfm")
    bt2100_pq = load_as_bt2100_pq(args.input_image)
    cv2.imwrite(args.output_image, bt2100_pq[:, :, ::-1])
if __name__ == "__main__":
    main()
