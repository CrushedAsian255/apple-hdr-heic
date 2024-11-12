# Convert HDR HEICs to JPEG XL

A tool to decode photos (HEIC files) taken on an iPhone that contain HDR gain map, and convert it to a PFM format HDR representation as per [Rec. 2100](https://en.wikipedia.org/wiki/Rec._2100) with PQ transfer function.

The PFM can be converted to JPEG XL using `cjxl <input.pfm> <output.jxl> -x color_space=RGB_D65_202_Per_PeQ`

Disclaimer: This project is NOT affiliated with, or endorsed by, Apple Inc. or any of its subsidiaries.

## Pre-requisites

* Python 3.10+
* [`exiftool`](https://exiftool.org/) 12.54+
  - For Ubuntu or Debian, do `sudo apt install libimage-exiftool-perl`
  - For other Linux distros, search `exiftool` using your package manager
  - For Mac or Windows, follow the instructions in website
  - For Windows, it is also available via [Scoop](https://scoop.sh/)

## Installation

Clone this repository, create a python environment and do:

```
pip install .
```

## Usage

```
apple-hdr-heic-decode input.heic output.pfm
cjxl output.pfm output.jxl -x color_space=RGB_D65_202_Per_PeQ
```

## Development

Please submit any bugs relating to the decoing [upstream](https://github.com/johncf/apple-hdr-heic/tree/master).